filenames = ['one.txt', 'two.txt', 'three.txt'] 
with open('/Users/Geckl/Desktop/TestTexts/output.txt', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile: 
			outfile.write(infile.read())
			outfile.write(" ")
