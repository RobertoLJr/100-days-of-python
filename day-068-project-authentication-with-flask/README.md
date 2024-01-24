# Day 68 Project: Authentication with Flask

## Concept

This project uses a four-page website to work with routing, authentication, and password hashing. The index page
provides buttons for Login and Register, as well as the navigation bar. Once successfully logged in or upon registration,
the user is directed to the Secrets page in which they can download a Flask Cheat Sheet file.

If the user tries to log in with a non-existing email in the database, a flash message will inform them of that.

If the user tries to log in with an incorrect password, another flash message will inform them of that.

If the user tries to register with an already existing email in the database, they will be redirected to the login
page with a flash message informing that email was already used to sign in.

The passwords registered in the database are encoded via Werkzeug with the `pbkdf2:sha256` method and a `salt_length` of 8.

## Resources

### Engines/Frameworks/Modules

- [Flask Quickstart Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [FlaskWTF](https://flask-wtf.readthedocs.io/en/1.0.x/) - Integration of Flask and WTForms.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)

### Miscellanea

- [Creating or using requirements.txt](https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub)
- [DB Browser for SQLite](https://sqlitebrowser.org/) - Useful for visualizing databases' structures and data.

### Fun stuff

- [cryptii](https://cryptii.com/) - Web app offering modular conversion, encoding and encryption online.
- [Have I Been Pwned](https://haveibeenpwned.com/Passwords) - Website allowing for searching across multiple data breaches to see if your email addresses have been compromised.
- [Password Complexity Checker](http://password-checker.online-domain-tools.com/)
- [Plain Text Offenders](https://plaintextoffenders.com/) - Examples of unsafe services that store passwords as plain text.
- [Wikipedia: List of the most common password](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords)