import re, os, sys, getopt

'''
This script can be usefull for when a comma is placed in a cell.  
For Example.
Here is a row with a cell that contains the user name.
Math,"Doe,John",Class 101

Find the index of the comma, (Index starts at 1) and run the script
removeComma.py -i classes.csv -o classes2.csv -d 2

The new cell will now look like this.
Math, "Doe John",Class 101
'''


def nth_repl(s, sub, repl, n):
	find = s.find(sub)
	# If find is not -1 we have found at least one match for the substring
	i = find != -1
	# loop util we find the nth or we find no match
	while find != -1 and i != n:
		# find + 1 means we start searching from after the last match
		find = s.find(sub, find + 1)
		i += 1
	# If i is equal to n we found nth match so replace
	if i == n:
		return s[:find] + repl + s[find+len(sub):]
	return s

def main(argv):
	inputfile=''
	outputfile=''
	removeCommaAt=''
	try:
		opts, args = getopt.getopt(argv,"hi:o:d:",["ifile=","ofile=","dindex="])
		print(opts)
	except getopt.GetoptError:
		print('removeComma.py -i <inputfile> -o <outputfile> -d <Index of comma to remove. (index starts at 1>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('removeComma.py -i <inputfile> -o <outputfile> -d <Index of comma to remove>')
			sys.exit()
		elif opt in ("-i", "-ifile"):
				inputfile = arg
		elif opt in ("-o", "-ofile"):
				outputfile = arg 	
		elif opt in ("-d", "-dindex"):	
				removeCommaAt = int(arg)
				
	if os.path.exists(outputfile):
				os.remove(outputfile)
		
	with open(inputfile) as f:
		open(outputfile, 'a').write(f.readline())
		next(f)
		for line in f:
			line = nth_repl(line, ",","",removeCommaAt)
			print(line)
			print(removeCommaAt)
			open(outputfile, 'a').write( re.sub('[^a-zA-Z0-9\n\.\,\-\\\/]', ' ',line))
	f.close()

if __name__ == "__main__":
	main(sys.argv[1:])
