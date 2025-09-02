# HW2: Scopes, Closures, LEGB

This folder contains ten Python tasks that demonstrate:
- the LEGB principle (Local, Enclosing, Global, Built-in)
- namespace handling
- use of global and nonlocal
- closures
- a first introduction to decorators (via memoization)

All scripts include docstrings, type annotations, and follow PEP 8 style.

---

## Files

1. HW2_1_builtins.py — Built-in scope & shadowing
   - my_sum() shadows the built-in sum.
   - Shows how to still access the original via import builtins.
   - What I added: shadowing demo + answers to review questions.

2. HW2_2_subscribers.py — Newsletter subscription manager
   - Global list subscribers.
   - subscribe(name) with nested confirm_subscription().
   - unsubscribe(name) removes or shows “not found”.
   - What I added: global + nested closure + validation.

3. HW2_3_discounts.py — Store orders with discounts
   - Global discount = 0.10.
   - create_order(price) applies global discount + VIP discount via nonlocal.
   - What I added: LEGB demo; validation for non-negative price.

4. HW2_4_training_timer.py — Training session timer
   - Global default_time = 60.
   - training_session(rounds) with nested adjust_time() using nonlocal.
   - What I added: LEGB comments; rounds validation.

5. HW2_5_calendar.py — Event calendar (closure + global)
   - Returns add_event, remove_event, view_events.
   - Events stored in a global list as required.
   - What I added: simple event handling; Ukrainian messages.

6. HW2_6_calculator_closure.py — Calculator with closures
   - create_calculator(operator) returns a function for +, -, *, /.
   - What I added: if/elif version; zero-division check.

7. HW2_7_expense_tracker.py — Expense tracker
   - Global total_expense.
   - add_expense(amount) uses global; get_expense() returns sum.
   - Console interface for adding/viewing expenses.
   - What I added: global demo + input validation.

8. HW2_8_user_settings.py — User settings
   - create_user_settings() returns set_setting, get_setting, view_settings.
   - Settings in enclosing scope; set_setting uses nonlocal.
   - What I added: defaults (theme, language, notifications); LEGB docstrings.

9. HW2_9_memoize.py — Caching via closures
   - memoize(func) returns a caching wrapper.
   - Used for either Fibonacci or factorial.
   - What I added: minimal version; demo with cache hits.

10. HW2_10_product_closure.py — Product management
    - create_product(name, price, quantity) returns (update_price, view_product).
    - update_price uses nonlocal to rebind enclosing price.
    - What I added: concise closure + nonlocal example.

---

## Usage

Each file is self-contained. Run them directly.