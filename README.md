# Memory Scramble Game

This repository contains the implementation of a configurable Memory Scramble Game developed for the Software Construction Tools course.

The game challenges players to uncover matching pairs of cards before the countdown timer expires. Players can customize the board dimensions and game duration before starting each session.

The project was developed using Python and Pygame with a modern pastel-themed user interface, animated card interactions, and custom kawaii-style icons.

---

## 👩‍💻 Developers

- Zeina Hesham — 11422025440337
- Maria Mohsen — 11

---

## 📌 Requirements

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

## 🎮 Gameplay Instructions

### Step 1 — Configure the Game

Before starting, the player can configure:

- Number of rows
- Number of columns
- Countdown timer duration

The game automatically ensures that the total number of cards is even so every card has a matching pair.

To maintain unique icon pairs, the maximum board size is limited to:

```text
4 x 4 = 16 cards
```

If the player exceeds the allowed board size, an error message is displayed.

---

### Step 2 — Start Playing

After pressing the **Start Game** button:

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
- They briefly flash red
- They flip back after a short delay

---

### Step 4 — Win or Lose

- Match all pairs before the timer reaches zero to win
- If the timer reaches zero before all matches are found, the game displays a Game Over screen

---

## ✨ Features

- Fully configurable board size
- Adjustable countdown timer
- Validation for maximum board size
- Randomized card placement every game
- Animated card flip effect
- Matching pair detection system
- Win and Game Over screens
- Restart button
- Modern pastel pink themed UI
- Hover animation and card shadows
- Responsive card layout
- Custom kawaii-style icon cards
- Smooth gameplay interactions
- Separate UI and game logic files for better organization

---

## 🛠️ Technologies Used

- Python
- Pygame
- Git & GitHub

---

## 📁 Project Structure

```text
Task-4-Software-Construction-Tools-Memory-Scramble-Game/
│
├── game.py
├── ui.py
├── README.md
└── assets/
    └── icons/
```

---

## 🔗 Repository Link

```text
https://github.com/gitzuzu/Task-4-Software-Construction-Tools-Memory-Scramble-Game
```

---

## 📝 Notes

- The project was developed using GitHub for version control and collaboration.
- Multiple commits were made throughout development to properly track project progress.
- The implementation focuses on clean UI design, smooth gameplay, and maintainable code structure.
- Gameplay logic and UI styling were separated into different files for better readability and maintainability.
- The game uses custom icon assets stored inside the `assets/icons` directory.