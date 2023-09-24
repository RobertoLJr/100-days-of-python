# Day 8 Project: Caesar Cipher

## Concept

The [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is one of the simplest and most widely
known encryption techniques. By today's standard, this technique is very rudimentary and not safe at all.
It works by taking a message as input and replacing each character by another character according to
a numeric key provided (e.g. the letter 'a' in the key of '2' becomes 'c' while in the key of '-1' becomes 'z').

As it is written, this program takes four inputs from the user as follows to perform these operations:

1. The cipher operation ("encode" or "decode");
2. The message to encode/decode;
3. The shift number (or key) to apply to the message;
4. The choice for either repeating this process or ending the program.

Once the first three inputs are provided, the program outputs a *string* with each alphabetic character
rotated in the key provided, which can be a positive or negative integer. Numeric values and symbols are
printed as they are in the original message.

Finally, the program asks the user if he/she wants to restart by providing the first three inputs again
until the user types "no" for the last question.

## Resources

### Functions and Methods

- [Python 3 Documentation - More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [array.array.index()](https://docs.python.org/3/library/array.html?highlight=index#array.array.index)