import os
import re

# Folder path containing the HTML files
folder_path = "/sdcard/.workspace/web/knowlet/pyq"
count = 0
# Loop through all files in the folder

for root, _, files in os.walk(folder_path):
    for file in files:
        if file.endswith("qp_2024.html"):
            new_name = '2024_solved.html'
            old_path = os.path.join(root, file)
            new_path = os.path.join(root, new_name)

            # Rename file if name changes
            if old_path != new_path:
                count += 1
                os.rename(old_path, new_path)
                print(f"Renamed: {file} → {new_name}\n${count}")
