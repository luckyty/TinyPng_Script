import tinify
import os
import os.path

tinify.key ="your key" # AppKey
fromPath ="/Users/lijiawei/Pictures/iDesign/Color/Images/Compressed/source" # source path
toPath ="/Users/lijiawei/Pictures/iDesign/Color/Images/Compressed/dest" # dest path

for root, dirs, files in os.walk(fromPath):
	newToPath = toPath
	if len(root) > len(fromPath):
		innerPath= root[len(fromPath):]
		if innerPath[0] == '/':
			innerPath = innerPath[1:]
		newToPath =  os.path.join(toPath,innerPath)
	
	for name in files:
		newFromFilePath = os.path.join(root, name)
		newToFilePath = os.path.join(newToPath, name)  
		fileName, fileSuffix = os.path.splitext(name)
		if fileSuffix == '.png' or fileSuffix == '.jpg':
			source = tinify.from_file(newFromFilePath)
			source.to_file(newToFilePath)	
		else:
			pass

	for dirName in dirs:
		os.mkdir(os.path.join(newToPath, dirName))

