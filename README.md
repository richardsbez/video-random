<p align="center">
  <img src="./VideoRandom.png" alt="Random Video Player Logo" width="200">
</p>

# <p align="center">🎬 Random Video Player</p>

Here is the English translation for your README.md:

🎬 Random Video Player
This is a simple and efficient Python script designed for Linux systems that selects and plays a random video from a specific folder (such as gallery-dl or Instagram downloads).

✨ Features
Random Selection: Picks a video at random within the configured directory.

Automatic Installation: On its first run, the script automatically creates a shortcut (.desktop) in your Linux application menu.

Dynamic Paths: The code automatically identifies its own installation path, making it highly portable.

MPV Integration: Uses the mpv player for lightweight playback and native controls.

🚀 How to Use
Prerequisites: Ensure you have python3 and mpv installed on your system.

Bash
sudo apt install mpv
Configuration: Place your videos in the gallery-dl/instagram folder (or adjust the path in the script).

Execution:

Bash
´python3 video_random.py´
App Menu: After the first run, you can open "Random Video Player" directly from your system's app menu without using the terminal.

📁 Project Structure
video_random.py: The main Python script.

VideoRandom.png: Project icon or screenshot.

mise.toml: Environment configurations (if using the mise manager).

README.md: Project documentation.
