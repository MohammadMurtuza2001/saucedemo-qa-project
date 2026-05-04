# Test Summary Report — SauceDemo Manual Testing

**Project:** SauceDemo E-Commerce Manual Testing  
**Tester:** Mohammad Murtuza Moin  
**Test Period:** 3-May-2026 to 4-May-2026  
**Environment:** Microsoft Edge 147.0.3912.86 on Windows 10 Pro  
**URL:** https://www.saucedemo.com

---

## 1. Test Execution Summary

| Module | Total TCs | Passed | Failed | Blocked |
| :--- | :---: | :---: | :---: | :---: |
| Login | 6 | 6 | 0 | 0 |
| Product Listing Page | 8 | 5 | 3 | 0 |
| Add to Cart | 5 | 5 | 0 | 0 |
| Checkout Flow | 8 | 6 | 2 | 0 |
| Navigation / UI | 3 | 3 | 0 | 0 |
| **Total** | **30** | **25** | **5** | **0** |

---

## 2. Pass Rate
Overall pass rate achieved was 83.3% across 30 executed test cases.

---

## 3. Defects Summary

| Bug ID | Title | Severity | Priority | Status |
| :--- | :--- | :--- | :--- | :--- |
| BUG-001 | Wrong Product Images for problem_user | High | P1 | Open |
| BUG-002 | Add to Cart button broken on product detail page for problem_user | High | P1 | Open |
| BUG-003 | Sort filter broken for problem_user | Low | P3 | Open |
| BUG-004 | Last Name field broken in the checkout page for problem_user | High | P1 | Open |
| BUG-005 | Checkout cannot be completed due to field overwriting bug for problem_user | Critical | P1 | Open |

---

## 4. Key Findings
* The core purchase flow works correctly and completely for standard_user — all 25 test cases passed with no defects found.
* problem_user experiences critical defects across product listing, cart, and checkout modules, with the checkout flow being entirely non-functional for this user type.
* Four out of five bugs identified are rated High or Critical severity, indicating significant quality issues for the problem_user account.
* BUG-005 represents a complete blocker for problem_user — the checkout form cannot be submitted due to the field overwriting bug documented in BUG-004, making purchase completion impossible.

---

## 5. Risks and Observations
During exploratory testing, the password field visibility toggle on the login page appeared inconsistently present during some sessions and absent during others. This behavior could not be reliably reproduced and was therefore not formally documented as a bug report. It is flagged here as an observation for further investigation.

---

## 6. Test Recommendation
- [x] **CONDITIONAL PASS** – Release with known defects documented

**Justification:**
The application functions correctly and completely for standard_user with an 83.3% overall pass rate. However, problem_user experiences multiple critical defects including wrong product images (BUG-001), a non-functional Add to Cart button (BUG-002), a broken sort filter (BUG-003), and a checkout-blocking field overwriting bug (BUG-004, BUG-005). These defects must be resolved before problem_user can be considered a viable account type for release.
