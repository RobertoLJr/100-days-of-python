# Day 60 Project: POST-Request Contact Form

## Concept

### Disclaimers
- As of the current implementation, the form owner should have a Gmail account (will be revised in the future);
- Unfortunately, Google has disabled support for the _less secure apps_ functionality (Fall of 2024), which the smtplib library used. The Submit button will now incur in an error. An alternative will be evaluated in the future.

This program is an improvement to the [Day 59 Project: Bootstrap Blog](../day-059-project-bootstrap-blog) as it adds the form functionality to the Contact page.
Upon filling and submitting the form, an email is sent from and to the email account set as `OWN_EMAIL` and its password `OWN_PASSWORD` with environment variables, containing the
name, the email, the phone number, and the message from the person who filled and submitted the form.

## Resources

### Engines/Frameworks

- [Bootstrap](https://getbootstrap.com/)
- [Flask Quickstart Documentation](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

### Miscellanea

- [n:point](https://www.npoint.io/) - Online and free schema editor and JSON endpoint generator to simulate API calls.
- [Pexels](https://www.pexels.com/)
