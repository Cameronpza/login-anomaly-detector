import streamlit as st
import pandas as pd
import sqlite3

# Connect to your database file
conn = sqlite3.connect("logins.db")

st.title("Login Anomaly Detector")
st.write("A simple dashboard flagging suspicious login activity.")

# --- Flag 1: Weak Auth ---
st.header("1. Weak Auth Logins (basic username/password)")
weak_auth = pd.read_sql_query(
    "SELECT user_id, department, auth_type FROM fake_logins WHERE auth_type = 'basic'",
    conn
)
st.write(f"Found {len(weak_auth)} logins using weak auth.")
st.dataframe(weak_auth)

# --- Flag 2: Repeated Failed Logins ---
st.header("2. Repeated Failed Logins (5+ in a row)")
repeated_fails = pd.read_sql_query(
    """
    SELECT user_id, COUNT(*) AS failed_attempts
    FROM fake_logins
    WHERE success = 'false'
    GROUP BY user_id
    HAVING COUNT(*) >= 5
    ORDER BY failed_attempts DESC
    """,
    conn
)
st.write(f"Found {len(repeated_fails)} users with 5+ failed logins.")
st.dataframe(repeated_fails)

# --- Flag 3: Odd-Hour Logins ---
st.header("3. Odd-Hour Logins (before 6am or after 9pm)")
odd_hours = pd.read_sql_query(
    """
    SELECT user_id, department, timestamp, auth_type
    FROM fake_logins
    WHERE CAST(strftime('%H', timestamp) AS INTEGER) < 6
       OR CAST(strftime('%H', timestamp) AS INTEGER) > 21
    ORDER BY timestamp
    """,
    conn
)
st.write(f"Found {len(odd_hours)} odd-hour logins.")
st.dataframe(odd_hours)

# --- Auth Type Breakdown Chart ---
st.header("Auth Type Breakdown")
auth_breakdown = pd.read_sql_query(
    "SELECT auth_type, COUNT(*) AS count FROM fake_logins GROUP BY auth_type",
    conn
)
st.bar_chart(auth_breakdown.set_index("auth_type"))

conn.close()