# Day 52 Project: D&D Random Wondrous Item Finder

## Concept

Disclaimer: This is an alternative project than that suggested by the original course.

This program works with web scraping using Selenium to access the lists of wondrous items from the [community wiki
DND 5th Edition](http://dnd5e.wikidot.com/). It gets hold of all the wondrous items from the wiki, shuffles them
and produces a random item according to the user's choice of a number between zero and the maximum number of items.

## Usage

Run the program and wait for the console to ask for a number between zero and an upper limit. Type in a number and
press Enter, then wait to see the results in the console, which will be printed like so:

```
NAME   : Alchemy Jug (Blue)
SOURCE : Source: Candlekeep Mysteries
SNIPPET: Wondrous item, uncommon
            
(This jug functions as an Alchemy Jug, except that it neither produces acid or poison. It can produce 1 quart of boiling hot tea instead.)

This ceramic jug appears to be able to hold a gallon of liquid and weighs 12 pounds whether full or empty. Sloshing sounds can be heard from within the jug when it is shaken, even if the jug is empty.

You can use an action and name one liquid from the table below to cause the jug to produce the chosen liquid. Afterward, you can uncork the jug as an action and pour that liquid out, up to 2 gallons per minute. The maximum amount of liquid the jug can produce depends on the liquid you named.

Once the jug starts producing a liquid, it can't produce a different one, or more of one that has reached its maximum, until the next dawn.
            
MORE INFO: http://dnd5e.wikidot.com/wondrous-items:alchemy-jug-blue
```

Press any key on the console to close the browser and end the program.

## Resources

### Libraries and Modules

- [random — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
- [re - Regular expression operations](https://docs.python.org/3/library/re.html)
- [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)
- [time - Time access and conversions](https://docs.python.org/3/library/time.html#module-time)
