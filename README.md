# Optical reading Chappe telegraph
#### Principle
- There is a Chappe telegraph powered by 3 servos motors and an Arduino card (Check the Arduino part on this project: https://github.com/Ilard/telegraphechappe_arduino).
- A camera read the telegraph symbols with a PC.
- The telegraph symbol is compared with a symbol's catalog.
- Each symbol corresponds to a numeric code.
- This corresponding code is send in JSON format to a web server and displayed on a web page (Check web development in this project: https://github.com/Ilard/telegraphechappe_web).

#### Technical platform
- PC with GNU Linux Debian 10.0 Testing.
- Webcam.
- Python 3.7.4.
- OpenCV library for optical reading.
- Requests library to send JSON data to a web server.

#### Simple schematic

```sh
   Chappe             Web camera          Web server       Display
  telegraph           with a PC           with JSON        symbol
   symbol             Python app          connection       & code

        \               _____               ______               \
  +--|--+     =[]      | PC  |             |      |        +--|--+
  |  |          |______|_____|--network-->-|server|--->--- |  |
     |                 /_____/             |______|           |
  Arduino    Webcam  optical work        Web animation     Web Page
```
