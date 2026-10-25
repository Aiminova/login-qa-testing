# Login QA Test Project

![CI](https://github.com/Aiminova/login-qa-testing/actions/workflows/ci.yml/badge.svg)

A focused QA study of a **login (authentication) module**. I used it to practice the whole testing cycle on one feature: test planning, test case design, automation, security checks and bug reporting.

## What I Covered
| Category | Examples | Automated tests |
|---|---|---|
| Functional | Valid login, login with Enter key | 2 |
| Negative | Wrong/empty/case-changed/whitespace inputs | 8 |
| Boundary | 1000-character input | 1 |
| Security | SQL injection (3 payloads), XSS, password masking, unauthorized access | 6 |
| Session | Logout and access to a protected page after logout | 1 |

## Tech Stack
Python 3.12 · pytest · Playwright · pytest-html · GitHub Actions

## Setup and Run
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

pytest                    # all tests
pytest -m smoke           # critical fast tests
pytest -m security        # security tests
pytest --headed           # run with a visible browser
```
Report: `reports/report.html`

## Project Structure
```
├── pages/login_page.py     # Page Object Model
├── tests/test_login.py     # Automated tests
├── docs/
│   ├── test_plan.md        # Test plan
│   ├── test_cases.md       # 17 test cases + manual checklist
│   └── bug_report_examples.md
├── conftest.py             # Shared settings
└── .github/workflows/ci.yml
```

## Design Decisions
- **Parametrized tests:** one test function covers many data combinations.
- **Page Object Model:** locators live in one place, so UI changes are cheap to maintain.
- **Security mindset:** I included basic OWASP-style checks (injection, XSS, session handling).
- **Traceability:** each automated test maps to a test case ID in `docs/test_cases.md`.

## Application Under Test
[the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login) (a public demo built for test practice)

---
Author: [Aiminova](https://github.com/Aiminova)
