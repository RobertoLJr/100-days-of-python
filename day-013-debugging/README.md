# Day 13 Study Session: Debugging

## Concept

This session does not involve a project _per se_, but instead focuses on techniques and tips to debug
flawed code. The projects will be resumed on Day 14.

We call *debugging* the process of removing "bugs" from one's code - or better yet, the process of finding
and correcting certain problems that might have been ingested by programming and deploying software.
A *bug*, then, can be defined as an error, a flaw or fault in the design, development, or operation of
computer software that causes it to produce an incorrect or unexpected result, or to behave in unintended
ways. More info can be found on [Wikipedia](https://en.wikipedia.org/wiki/Software_bug), including one
of the most prominent usage of the term by Grace Hopper.

## Tips and techniques for debugging

### 1. Describe the problem

---

If the problem itself is "messy" or not very well described, it becomes really hard to debug it. One
useful technique is to untangle the problem and try to make sense of what is actually going on.

An important thing to keep in mind is that **you need to get used to extracting useful information
from the errors on the console, when they are present**. You can use that information to search
on Google about that output or look into StackOverflow. [See the 10th technique below](#10-ask-stackoverflow).

### 2. Reproduce the bug

---

This tip actually revolves around asking the right questions in relation to the bug and its reproduction.
By going through the non-exhaustive list of questions below, it's possible to grasp a more thorough
understanding of the program's goal as well as of the program's actual behaviour:

1. What do you need the program to do?
2. What does it actually do?
3. What are the issues you've found?
4. Have you encountered these types of problems before? If so, what did you do to fix them?
5. Where and why do you think the bugs occurred?

### 3. Play computer and evaluate each line

---

This technique should encourage you to read your code line by line and **interpret exactly what it does
and what result it should produce according to its actual implementation** and not with your goal in mind.

### 4. Fix the errors

---

Although obvious, this statement refers to the errors pointed by the IDE being used. Some of those
might not be critical and overlooked, so it is a good practice to try and use the clues provided by
the environment before continuing with the program's development. These errors mostly include **syntax errors.**

### 5. Use _`print()`_ judiciously

---

The use of the _print()_ function can facilitate the detection of exactly when the program's output
starts to deviate from its intention. The overuse of this technique can turn into a difficult cleanup
afterward, so it's important to keep track of it. This technique mostly covers **logic errors**.

### 6. Use a Debugger

---

This tool is considerably more complex than the mere use of previous techniques, but it can provide
detailed insight into the code's execution. For analyzing very simple parts of code, the [Online
Python Tutor](https://pythontutor.com/) contains a unique step-by-step visual debugger. In general,
every IDE contains its own debugger tool. This technique is very useful for identifying
**semantic, logic or runtime errors.**

### 7. Take a break

---

Sometimes insights come at odd hours and more easily when you're not looking uninterruptedly
at the same code for hours. A small (or longer) break can leverage the mind to wander toward
less contrived environments and bring solutions that would hardly come by so smoothly.

### 8. Ask someone

---

Two interesting things happen when this technique is put to use: first, when you are trying
to explain the problem to someone else, you yourself might catch a mistake in the logic of its
solution's implementation rather than in the code itself. Secondly, the other person might have
already faced that problem or might develop an insight for it at the spot, specially if that
someone is a more experienced programmer, so really it could be a win-win situation.

### 9. Run the code often

---

Avoid running your code only after writing large parts of it. Try to break your program into
smaller implementations and milestones, so you can constantly check and debug without having
to fix too many problems at once that oftentimes intermingle and make each other worse.

### 10. Ask [StackOverflow](https://stackoverflow.com/)

---

This resource is extremely helpful when you know how to search right. The odds that another
programmer has faced the same problem you're facing are high, and someone might have helped
with a useful answer. If not, you can make a post asking for help trying to pass through it
the questions from [the 2nd technique](#2-reproduce-the-bug).
