# Day 48 Project: Automated Game PLaying Bot

## Concept

This program functions as a bot to automatically play the [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) game under certain limitations.
As of the current implementation, by executing the program, the game is opened in Chrome web browser. Then, the program selects the English
language to play and start clicking on the cookie to gain points. Every 5 seconds, it checks the product list and buys the most expensive
product available. After 5 minutes, the program closes the browser and prints in the console the amount of cookies per second achieved.

## Resources

### Libraries and Modules

- [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)
- [time - Time access and conversions](https://docs.python.org/3/library/time.html#module-time)

### Miscellanea

- [Cookie Clicker Game](https://orteil.dashnet.org/cookieclicker/)
- [Cookie Clicker Game (classic)](https://orteil.dashnet.org/experiments/cookie/)