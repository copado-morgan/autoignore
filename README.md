# Script to parse newline-separated managed package lists from text files.
# works best with a 1 column csv file of namespaces. Will trim whitespace in the future, but watch for it now.
#Syntax:
#python3 autoignore.py filename.csv

Used to help create gitignore files for salesforce git repos. You don't need to commit managed package classes, triggers and apex pages, so pull the namespaces of all your managed packages from your installed package page.
