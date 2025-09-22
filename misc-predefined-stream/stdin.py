import sys

for line in sys.stdin:
    if line.strip() == 'q':
        break
    print(line)

print('You pressed q, bye!')
