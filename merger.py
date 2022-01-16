import os

mainDirectory = os.path.join(os.path.dirname(__file__), "main/")


# Return a list of all python files in the specified directory
def getPyFiles(directory):
    fileList = []
    for item in os.listdir(directory):
        itemNamePath = os.path.join(directory, item)
        if os.path.isdir(itemNamePath):
            fileList.extend(getPyFiles(itemNamePath))
        elif os.path.isfile(itemNamePath):
            if itemNamePath.endswith('.py') and itemNamePath != __file__:
                fileList.append(itemNamePath)
        else:
            print("Item " + itemNamePath + " is neither a file nor a directory, skipping it.",
                  file=sys.stderr, flush=True)
    return fileList


# Return the index of the 'main/main.py' file from the specified list
def getMainFileIndex(fileList):
    mainFileIndex = -1
    for index, file in enumerate(fileList):
        if file == os.path.join(mainDirectory, "main.py"):
            mainFileIndex = index
            break
    if mainFileIndex == -1:
        raise FileNotFoundError(
            "No 'main.py' file found in the 'main' directory")
    return mainFileIndex


# Get all python files from the 'main' directory and its sub-directories
fileList = getPyFiles(mainDirectory)

# Move the 'main.py' file to the end of the list
# so that it is appended last to the 'merge.py' file
fileList.append(fileList.pop(getMainFileIndex(fileList)))


mergeFile = open("merge.py", "w")

# Extract all imports, and append them to the 'merge.py' file
imports = set()
for f in fileList:
    readFile = open(f, "r")
    for line in readFile:
        if line.__contains__("import"):
            imports.add(line)
for s in imports:
    mergeFile.write(s)
mergeFile.write("\n")


# Append the content of each file at the end of the 'merge.py' file
for f in fileList:
    mergeFile.write("\n")
    readFile = open(f, "r")
    for line in readFile:
        if not line.__contains__("import"):
            mergeFile.write(line)
    readFile.close()
    mergeFile.write("\n")
