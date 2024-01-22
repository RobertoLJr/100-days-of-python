# Day 49 Project: Automated Job-Saving Bot

## Concept

This program automates the process of saving jobs from the LinkedIn first page jobs. However, it has many constrictions
that should be revised in the future.

As of the current implementation, the program works with a fixed URL that searches for "internship/entry-level remote
positions for a Data Engineer in the United Kingdom." With a few tweaks, it could also apply automatically for the
jobs.

## Requirements

- LinkedIn account.

## Usage

1. Go to the Jobs tab in LinkedIn and select the constrictions for the job search, then copy the URL into the code.
2. Provide your LinkedIn username and password as environment variables.
3. Verify if all the jobs from the first page were saved in your profile.

## Resources

### Libraries and Modules

- [os - Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)
- [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)
- [time - Time access and conversions](https://docs.python.org/3/library/time.html#module-time)

### Miscellanea

- [LinkedIn](https://www.linkedin.com)