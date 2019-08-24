# Optical reading Chappe telegraph
#### Principle
- There is a Chappe telegraph powered by 3 servos motors and an Arduino card. (Check the Arduino part on this project).
- A camera read the telegraph symbols with a PC.
- The telegraph symobol is compared with a symbol's catalog.
- Eatch symbol corresponds to a code.
- The corresponding code is send in JSON format to a web server and displayed on a web page.

#### Technical plateform
- PC with GNU Linux Debian 10.0
- Webcam
- Python 3.7.4
- OpenCV library for optical reading
- Requests library to send JSON data to a web server
