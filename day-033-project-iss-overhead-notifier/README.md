# Day 33 Project: ISS Overhead Notifier

## Concept

This program works with two different APIs to identify via functions if the ISS is overhead a current location, 
and if it is nighttime in the said location (that way, it would be possible to see it). As of now, the user
would be required to hardcode some information for this code to work properly. Those would be:

- The exact coordinates for the user's location (you can search for those [here](https://www.latlong.net/)).
- The email, password and host domain for the SMTP.

This program could be uploaded to a Cloud platform to be executed automatically, otherwise it would be
required to keep it running at all times.

As a result of its execution, whenever the ISS is overhead, and it is nighttime, a notification will be sent to
the provided email reminding the user to look up and try to see it!

## Resources

### APIs

- [International Space Station Current Location API](https://open-notify.org/Open-Notify-API/ISS-Location-Now/)
- [Sunset and Sunrise Times API](https://sunrise-sunset.org/api)

### Modules and libraries

- [datetime](https://docs.python.org/3/library/datetime.html)
- [requests](https://docs.python-requests.org/en/latest/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [time](https://docs.python.org/3/library/time.html)

### Miscellanea

- [HTTP Status Codes Glossary](https://www.webfx.com/web-development/glossary/http-status-codes/)