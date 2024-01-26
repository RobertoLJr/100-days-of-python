# Day 72 Project: Data Exploration with Pandas

## Concept

This project is more of a compilation of notes from Pandas, although the `main.py` file actually performs some web
scraping to collect data into a Pandas DataFrame for practice. Upon execution, the program uses BeautifulSoup to
access [College Salary Report on payscale](https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors)
and collect data from the updated table, creating a Pandas DataFrame from it containing all the information.

The end of the file contains a few commented commands for data exploration.

Since this program works with pagination, there is room for improvement by implementing Selenium to directly interact
with the webpage. This application should perform better that way.

Included, there is a Jupyter Notebook that works with the file `salaries_by_college_major` in the data directory,
very similar to the web scraped data, although outdated. This file compiles a few other commands to work with DataFrames.

## Resources

- [BeautifulSoup documentation](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Pandas documentation](https://pandas.pydata.org/docs/index.html)