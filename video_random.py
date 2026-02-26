import os
import random
import subprocess
import sys
from pathlib import Path

# --- SOFTWARE SETTINGS ---
APP_NAME = "RandomVideo"

# Automatically locates the folder based on where the script is saved
BASE_DIR = Path(__file__).resolve().parent
VIDEO_DIR = BASE_DIR / "gallery-dl" / "instagram"

EXTENSIONS = {".mp4", ".mkv", ".webm", ".mov"}

# Where the system shortcut will be saved
DESKTOP_ENTRY_PATH = Path.home() / ".local/share/applications" / "random_video.desktop"


def install_software():
    """Automatically creates the shortcut in the application menu."""
    script_path = Path(__file__).resolve()

    desktop_content = f"""[Desktop Entry]
Type=Application
Name={APP_NAME}
Comment=Software to play random videos
Exec=python3 {script_path}
Icon=~/.local/share/applications/icons/VideoRandom.png
Terminal=false
Categories=AudioVideo;Player;
Keywords=video;random;instagram;
"""
    try:
        DESKTOP_ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(DESKTOP_ENTRY_PATH, "w") as f:
            f.write(desktop_content)

        # Make the shortcut executable
        DESKTOP_ENTRY_PATH.chmod(0o755)
        print(f"✅ {APP_NAME} installed successfully!")
        print(f"You can close this terminal. Look for '{APP_NAME}' in your app menu.")
    except Exception as e:
        print(f"❌ Installation error: {e}")


def play_video():
    """Main logic of the software."""
    if not VIDEO_DIR.is_dir():
        # If the folder doesn't exist, notify the user
        subprocess.run(
            ["notify-send", APP_NAME, f"Error: Folder {VIDEO_DIR} not found!"]
        )
        return

    videos = [f for f in VIDEO_DIR.iterdir() if f.suffix.lower() in EXTENSIONS]

    if not videos:
        subprocess.run(["notify-send", APP_NAME, "No videos found in the folder!"])
        return

    target_video = random.choice(videos)

    # Run mpv
    # - Native controls: [Space] Pause, [q] Quit
    subprocess.run(["mpv", "--force-window", f"--title={APP_NAME}", str(target_video)])


if __name__ == "__main__":
    # If run via terminal and shortcut doesn't exist, it installs first.
    # Then it plays the video.
    if not DESKTOP_ENTRY_PATH.exists():
        install_software()

    play_video()
