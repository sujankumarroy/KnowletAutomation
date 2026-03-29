import os

search_string = '<div class="container">'
root_folder = "/sdcard/.workspace/web/knowlet/pyq"

for root, dirs, files in os.walk(root_folder):
    for file in files:
        file_path = os.path.join(root, file)

        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                count = content.count(search_string)

                if count > 1:
                    print(f"{file_path} -> {count} times")

        except Exception:
            pass
