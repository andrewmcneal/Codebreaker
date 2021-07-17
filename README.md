# Codebreaker

This is my first venture into GUI based gameing. It is based on the game Mastermind. The player uses colored pegs to try to break a secret code implemeted by the computer. There are four positions to fill. No position will be vacant. The computer will respond with black or white pegs indicating accuracy. A white peg indicates a correct color chosen but wrong position. A black peg indicates a correct color chosen in the correct position. There are currently 7 colored pegs available for the code. They are red, blue, yellow, green, purple, orange, and brown.

The player allignes the clored pegs as they choose and then click the check code button next to that row. The computer will then check the code and post the results. The player has 15 tries to crack the code.

This application is written in Python using Tkinter as the GUI framework. This application also uses a custom script called mylogger.py in order to write status updates to the file log.log.

