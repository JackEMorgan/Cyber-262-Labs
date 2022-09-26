# Jack Morgan, Cyber 262, Hozza, 3/22/2022

logA = open("Log-A.strace", "r")
logB = open("Log-B.strace", "r")

logA_content = logA.readlines()
readExp = " read("
counter = 0
for line in logA_content:
    if readExp in line:
        #print('Read from LogA: ' + line)
        counter += 1
print("Jack Morgan count_logAread " + str(counter))

logB_content = logB.readlines()
readExp = " read("
counter = 0
for line in logB_content:
    if readExp in line:
        #print('Read from LogB: ' + line)
        counter += 1
print("Jack Morgan count_logBread " + str(counter))

counter = 0
readExp = " read("
keyboardExp = "tty"
for line in logA_content:
    if readExp in line and keyboardExp in line:
        counter += 1
print("Jack Morgan count_logAkeyboard " + str(counter))

counter = 0
readExp = " read("
keyboardExp = "tty"
for line in logB_content:
    if readExp in line and keyboardExp in line:
        counter += 1
print("Jack Morgan count_logBkeyboard " + str(counter))

counter = 0
readExp = " read("
keyboardExp = "tty"
pipeExp = "pipe"
for line in logA_content:
    if readExp in line and keyboardExp not in line and pipeExp not in line:
        counter += 1
print("Jack Morgan count_logAfilename " + str(counter))

counter = 0
readExp = " read("
keyboardExp = "tty"
pipeExp = "pipe"
for line in logB_content:
    if readExp in line and keyboardExp not in line and pipeExp not in line:
        counter += 1
print("Jack Morgan count_logBfilename " + str(counter))
