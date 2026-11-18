import os
import shutil

os.makedirs("/output", exist_ok=True)
shutil.copyfile("news.png", "/output/entry.png")
