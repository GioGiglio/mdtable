#!/usr/bin/python
#encoding: utf-8
from __future__ import print_function
import sys

def main():
	cols = len(sys.argv) -1

	if len(sys.argv) < 2:
		print("Error: Provide column names or '-f' flag to get them from the first line", file=sys.stderr)
		exit(1)

	# check -f flag
	if sys.argv[1] == '-f':
		headers = next(sys.stdin).split()
		print(*headers, sep=' | ')
		cols = len(headers)
	elif cols < 2:
		print('Error: More than 1 column needed', file=sys.stderr)
		exit(1)
	else:
		print(*sys.argv[1:],sep=' | ')
	
	print((cols * ' --- |').strip('|').strip())

	for line in sys.stdin:
		tokens = line.split()
		tokens[cols-1] = ' '.join((tokens[cols -1:]))
		print(*tokens[0:cols], sep=' | ')

if __name__ == '__main__':
	main()