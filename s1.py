import os.path
import sys
# default input and output file names
inputFileName = '1.hkl'
outputFileName = '1_out.hkl'
batchFlag = ' 1' #The needed batch file number, which will be filtered out
terminalLineEndingSequence = ' 0'
# attempt to import the input and output file names

#Header
print('')
print('===============================================================')
print('Program: HKLF5 batch splitter, v1.01, 15/02/2024  ')
print('Syntax: progName.ext input_file.ext output_file.ext batchNumber')
print('===============================================================')
print('')


counter = 1
try:
	inputFileName = sys.argv[1]	
except:
	print("Error: file name unrecognized")
try:
	outputFileName = sys.argv[2] 	
except:
	print("Error: file name unrecognized")
try: 
	batchFlag = sys.argv[3]
	if len(batchFlag) > 2:
		print("batchFlag is not recognized")
except:
	print("Error: batchFlag is not recognized")

if len(batchFlag) == 1:
	batchFlag = ' ' + batchFlag
	
print("Batch processed:", batchFlag)

def lineSorter(lineCurrent):
	if (lineCurrent[len(lineCurrent)-3:len(lineCurrent)-1]) == batchFlag:
		return lineCurrent
	else:
		return ''
		
f = open(inputFileName, 'r')
if os.path.isfile(outputFileName) == False:
	f_out = open(outputFileName, 'x')
else:
	f_out = open(outputFileName, 'w')

Lines = f.readlines()	

		
for line in Lines:	
	lineSorted = lineSorter(line)
	if lineSorted != '':
		lineSorted = lineSorted[0:len(lineSorted)-2]	
		while lineSorted[len(lineSorted)-2:len(lineSorted)-1] == ' ':
			lineSorted=lineSorted[0:len(lineSorted)-1]
		if lineSorted.endswith('\n') == False:
			lineSorted = lineSorted + '\n'				
		f_out.write(lineSorted)


	

counter = -1
while Lines[counter] == ('' or '\n') :
	counter = counter - 1
lastLine =  Lines[counter]
if lastLine[len(lastLine)-3:len(lastLine)-1] == terminalLineEndingSequence :     #Adding the final line with zeroes of the hkl file, if there was such a line
	f_out.write(lastLine)

try:
	f.close()
	f_out.close()
except: 
	print("File operations were not successful")
else: 
	print("Successful termination")
