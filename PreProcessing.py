import os
from PIL import Image
import numpy
path = '/home/linnie/Downloads/images/Images'
files = []
for r, d, f in os.walk(path):
	for file in f:
		if '.jpg' in file:
			files.append(os.path.join(r, file))

for f in files:
	pic = numpy.asarray(Image.open(f))
	file= open("Images(AsArray).txt","w+")
	print("writing path")
	file.write(f)
	print("writing array")
	file.write(str(pic))
