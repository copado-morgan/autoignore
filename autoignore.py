# Script to parse newline-separated managed package lists from text files.
# works best with a 1 column csv file of namespaces. Will trim whitespace in the future, but watch for it now.
#Syntax:
#python3 autoignore.py filename.csv
import sys
nameSpaces = open(sys.argv[1])
#need to catch no file specified exception, provide directions.
nameSpacesVar = nameSpaces.readlines()
nameSpaces.close()
#need to strip white space. Readlines brings in as a list, the strip method is for strings
with open("generated.gitignore", "w") as outputFile: #export newFileLines to text file
    for nameVal in nameSpacesVar: #this isn't appending the __* for some reason. Am going to redo this with the format option.
        outputFile.write('classes/' + nameVal + '__*' + '\r')
        outputFile.write('triggers/' + nameVal + '__*' + '\r')
        outputFile.write('pages/' + nameVal + '__*' +'\r\r')
    print ("\"generated.gitignore\" file created")
#should probably add option to specify output filename. Could also use an option to choose overwriting existing file.
