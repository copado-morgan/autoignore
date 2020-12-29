# Script to parse newline-separated managed package lists from text files.
# works best with a 1 column csv file of namespaces.
# Syntax:
# python3 autoignore.py -i filename.csv -o outputPrefix
import argparse

# command line switches
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True)
parser.add_argument("-o", "--output", required=False)
args = parser.parse_args()
if args.output:
    outputFileName = args.output + ".gitignore"
else:
    outputFileName = "generated.gitignore"

# takes input file, assigns to str var
nameSpaces = open(args.input)
nameSpacesVar = nameSpaces.readlines()
nameSpaces.close()

# takes default.gitignore, assigns to var
defaultIgnore = open('./resources/default.gitignore')
defaultIgnoreVar = defaultIgnore.read()
defaultIgnore.close()

# parses input file as list, strips whitespace and newlines
with open(outputFileName, "w") as outputFile:  # export newFileLines to text file
    outputFile.write(defaultIgnoreVar + '\r')
    for nameVal in nameSpacesVar:
        nameVal.strip()
        nameVal = nameVal.replace('\n', '')
        nameVal = nameVal.replace('\r', '')

        if nameVal:
            outputFile.write('classes/' + nameVal + '__*' + '\r')
            outputFile.write('triggers/' + nameVal + '__*' + '\r')
            outputFile.write('pages/' + nameVal + '__*' + '\r\r')
    print(outputFileName + " file created")
