import sys

def readStdin():
    data = sys.stdin.readlines()
    t = int(data[0])
    cases = list()

    print(t)
    for i in range(0,t):
        line = sys.stdin.readline()
        cases.append(line)

    for case in cases:
        print(case)

readStdin()