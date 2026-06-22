# SauceDemo QA Project — Manual + Automation


## What is this?
A full-cycle QA project for [SauceDemo](https://www.saucedemo.com), a demo e-commerce application. The project covers manual testing across all major user flows, followed by Selenium-based automation for the Login module to establish a repeatable regression suite.

---

## Project Phases

- [x] Phase 1 — Exploratory Testing ✅
- [x] Phase 2 — Test Plan ✅ ([View Test Plan](./test-plan/test-plan.md))
- [x] Phase 3 — Test Cases ✅ ([View Spreadsheet](https://docs.google.com/spreadsheets/d/1nSEImQ-M-B-03WE1A-eFEcV1ocAFtBWc-P5DZ3tne7M/edit?usp=sharing))
- [x] Phase 4 — Test Execution ✅
- [x] Phase 5 — Bug Reports ✅ ([View Reports](./bug-reports/))
- [x] Phase 6 — Test Summary Report ✅ ([View Report](./test-summary-report/test-summary-report.md))
- [x] Phase 7 — Login Automation (Selenium + Python + Pytest) ✅ ([View Automation](./automation/))

---

## Project Deliverables

- **Test Case Spreadsheet:** Detailed test cases covering Login, PLP, Cart, and Checkout modules.
- **Bug Reports:** 5 documented defects (3 High, 1 Critical, 1 Low) found using the `problem_user` account.
- **Summary Report:** Final assessment of the application's readiness for release.
- **Automation Suite:** 8 automated login tests using Selenium + Pytest, with an HTML report output.

---

## Manual Testing — Key Findings

- 25/30 test cases passed — **83.3% pass rate**
- `standard_user`: all 25 test cases passed with zero defects
- `problem_user`: 5 critical/high severity bugs found, including a checkout-blocking field overwriting bug (BUG-004, BUG-005)
- Application rated: **CONDITIONAL PASS**

---

## Login Automation — Selenium + Python + Pytest

### Why Automation Was Added
Manual testing provided deep product insight and helped identify critical user flows. Automation was then layered on top to create a repeatable regression suite that can be triggered whenever the login page changes.

### What is Automated

| Test | Description |
| :--- | :--- |
| TC-01 | Valid login: `standard_user` with correct password lands on inventory page |
| TC-02 | Locked account: `locked_out_user` receives appropriate error message |
| TC-03 | Wrong password: displays error on entering wrong password |
| TC-04 | Empty username: displays error on empty username field |
| TC-05 | Empty password: displays error on empty password field |
| TC-06 | Both fields empty: displays error on both empty fields |
| TC-07 | Correct error message: full message displays with no spelling mistakes |
| TC-08 | URL contains `inventory`: visible in URL after successful login |

### Tech Stack

| Tool | Purpose |
| :--- | :--- |
| Selenium | Automates browser actions (clicking, typing, navigation) |
| pytest | Writes, organizes, and runs test scripts |
| pytest-html | Generates an HTML test report |
| webdriver-manager | Auto-downloads the required browser driver |

### How to Set Up and Run

```bash
# Step 1: Clone the repo
git clone <repo-url>

# Step 2: Open the project in VS Code and navigate to the automation folder
cd automation

# Step 3: Activate the virtual environment
venv/Scripts/activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Run the tests
pytest
```

Once complete, open `automation-report.html` in your browser to view the full HTML report.

### Automation Test Results

| Test | Description | Result |
| :--- | :--- | :--- |
| TC-01 | Valid credentials reach products page | ✅ Passed |
| TC-02 | `locked_out_user` shows error message | ✅ Passed |
| TC-03 | Wrong password shows error | ✅ Passed |
| TC-04 | Empty username shows error | ✅ Passed |
| TC-05 | Empty password shows error | ✅ Passed |
| TC-06 | Both fields empty shows error | ✅ Passed |
| TC-07 | Error message text is correct | ✅ Passed |
| TC-08 | URL contains `inventory` after valid login | ✅ Passed |

---

## Tools Used

- **Browser:** Microsoft Edge 147
- **OS:** Windows 10 Pro
- **Test Case Management:** Google Sheets
- **Documentation:** Microsoft Word, Markdown
- **Screenshot Capture:** Greenshot
- **Automation:** Selenium, Pytest, Python
- **Version Control:** Git & GitHub

---

## Author

**Mohammad Murtuza Moin**
