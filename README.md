# Snake — Terminal Edition 🐍🟩

A terminal-based ASCII **Snake** game written in **Python**, featuring **real-time movement**, **ANSI color graphics**, and simple game rules on an 8×8 grid.
The snake moves continuously using timed non-blocking keypresses; you steer it with **W/A/S/D**, collect apples, and avoid collisions.

---

## ✨ Features

- **8×8 board** with compact coordinates (rows A–H, cols 0–7).
- **Real-time controls** without pressing Enter (raw/CBREAK input via `termios` + `select`).
- **Colored ASCII rendering**:
  - Snake **body** = green `■`, **head** = light green arrows (`▲◄▼►`)
  - **Apple** = red `●`
- **Lives & Apple “lifetime”**: apples expire after a number of ticks; missed apples cost lives.
- **Score & history**:
  - Score increases as you move; on game over you’re prompted for a name and the last **4 results** are kept in `history.txt`.

---

## 🎮 Controls

- **W** = up
- **A** = left
- **S** = down
- **D** = right
- **Q** = quit

> Input is read per keypress (non-blocking) on a timer tick; if no key is pressed before the tick, the snake continues in its current direction.

---

## 📦 Requirements

- **Python 3** (tested with 3.10+)
- **Linux/macOS terminal** (uses `termios`, `tty`, `select`)
  - On Windows, use **WSL** or run in a POSIX-compatible environment.
- No third-party packages required.

---

## ▶️ Run

From the project folder:

```bash
python3 Snake.py
