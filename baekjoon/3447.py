import sys

code = sys.stdin.readlines()
for line in code:
    line = line.rstrip()
    while 'BUG' in line:
        line = line.replace('BUG', '')
    print(line)