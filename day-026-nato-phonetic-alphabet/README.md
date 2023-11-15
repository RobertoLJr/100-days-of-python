# Day 26 NATO Phonetic Alphabet

## Concept

When you are spelling out a name, location, code, registration number, zip code etc., over a noisy or faint radio or
phone link, it is easy for letters and numbers to be misheard. The [NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)
is a set of clear code words for communicating the letters of the Roman alphabet when spelling a word.

This program produces a list of NATO phonetic codes for any String taken as input from the user, first. To do so,
it uses the Pandas module to create a DataFrame and create a dictionary with the `key, value` pair as `letter, code`.
This step is performed under concepts of List Comprehension, as well as the next one.

Finally, it produces as output a list of codes for each character in the given string.

## Resources

### Python Data Structures

- [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

### Modules

#### Pandas

- [Pandas API Reference](https://pandas.pydata.org/docs/reference/index.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- 