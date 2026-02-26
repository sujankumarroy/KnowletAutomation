import os 

ROOT_DIR = "/sdcard/.workspace/web/knowlet/notes"
count = 0
for root, _, files in os.walk(ROOT_DIR):
	for file in files:
		
		if file.endswith(".html"):
			
			file_path = os.path.join(root, file)
			with open(file_path, "r") as r:
				content = r.read()
			if '''<link rel="stylesheet" href="../../../../assets/styles/supabase.css">''' in content:
				content = content.replace('   <link rel="stylesheet" href="../../../../assets/styles/supabase.css">','')

				with open(file_path, "w") as w:
					w.write(content)

				print(file_path.replace(ROOT_DIR, ""))
				count += 1

print("total: {}".format(count))