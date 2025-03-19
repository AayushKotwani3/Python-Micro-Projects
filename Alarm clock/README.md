# Alarm Timer ⏰

This is a simple **Alarm Timer** written in Python. It allows users to set a countdown timer, and once the timer reaches zero, it plays an alarm sound.

## 🚀 Features
- Set an alarm using minutes and seconds.
- Displays a countdown timer.
- Plays an alarm sound when the timer ends.

## 📜 How It Works
The script uses Python’s built-in `time.sleep()` function to create a countdown. It continuously updates the remaining time and plays an alarm sound when the countdown is complete.


## 🛠 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/AayushKotwani3/Python-Micro-Pojects.git
   ```
2. Navigate to the script's directory:
   ```bash
   cd Python-Micro-Projects
   ```
3. Install the required dependency:
   ```bash
   pip install playsound
   ```
4. Run the script:
   ```bash
   python alarm.py
   ```

## 📌 Notes
- Ensure you have an `alarm.mp3` sound file in the same directory as the script.
- If `playsound` doesn't work, try using `pygame.mixer` or another sound-playing module.
