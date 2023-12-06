# Day 28 Project: Pomodoro App

## Concept

The [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) is a well known time management method
developed by Francesco Cirillo in the 1980s. It might be a useful resources for studies, general productivity
or as a kitchen timer.

This program simulates such a technique in the following way:

1. the `Start` button initializes a **Work** session. Each Work session lasts for 25 minutes.
2. After each Work session, a **Break** session begins, lasting for 5 minutes.
3. After four Work sessions, the next Break session is replaced by a longer **Break** session that lasts for 20 minutes.
4. The loop starts again, repeating this process until the program is closed.

The change between each session is marked by a ring bell that should work fine on Windows. The program was not tested
within other environments.

The `Reset` button resets the Timer and the repetition. Once pressed, the user should press the `Start` button
again to restart the application.

## Resources

- [Color Hunt](https://colorhunt.co/) for quick palette references.

### Packages and modules

- [math](https://docs.python.org/3/library/math.html)
- [tkinter package](https://docs.python.org/3/library/tkinter.html)
- [winsound module](https://docs.python.org/3/library/winsound.html)