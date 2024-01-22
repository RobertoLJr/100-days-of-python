# Day 15 Project: Coffee Machine

## Concept

This program is a very common simulation of a simple coffee machine. The program should fulfill the following
requirements:

1. Prompt user by asking "What would you like (espresso/latte/cappuccino)?"
   1. Check the user's input to decide what to do next;
   2. The prompt should show every time action has completed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering "off" to the prompt.
3. Print report.
   1. Shows the current resource values for water, milk, coffee, and money.
4. Check resources sufficient?
   1. When the user chooses a drink, the program should check if there are enough resources to make that drink;
   2. If not, the program should not continue to make the drink.
5. Process coins.
   1. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert
coins (quarters = $ 0.25, dimes = $ 0.10, nickles = $ 0.05, pennies = $ 0.01).
6. Check transaction successful?
   1. Check that the user has inserted enough money to purchase the drink they selected.
   2. If the user has inserted enough money, then the cost of the drink gets added to the machine as the
   3. profit and this will be reflected the next time "report" is triggered.
   4. If the user has inserted too much money, the machine should offer change.
7. Make Coffee
   1. If the transaction is successful and there are enough resources to make the drink the user selected,
then the ingredients to make the drink should be deducted from the coffee machine resources.
   2. Once all resources have been deducted, tell the user "Here is your `drink`. Enjoy!".

## Resources

### IDE-specific

- [PyCharm keyboard shortcuts](https://www.jetbrains.com/help/pycharm/mastering-keyboard-shortcuts.html)
- [PyCharm TODO comments](https://www.jetbrains.com/help/pycharm/using-todo.html)