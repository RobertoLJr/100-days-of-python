# Day 51 Project: Automated Internet Speed Recorder

## Concept

Disclaimer: This is an alternative project than that suggested by the original course.

This program works with web scraping to perform an internet speed test. Then, it opens a csv file in the `data` directory to append the
current datetime in `dd/mm/YYYY HH:MM:SS` format, and the download and upload speeds. If the file does not exist,
the program creates one, writes the header and appends the first record.

## Usage

Before executing the program, make sure that the internet speed test is capable of achieving results before **45 seconds**,
which is the default timeout for the web scraping to get the required web elements. If you find the test needs more
time to conclude, provide a timeout (in seconds) as an argument when the `InternetSpeedBot` object is created in `main.py`.
Otherwise, the program will consider a timeout of 45 seconds.

## Resouces

### Libraries and Modules

- [datetime - Time access and conversions](https://docs.python.org/3/library/time.html#module-time)
- [csv - CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)
- [The Selenium Browser Automation Project](https://www.selenium.dev/documentation/)

### Miscellanea

- [SPEEDTEST](https://www.speedtest.net/)