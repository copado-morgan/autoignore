# Script to parse newline-separated managed package lists from text files.
# Works best with a 1 column csv file of namespaces. Copy the table from your installed packages list in your salesforce org setup. Strip the results down  to just the namespaces column using your favorite spreadsheet tool.
# Syntax:
# python3 autoignore.py -i filename.csv -o outputPrefix
# -o is optional. Example "-o test" would output "test.gitignore"
# Used to help create gitignore files for salesforce git repos. You don't need to commit managed package classes, triggers and apex pages, so pull the namespaces of all your managed packages from your installed package page.
