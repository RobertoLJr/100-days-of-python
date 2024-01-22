# Day 63 Project: Virtual Bookshelf

## Concept

This program introduces the usage of SQLite databases and CRUD operations within a Flask application via the SQLAlchemy toolkit for SQL. It functions
by first creating a connection to a _library_ database. Then, if it is run for the first time, it should produce a simple
HTML page informing the user that the Library is empty, but allowing for them to add a book. Each entry comprises the
book's title, author, and a rating. Whenever a new entry is added, the application adds that book's data to the _library_
database and redirects the user to the home page, displaying all the books' data from the database.

The link for _Edit Rating_ brings the user to a form page in which they can update the rating in the database.

The link for _Delete_ removes that entry from the database.

## Resources

### Engines/Frameworks/Modules

- [Bootstrap Flask](https://bootstrap-flask.readthedocs.io/en/stable/) - Jinja macros for Bootstrap and Flask - Renders Flask-related data/objects to Bootstrap markup HTML more easily.
- [Flask Quickstart Documentation](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

### Miscellanea

- [Creating or using requirements.txt](https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub)
- [DB Browser for SQLite](https://sqlitebrowser.org/) - Useful for visualizing databases' structures and data.