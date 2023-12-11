# Day 32 Project: Automated Birthday Wisher

## Concept

This program loads a CSV file containing people's data in the format `name,email,year,month,day`. It then
compares the current date in the format `day/month` with the day and month for each register in the file.
If the data match, the program randomly picks one of the three original email templates and replaces
the proper placeholders for the person's name and for the sender's signature. Finally, it sends an email
to the person's email, wishing them a happy birthday.

This implementation will be reviewed in the future for a more concise code. It could, for example, make use
of dictionary comprehension, and manage sensitive information as environment variables or via GUI.

## Resources

### Modules and libraries

- [pandas](https://pandas.pydata.org/docs/)
- [random](https://docs.python.org/3/library/random.html)
- [smtplib](https://docs.python.org/3/library/smtplib.html)

### Miscellanea

This code (and others)
can be configured to execute every day at a certain time by using https://www.pythonanywhere.com/!