# Day 37 Project: Habit Tracker

## Concept

This program uses the Pixela API to create a graph that can be used as a habit tracker. As of the current implementation,
the program works via functions that can be called one at a time. For usage, the user should provide as constants
a desired username, a custom token to be created (see the restrictions in Pixela API document in the resources), and
a name for the desired graph. In summary, the user can uncomment one of the four functions at the end of the code
to use the API. The functions and their usage are:

`create_account()`: make a new account in pixela with the data in constants passed as arguments.

`create_graph()`: make a new graph using your username and the name of the graph in constants passed as data.

`post_pixel(quantity: str)`: post a new pixel for today's date passing the quantity as string as argument.

`update_pixel(quantity: str)`: update the pixel for yesterday's date passing the quantity as string as argument.

`delete_pixel()`: delete the pixel for today's date.

## Resources

### APIs

- [pixela API documentation](https://docs.pixe.la/)

### Modules and libraries

- [requests](https://requests.readthedocs.io/en/latest/)

### Miscellanea

- [pixela Website](https://pixe.la/)