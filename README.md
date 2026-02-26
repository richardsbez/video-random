<p align="center">
  <img src="./VideoRandom.png" alt="Random Video Player Logo" width="200">
</p>

# <p align="center">🎬 Random Video Player</p>

Here is the English translation for your README.md:

🎬 Random Video Player
This is a simple and efficient Python script designed for Linux systems that selects and plays a random video from a specific folder (such as gallery-dl or Instagram downloads).

✨ Features
Random Selection: Picks a video at random within the configured directory.

Automatic Installation: On its first run, the script automatically creates a shortcut (<pre>```.desktop``` </pre>) in your Linux application menu.

Dynamic Paths: The code automatically identifies its own installation path, making it highly portable.

MPV Integration: Uses the <pre>```mpv``` </pre> player for lightweight playback and native controls.

🚀 How to Use
📦 Prerequisites

Make sure the following dependencies are installed:

<pre>```python3``` </pre>

<pre>```mpv``` </pre>

🖥 Install MPV (Debian/Ubuntu)

<pre>```
sudo apt update
sudo apt install mpv
``` </pre>

🖥 Install MPV (Arch Linux)

<pre>```
sudo pacman -S mpv
``` </pre>
  
⚙️ Configuration

Place your videos inside:

<pre>```
gallery-dl/instagram/
``` </pre>
  
Or modify the target directory directly inside:

<pre>```
video_random.py
``` </pre>


▶️ Execution

Run the script manually:

<pre>```
python3 video_random.py
``` </pre>

After the first execution, the script will automatically create a desktop entry, allowing you to open:

<pre>```
Random Video Player
``` </pre>

directly from your system’s application menu — no terminal required.

📁 Project Structure
<pre>```
.
├── video_random.py
├── VideoRandom.png
├── mise.toml
└── README.md
``` </pre>
