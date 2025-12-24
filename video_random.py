import os
import random
import subprocess

FOLDER = "/home/richards/gallery-dl/instagram"
VIDEOS = [f for f in os.listdir(FOLDER) if f.endswith((".mp4", ".mkv", ".webm"))]

if VIDEOS: 
  video = random.choice(VIDEOS)
  subprocess.run(["mpv", os.path.join(FOLDER, video)])
