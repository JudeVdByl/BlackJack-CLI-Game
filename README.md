```markdown

Blackjack CLI
A simple command‑line Blackjack game written in Python. Great for learning how to work with lists, control flow, and basic game logic.

Demo

Features
Deal random cards to player and dealer

Detect aces as either 11 or 1 to prevent busts

Loop for multiple games in one session

Clean win, lose, draw messages

Quick start
```bash

Clone the repo
git clone https://github.com/<your-user>/blackjack-cli.git
cd blackjack-cli

(Optional) create a virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

Run the game
python blackjack.py
```

Requires Python 3.8+. No external dependencies.

How it works
card_deal(total) — returns the value of a randomly dealt card. If dealing an ace (11) would bust the given total, the ace is automatically counted as 1 instead.

The main while loop keeps the game running until the player opts out.

Dealer draws until their total is at least 17, following standard Blackjack rules.

Read through the source code in blackjack.py and see the inline docstrings for more details.

Roadmap
 Refactor into functions/classes to improve readability

 Add unit tests

 Replace input() with argparse flags for automated testing

 Add colors to terminal output

 Build a GUI version with Tkinter or PyGame

Contributing
Feel free to fork the repo and submit pull requests. Make sure your code passes flake8 and includes tests for new features.

License
Distributed under the MIT License. See LICENSE for more information.
```
