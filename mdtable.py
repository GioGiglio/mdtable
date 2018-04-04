#!/usr/bin/python
from __future__ import print_function
import sys

def main():
	cols = len(sys.argv) -1
	if not cols > 1:
		print('Invalid format: more than 1 cols needed', file=sys.stderr)
		return

	print(*sys.argv[1:],sep=' | ')
	print((cols * ' --- |').strip('|'))

	for line in sys.stdin:
		line = line.strip()
		tokens = line.split()
		tokens[cols-1] = ' '.join((tokens[cols -1:]))
		print(*tokens[0:cols], sep=' | ')

if __name__ == '__main__':
	main()