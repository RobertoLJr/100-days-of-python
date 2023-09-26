# Day 9 Project: Secret Auction

## Concept

This program simulates a [blind auction](https://en.wikipedia.org/wiki/First-price_sealed-bid_auction).
It first asks the user for their name, then asks for a bid as a _float_. Then, the program asks if there are
more bidders to be added, continually asking the next bidder's name and bid if the answer is 'yes',
otherwise the program continues.

When there are no more bidders to be added, the program loops through a dictionary populated by the
previous inputs and returns the name of the auction's winner along with their bid, which should be the
higher value from all the previous bid inputs.

## Resources

### Data Structures

- [Python 3 Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Functions and Methods

- [os.system(_command_)](https://docs.python.org/3/library/os.html?highlight=module%20os#os.system)

### Modules

- [os - Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html?highlight=module%20os#module-os)