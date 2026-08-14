
# Login Anomaly Detector

🔗 **Live dashboard:** https://security-risk-dashboard.streamlit.app/
📂 **Repository:** github.com/Cameronpza/login-anomaly-detector

A tool that analyzes login activity and flags suspicious patterns — inspired by the kind of login/auth security analytics real security and data teams use, particularly on cloud platforms like Snowflake.

\---

## What it does

This project analyzes a dataset of internal login attempts and flags four types of risk:

1. **Weak auth usage** — logins using basic username/password instead of SSO, key-based, or token-based authentication
2. **Repeated failed logins** — users with 5+ failed login attempts, which could indicate a locked-out account or someone attempting unauthorized access
3. **Odd-hour logins** — logins occurring outside normal working hours (before 6am or after 9pm)
4. **Unusual system access** — a breakdown of how often each user accesses each system, used to identify low-frequency, potentially unusual access patterns

Results are displayed in a live Streamlit dashboard, with flagged tables and a chart of authentication method usage.

\---

## Why this project — and how it evolved

I built this to demonstrate practical SQL and AI-assisted development skills for a junior data engineering role. The project went through two meaningful changes based on real feedback, which I think say more about my process than the final code does:

**Version 1 → Version 2: from public-internet attacks to internal auth analytics**
I originally framed this around public-internet brute-force login attempts. After talking it through with my mentor, I learned that logging into a company database from the public internet is essentially never how real access works — access almost always happens from within a company's own network. That conversation also surfaced a more accurate and more relevant angle: **authentication method itself** (basic username/password vs. SSO, key-based, or token-based auth) is a much bigger real-world risk factor, especially on cloud-hosted platforms like **Snowflake**, where data is exposed to the internet and strong auth methods matter far more than on older, internal-only systems. I rebuilt the project around this — internal login analytics, with weak-auth detection as a core flag — rather than the original (and less accurate) public-attack framing.

**Considered: a real Snowflake version**
I also looked at building this directly against a real Snowflake trial account, querying its built-in `LOGIN\_HISTORY` system view instead of using generated data — since that would reflect exactly how a real security/data team would approach this on Snowflake itself. I decided to keep this project on fake, locally-generated data in order to hit a tight deadline, but a real-Snowflake version is a natural next iteration of this project (see "What I'd do next" below).

\---

## Tech used

* **SQLite** — local data storage
* **SQL** — the four flag queries (`/sql`)
* **Python + Streamlit** — the dashboard (`app.py`)
* **\~750 fake login records** — generated with realistic suspicious patterns deliberately built in, so the flags have real signal to catch

\---

## How I used Claude

I used Claude as a coding assistant throughout the build — generating the fake dataset, writing and explaining each SQL query, and scaffolding the Streamlit dashboard. For every query, I made sure I could explain what it does and why in my own words before moving on to the next one; that process is documented alongside my working notes in this repo.

Claude was also useful for thinking through the project's real-world framing — the internal-vs-public-access reframe above came out of a conversation about what my mentor had actually explained, translated into a concrete change in the project's design rather than just cosmetic edits.

\---

## Project structure

=======

## What I'd do next

* Rebuild this against a **real Snowflake trial account**, querying `SNOWFLAKE.ACCOUNT\_USAGE.LOGIN\_HISTORY` instead of generated data
* Add automatic flagging for unusual system access (currently a manual-review query rather than an automated flag)
* Add a machine-learning-based anomaly score instead of fixed thresholds
* Add alerting instead of a static dashboard
* 

