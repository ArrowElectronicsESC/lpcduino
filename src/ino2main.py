import regex

mainFile = "main.c"
blinkFile = "blink.ino"
outputFile = "main.c"

def extractFunctionContent(file, functionName):
    # regex to find c function content
    regex_c_function = regex.compile(r'('+functionName+r'\s*\(.*?\)\s)({((?>[^{}]+|(?2))*)})')
    # print(regex_c_function)

    with open(file, "r") as main:
        mainContent = main.readlines()

    content = "\n".join(mainContent)

    # apply regex
    group = regex_c_function.findall(content)[0][-1]
    group = group.replace("\n\n", "\n")
    if group[0] == "\n":
        group = group[1:]
    if group[-1] == "\n":
        group = group[:-1]
    return group


with open(mainFile, "r") as main:
    mainContent = main.readlines()

with open(blinkFile, "r") as blink:
    blinkContent = blink.readlines()

codeSetupStartString = "/************************ .INO CODE SETUP START *************************/"
codeSetupEndString = "/************************ .INO CODE SETUP END *************************/"
codeLoopStartString = "/************************ .INO LOOP CODE START *************************/"
codeLoopEndString = "/************************ .INO LOOP CODE END *************************/"

# find the index of the first line of codeSetupStartString
codeSetupStartIndex = [i for i, x in enumerate(mainContent) if x.strip().startswith(codeSetupStartString)]
codeSetupStartIndex = codeSetupStartIndex[0]

# find the index of the first line of codeSetupEndString
codeSetupEndIndex = [i for i, x in enumerate(mainContent) if x.strip().startswith(codeSetupEndString)]
codeSetupEndIndex = codeSetupEndIndex[0]

mainContent.insert(codeSetupStartIndex+1, extractFunctionContent(blinkFile, "setup"))

codeLoopStartIndex = [i for i, x in enumerate(mainContent) if x.strip().startswith(codeLoopStartString)]
codeLoopStartIndex = codeLoopStartIndex[0]

codeLoopEndIndex = [i for i, x in enumerate(mainContent) if x.strip().startswith(codeLoopEndString)]
codeLoopEndIndex = codeLoopEndIndex[0]

mainContent.insert(codeLoopStartIndex+1, extractFunctionContent(blinkFile, "loop"))

with open(outputFile, "w") as result:
    for line in mainContent:
        result.write(line)
