# Day 68 Project: Fully-fledged Blog Website

## Concept

This program works with Flask to provide a fully-fledged website application that allows users to create, edit or delete
posts as well as leaving comments. As of the current implementation, only the admin (namely, the user with id = 1 in
the Users table from the database) can create, edit or delete posts. All other users should be able to register, log in,
and leave comments.

This project comes with two users, one post, and one comment in the relational database, to function as examples.

Originally, this program should use [Gravatar](https://gravatar.com/) in the comments section, but due to incompatibility with Flask 3.0.0
a workaround was necessary, as provided in the code with an appropriate comment.

## Resources

### Engines/Frameworks/Modules

- [CKEditor](https://flask-ckeditor.readthedocs.io/en/latest/) - Integration of CKEditor for Flask.
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - Provides user session management for Flask.
- [FlaskWTF](https://flask-wtf.readthedocs.io/en/1.0.x/) - Integration of Flask and WTForms.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
  - [SQLAlchemy Basic Relationship Patterns](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/3.0.x/) - Used in this project to handle password hashing.
- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)

### Miscellanea

- [Creating or using requirements.txt](https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub)
- [DB Browser for SQLite](https://sqlitebrowser.org/) - Useful for visualizing databases' structures and data.