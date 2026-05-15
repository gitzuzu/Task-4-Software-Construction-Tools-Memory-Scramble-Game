# Memory Scramble Game

This repository contains the implementation of a configurable Memory Scramble Game developed for the Software Construction Tools course.

The game challenges players to uncover matching card pairs before the countdown timer expires. Players can customize the board dimensions and game duration before starting each session.

The project was developed using Python and Pygame with a modern pastel-themed user interface and animated card interactions.

---

## Developer

- Zeina Hesham — 11422025440337

---

## Requirements

Before running the project, make sure the following are installed:

- Python 3.10 or higher
- Pygame library

Install Pygame using:

```bash
pip install pygame
```

---

## Running the Game

1. Clone or download the repository:

```bash
git clone https://github.com/gitzuzu/Task-4-Software-Construction-Tools-Memory-Scramble-Game.git
```

2. Open the project folder.

3. Run the game using:

```bash
python game.py
```

The game window will launch automatically.

---

## Gameplay Instructions

### Step 1 — Configure the Game

Before starting, the player can configure:

- Number of rows
- Number of columns
- Countdown timer duration

The game automatically ensures that the total number of cards is even so every card has a matching pair.

---

### Step 2 — Start Playing

After pressing the Start Game button:

- Cards are shuffled randomly
- All cards appear face-down
- The countdown timer starts immediately

---

### Step 3 — Match Cards

- Click one card to reveal it
- Click a second card to attempt a match

If the cards match:
- They remain face-up

If the cards do not match:
- They flip back after a short delay

---

### Step 4 — Win or Lose

- Match all pairs before the timer reaches zero to win
- If the timer reaches zero before all matches are found, the game displays a Game Over screen

---

## Features

- Fully configurable board size
- Adjustable countdown timer
- Randomized card placement every game
- Animated card flip effect
- Match detection system
- Win and Game Over states
- Restart button
- Modern pastel pink themed UI
- Hover animation and card shadows
- Responsive card layout

---

## Technologies Used

- Python
- Pygame
- Git & GitHub

---

## Project Structure

```text
memory-scramble-game/
│
├── game.py
├── ui.py
├── README.md
└── .gitignore
```

---

## Repository Link



```text
https://github.com/gitzuzu/Task-4-Software-Construction-Tools-Memory-Scramble-Game
```

---

## Notes

- The project was developed using GitHub for version control and collaboration.
- Multiple commits were made throughout development to properly track project progress.
- The implementation focuses on clean UI design, smooth gameplay, and maintainable code structure.
- The project separates gameplay logic and UI styling into different files for better organization.