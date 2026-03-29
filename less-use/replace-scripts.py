import os 

ROOT_DIR = "/sdcard/.workspace/web/knowlet/pyq"
count = 0

for root, _, files in os.walk(ROOT_DIR):
	for file in files:

		if file.endswith(".html"):

			file_path = os.path.join(root, file)
			with open(file_path, "r") as r:
				content = r.read()

			content = content.replace('../../../../assets/styles/units.css', '../../../../css/core.css')
			content = content.replace('../../../../assets/scripts/units.js', '../../../../js/core.js')

			with open(file_path, "w") as w:
				w.write(content)

			count += 1

print("total: {}".format(count))
