#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser(description='Simple calculator generator')
parser.add_argument('-s', action='store', dest='s', help='Start value', default=0, type=int)
parser.add_argument('-e', action='store', dest='e', help='End value', default=5, type=int)
parser.add_argument('-p', action='store', dest='p', help='Precision', default=1, type=float)
parser.add_argument('-o', action='store', dest='o', help='Operators', default='+,-,*,/', type=str)
parser.add_argument('-f', action='store', dest='f', help='Output file', default='calc.py', type=str)
args = parser.parse_args()

START = args.s
END = args.e
PRECISION = args.p
OPS = args.o.split(',')

print(START, END, OPS, args.f)

f = open(args.f, 'w')

f.write('#!/usr/bin/python3\n')
f.write('x = input(\'x=\')\n')
f.write('y = input(\'y=\')\n')
f.write('op = input(\'operator=\')\n')

f.write('if op != \'{}\''.format(OPS[0]))
for op in OPS[1:]:
    f.write(' and op != \'{}\''.format(op))
f.write(':\n')
f.write('  print(\'Invalid operator: \'+op+\'\')\n')
f.write('  exit()\n')

f.write('if x != \'{}\''.format(START))
for x in range(START, END+1):
    f.write(' and x != \'{}\''.format(x))
f.write(':\n')
f.write('  print(\'X number out of range: \'+str(x)+\'\')\n')
f.write('  exit()\n')

f.write('if y != \'{}\''.format(START))
for y in range(START, END+1):
    f.write(' and y != \'{}\''.format(y))
f.write(':\n')
f.write('  print(\'Y number out of range: \'+str(y)+\'\')\n')
f.write('  exit()\n')

for x in range(START, END+1):
    for y in range(START, END+1):
        for op in OPS:
            f.write('if x==\'{}\' and y==\'{}\' and op==\'{}\':\n'.format(x, y, op))
            try:
                f.write('  print(\'{}{}{}={}\')\n'.format(x, op, y, eval('{}{}{}'.format(x, op, y))))
            except Exception as e:
                f.write('  print(\'{}\')\n'.format(e))
            f.write('  exit()\n')