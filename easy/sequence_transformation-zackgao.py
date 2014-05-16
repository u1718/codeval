import fileinput

def countSections(line):
    last = line[0]
    count = 1
    for i in range(len(line)):
        if line[i] != last:
            count += 1
        last = line[i]
    return count

def singleLetter(line):
    last = line[0]
    for i in range(len(line)):
        if line[i] != last:
            return False
        last = line[i]
    return True

def allA(line):
    last = "A"
    for i in range(len(line)):
        if line[i] != last:
            return False
        last = line[i]
    return True

def allB(line):
    last = "B"
    for i in range(len(line)):
        if line[i] != last:
            return False
        last = line[i]
    return True

def allZero(line):
    last = "0"
    for i in range(len(line)):
        if line[i] != last:
            return False
        last = line[i]
    return True

def allOne(line):
    last = "1"
    for i in range(len(line)):
        if line[i] != last:
            return False
        last = line[i]
    return True

for line in fileinput.input():
    test = line.strip().split()
    if singleLetter(test[1]):
        if allA(test[1]) and len(test[1]) >= len(test[0]):
            print "Yes"
        elif allB(test[1]) and allOne(test[0]) and len(test[1]) >= len(test[0]):
            print "Yes"
        else:
            print "No"
    elif countSections(test[0]) == countSections(test[1]):
        print "Yes"
    elif countSections(test[0]) > countSections(test[1]):
        print "Yes"
    else:
        print "No"
