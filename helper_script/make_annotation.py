from os import listdir

image_list = listdir("./brand")
image_list.remove('.git')
for img in image_list:
	if img[-3:] != "jpg":
		image_list.remove(img)
open("extract_db_list.txt", "w").write('\n'.join(image_list))
