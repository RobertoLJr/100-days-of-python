# Day 62 Project: Coffee & Wi-Fi WebSite

## Concept

This program continues the web development section with Flask, Bootstrap, Jinja, and WTForms capabilities. It renders
a homepage that can redirect to another page containing a list of cafés - their respective names, Google Map links,
opening/closing time, and ratings for coffee quality, Wi-Fi Strength, and Power Outlet Availability.

There is a secret page accessed by adding `/add` to the end of the homepage URL that leads to a form. This form takes
as input the very same previously listed elements, so the user can add a new entry for a café. Immediately after validation
and submission, the page redirects the user to the café listing containing the new addition.

The `requirements.txt` file is up to the date 17/01/2024.

## Resources

### Engines/Frameworks/Modules

- [Bootstrap Flask](https://bootstrap-flask.readthedocs.io/en/stable/) - Jinja macros for Bootstrap and Flask - Renders Flask-related data/objects to Bootstrap markup HTML more easily.
- [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
- [FlaskWTF](https://flask-wtf.readthedocs.io/en/1.0.x/) - Integration of Flask and WTForms.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- [WTForms](https://wtforms.readthedocs.io/en/3.0.x/)

### Miscellanea

- [Creating or using requirements.txt](https://docs.google.com/document/d/e/2PACX-1vRIW_TuZ6z0ASjAoxgJgmzjGYLCDx019tKvphaTwK_Za7fnMKywUuXI0-s5wr0nQI_gprm6J6y7L9rL/pub)