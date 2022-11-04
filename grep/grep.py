# get file name from user
## input   file name   (string)
## output   file name    (string)

# find file in directory
## input   file name    (string)
## output   the file    (file handle)

# get the text contents of a file -
## input   the file    (file handle)
## output   all the text in the file    (a list of strings)

# get text input from user
## input the text (string)
## output the text (string)

# search lines for that text
## input the text (string)
## output the line number (integer? string?)

print("starting the grep program")
def GetFileName():
    filename = input("File Name:")
    return filename

def FindFile(filename):
    FileHandle = open(filename)
    return FileHandle

def GetTextContents(FileHandle):
    lines = FileHandle.readlines()
    return lines

def GetSearchText():
    searchtext = input("Enter the text you are looking for:")
    return searchtext

def SearchForText(searchtext, lines):
    for line in lines:
        if (searchtext in line):
            print(line)

    # look for 'searchtext' in 'lines'

filename = GetFileName()
FileHandle = FindFile(filename)
lines = GetTextContents(FileHandle)
searchtext = GetSearchText()
SearchForText(searchtext, lines)
