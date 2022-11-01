# get file name from user
## input   file name   (string)
## output   file name    (string)

# find file in directory
## input   file name    (string)
## output   the file    (file handle)

# get the text contents of a file -
## input   the file    (file handle)
## output   all the text in the file    (a list of strings)
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

filename = GetFileName()
FileHandle = FindFile(filename)
lines = GetTextContents(FileHandle)
print(lines)


