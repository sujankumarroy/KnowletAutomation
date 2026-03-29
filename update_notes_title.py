import os
import re

FOLDER_PATH = "/sdcard/.workspace/web/knowlet/pyq"  # Change this to your folder containing HTML files

def get_semester(sem):
  """Determine semester based on course code number."""
  sem = int(sem)
  if sem == 1:
    return "1st Semester"
  elif sem == 2:
    return "2nd Semester"
  elif sem == 3:
    return "3rd Semester"
  elif sem == 4:
    return "4th Semester"
  elif sem == 5:
    return "5th Semester"
  elif sem == 6:
    return "6th Semester"
  elif sem == 7:
    return "7th Semester"
  elif sem == 8:
    return "8th Semester"
  else:
    return "Any Semester"

def generate_title(path):
  name = path.removeprefix(FOLDER_PATH).removesuffix('.html')
  parts = name.split("/")
  #  notes/semester_1/ecology/dsc_101/unit_1
  sem = ' '.join(parts[1].split('_')).capitalize()
  sub = ' '.join(w.capitalize() for w in (parts[2].split('_')))
  paper = ' '.join(parts[3].split('_')).upper()
#   unit = ' '.join(parts[4].split('_')).capitalize()
  
  pptTitle = "Solved Question Paper - " + parts[4].split('_')[0]

  semester = get_semester(int((parts[1].split('_'))[1]))
  
#   return f"{sub} {paper} {unit} | {semester} Notes - Knowlet"
  return f"{sub} {paper} {pptTitle} | {semester} - Knowlet"
  
# Regex to find <title> tag
title_pattern = re.compile(r'<title>.*?</title>', re.IGNORECASE)

Changed = 0
Total = 0
CL = []

for root, _, files in os.walk(FOLDER_PATH):
  for filename in files:
    # if re.match(r"unit_(\d+)\.html", filename):
      file_path = os.path.join(root, filename)
      Total += 1
      
      with open(file_path, "r", encoding="utf-8") as f:
        c = f.read()
      
      new_title = generate_title(file_path)
      print(new_title)
      #print(new_title)
      if title_pattern.search(c):
        # Replace existing title
        nc = title_pattern.sub(f"<title>{new_title}</title>", c)
      else:
        # Insert <title> inside <head> if missing
        nc = re.sub(r"(<head.*?>)", r"\1\n<title>" + new_title + "</title>", c, flags=re.IGNORECASE)
      
      if c != nc:
        Changed += 1
        with open(file_path, "w", encoding="utf-8") as f:
          f.write(nc)
        print(f'{file_path.removeprefix(FOLDER_PATH)} ✅')
        
print(f"All titles updated successfully!\nTotal: {Total}\nChanged: {Changed}")