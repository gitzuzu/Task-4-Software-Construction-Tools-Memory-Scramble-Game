# Memory Scramble Game

This repository contains the implementation of a configurable Memory Scramble Game developed for the Software Construction Tools course.

The game challenges players to uncover matching card pairs before the countdown timer expires.
Players can customize the board dimensions and game duration before starting each session.

---

## Developer

- Zeina Hesham — 11422025440337

---

## Requirements

Before running the project, make sure the following are installed:

- A modern web browser (Chrome, Edge, Firefox, etc.)
- Visual Studio Code or any code editor (optional)

No additional libraries or frameworks are required.

---

## Running the Game

1. Download or clone the repository:

```bash
git clone https://github.com/your-username/memory-scramble-game.git
```

2. Open the project folder.

3. Launch the game by opening:

```text
index.html
```

The game will start directly in the browser.

---

## Gameplay Instructions

### Step 1 — Configure the Game

Before starting, the player can select:

- Number of rows
- Number of columns
- Countdown timer duration

The game automatically ensures that the total number of cards is even so every card has a matching pair.

---

### Step 2 — Start Playing

After pressing the Start button:

- Cards are shuffled randomly
- All cards are placed face-down
- The countdown timer begins immediately

---

### Step 3 — Match Cards

- Click one card to reveal it
- Click a second card to attempt a match

If the cards match:
- They remain face-up

If the cards do not match:
- They flip back face-down after a short delay

---

### Step 4 — Win or Lose

- Match all pairs before the timer ends to win
- If time reaches zero before matching all cards, the game displays a Game Over message

---

## Features

- Fully configurable board size
- Adjustable countdown timer
- Random card shuffling every game
- Interactive card flipping system
- Match detection logic
- Win and Game Over screens
- Responsive user interface
- Smooth and simple gameplay experience

---

## Technologies Used

- HTML
- CSS
- JavaScript
- Git & GitHub

---

## Project Structure

```text
memory-scramble-game/
│
├── index.html
├── style.css
├── script.js
├── assets/
│   └── icons/
├── README.md
└── .gitignore
```

---

## Repository Link

Replace the link below with your public GitHub repository:

```text
https://github.com/your-username/memory-scramble-game
```

---

## Notes

- The project was developed using GitHub for version control and collaboration.
- Multiple commits were made throughout development to properly track project progress.
- The implementation focuses on simplicity, usability, and clean game interaction.