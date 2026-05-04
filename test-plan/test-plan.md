# Test Plan  
## SauceDemo E-Commerce Manual Testing

---

## 1. Project Overview
SauceDemo is a demo e-commerce web application created by Sauce Labs for the purpose of software testing practice. It simulates a real online store where users can browse products, add items to a cart, and complete a checkout flow. The application is publicly accessible and is used by QA engineers and students to practice manual and automated testing techniques.

---

## 2. Scope of Testing

### In Scope (what we WILL test):
- Login / authentication  
- Invalid credential error handling  
- Password visibility toggle  
- Product listing page  
- Sort / filter (4 options)  
- Add to cart  
- Remove from cart (on listing page)  
- Cart badge counter  
- Cart page (with Continue Shopping + Checkout)  
- Checkout — Information form with validation  
- Checkout — Order review/confirmation page  
- Order completion confirmation  
- Burger menu (All Items, About, Logout, Reset App State)  
- Responsiveness  

### Out of Scope (what we will NOT test):
- Amount of traffic the website can handle (load)  
- Payment method and its security  
- Website’s vulnerability  
- Formal Performance Testing (JMeter)  

---

## 3. Test Objectives
- Verify that a standard user can successfully log in, browse products, add items to cart, and complete a checkout from start to finish.  
- Confirm that all form fields reject invalid or empty inputs with appropriate error messages.  
- Ensure that UI elements including product images, text, and navigation links display correctly and are functional.  
- Identify and document any defects that block or degrade the core purchase flow.  

---

## 4. Test Types to be Performed
- **Functional Testing:** Making sure the flow of the website is stable.  
- **UI Testing:** Making sure the web elements, icons, texts are not cluttered or messy.  
- **Negative Testing:** Making sure the features like cart don’t behave abnormally.  
- **Boundary Testing:** Making sure input fields handle edge cases such as empty fields or unexpected characters.  

---

## 5. Test Environment
- **Browser:** Microsoft Edge Version 147.0.3912.86 (64-bit)  
- **OS:** Windows 10 Pro (22H2)  
- **URL:** https://www.saucedemo.com  
- **Test Data:** The login credentials (`standard_user` and `problem_user`) will be used.  

---

## 6. Entry Criteria
Stable internet connection and the site https://www.saucedemo.com should be up and running. We should be able to log in with the credentials `standard_user` and `problem_user`.

---

## 7. Exit Criteria
Testing is considered complete when:  
1. All test cases listed in the test plan have been executed  
2. All identified defects have been logged with full bug reports  
3. A test summary report has been produced  

If a critical defect blocks further testing, the affected area will be flagged as **Blocked** and documented accordingly.

---

## 8. Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Site goes offline | Low | High | Contact the Project Manager and wait for further notice |
| Hardware Issues | Low | High | Contact the IT team ASAP to get the hardware fixed |
| Internet connection lost | Low | Medium | Contact the IT team to restore network |
| Credentials won’t work | Medium | Low | Switch to other credentials |
| Incorrect assumptions in test cases | Low | Medium | Re-explore the app before writing expected results |

---

## 9. Deliverables
- Test Plan (this document)  
- Test Cases (30 test cases in a structured table)  
- Bug Reports (minimum 5)  
- Test Summary Report  

---

## 10. Schedule (Estimated)

| Phase | Estimated Time |
|------|--------------|
| Exploration | 1 hour |
| Test Plan | 30 mins |
| Test Case | 2–3 hours |
| Test Report | 1 hour |
