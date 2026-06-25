# SauceDemo POM Framework

This project is structured using Page Object Model which separates page interactions from test logic into two folders, namely pages and tests.

The pages folder contains six page classes, login, inventory, cart, info, overview and complete. Each class holds locators and actions for that page.

The tests folder contains two test files, checkout flow and invalid login, which contains actual test cases.

There is also another file called conftest file in the tests folder, which handles browser setup and teardown.

**test_complete_checkout**: This tests login, add to cart, go through checkout and verifies order confirmation message.
**test_negative**: This verifies correct error message is displayed when invalid credentials are entered.

# How to Run

python3 -m pytest tests/ -v