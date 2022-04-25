filenames = ['BrEd.txt', 'colton.txt', 'Garrett.txt', 'Kasey.txt', 'sam.txt', 'victor.txt', 'zoey.txt'] 
with open('/Users/Geckl/Documents/itp/Morning/output.txt', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile: 
			outfile.write(infile.read())
			outfile.write(" ")
