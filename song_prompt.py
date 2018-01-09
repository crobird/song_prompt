#!/usr/bin/env python

import random

DEFAULT_MIN_BPM     = 80
DEFAULT_MAX_BPM     = 160
DEFAULT_MODULE_FILE = 'modules.txt'
DEFAULT_MODULE_NUM  = 1

def get_bpm(min, max, step):
	if step:
		return random.randrange(min, max, step)
	else:
		return random.randrange(min, max)


def get_module_list(module_file):
	modules = []
	with open(module_file, 'r') as fh:
		for line in fh:
			if line.rstrip():
				modules.append(line.rstrip())
	random.shuffle(modules)
	return modules


def main(args):
	bpm = get_bpm(args.min, args.max, 5 if args.round else None)
	print("BPM: {}".format(bpm))

	modules = get_module_list(args.module_file)
	for i in range(args.number_of_modules):
		print(modules.pop())


if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('--min', help="Minimum BPM range (default: {})".format(DEFAULT_MIN_BPM), default=DEFAULT_MIN_BPM, type=int)
	parser.add_argument('--max', help="Maximum BPM range (default: {})".format(DEFAULT_MAX_BPM), default=DEFAULT_MAX_BPM, type=int)
	parser.add_argument('--round', help="Round BPM to nearest 5", default=False, action="store_true")
	parser.add_argument('-F', '--module_file', 
		help="File of modules to randomize through (default: {})".format(DEFAULT_MODULE_FILE),
		default=DEFAULT_MODULE_FILE)
	parser.add_argument('-N', '--number_of_modules',
		help="Number of modules to return (default: {})".format(DEFAULT_MODULE_NUM),
		default=DEFAULT_MODULE_NUM,
		type=int)

	args = parser.parse_args()

	main(args)