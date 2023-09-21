# Day 5 Project: Password Generator

## Concept

The Password Generator is a simple program that takes three numeric inputs from the user to generate
a random password with a total number of characters that are the sum of those inputs. The first input
refers to the number of alphabetic characters in the password while the second and the third refer to
the number of symbols and numeric characters, respectively.

With the input provided, the program consults three built-in lists corresponding to those three categories
(letters, symbols and numbers) and randomly picks the informed number of elements from each list,
concatenating them into two Strings - the first corresponds to a randomly generated password ordered as
letters-symbols-numbers. The second provides a shuffled password, where each character can appear anywhere 
in the String.


## Resources

### Classes
- [Python Lists](https://docs.python.org/3/library/stdtypes.html?highlight=list#list)

### Control Flow Structures
- [for Statement (and more)](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

### Modules
- [random](https://docs.python.org/3/library/random.html?highlight=random#module-random)

### Functions
- [input()](https://docs.python.org/3/library/functions.html?highlight=print#input)
- [print()](https://docs.python.org/3/library/functions.html?highlight=print#print)
- [random.choice(seq)](https://docs.python.org/3/library/random.html?highlight=choice#random.choice)
- [random.shuffle(x)](https://docs.python.org/3/library/random.html?highlight=choice#random.shuffle)
- [str.join(iterable)](https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join)
