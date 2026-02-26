ROOT_FILE = '/sdcard/.workspace/assets/new_rating_rows.csv'

with open(ROOT_FILE, 'r') as r:
	content = r.read()

rows = content.splitlines()
id = 0
newContent = ''
newContent1 = ''
nc = 0
nc1 = 1
for row in rows:
	items = row.split(',')
	if (not items[6]):
		items[6] = 'Unknown@0000'
		row = ','.join(items)
	newContent += row + '\n'
	id += 1
# print('1/2')
# for row in rows:
# 	items = row.split(',')
# 	items[0] = str(id)
# 	newRow = ','.join(items)
# 	if (items[5]):
# 		newContent1 += newRow + '\n'
# 		id += 1
# 		print(id)
# print('2/2')
with open('/sdcard/.workspace/assets/new_rating_rows.csv', 'w') as w:
	w.write(newContent + newContent1)
print('✅ done')
print(id)