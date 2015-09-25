from __future__ import print_function
import argparse
import subprocess


def run_file(script, inp):
	command = "python3 " + script
	process = subprocess.Popen(command, stdin=subprocess.PIPE,
		stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	res = process.communicate(inp)
	if process.returncode != 0:
		raise RuntimeError("Error: {0}, {1}, {2}".format(
				process.returncode, res[0], res[1]))
	return res[0]

def parse_args():
	parser = argparse.ArgumentParser(description="Check task")
	parser.add_argument("file")
	parser.add_argument("test_in")
	parser.add_argument("test_out")

	return parser.parse_args()

def main(args):
	with open(args.test_in) as fin:
		inp = fin.read()
	result = run_file(args.file, inp)
	with open(args.test_out) as fin:
		exp_result = fin.read()
	checker(result, exp_result)
	print("Ok")

def checker(result, exp_result):
	try:
		_checker(result, exp_result)
	except AssertionError:
		import inspect
		frame = inspect.trace()[-1][0]
		from pprint import pprint
		print("Locals:")
		pprint(frame.f_locals)
		raise
		# import pdb
		# pdb.set_trace()

def _checker(result, exp_result):
	result = result.strip().splitlines()
	exp_result = exp_result.strip().splitlines()
	assert len(result) == len(exp_result)
	for l_real, l_exp in zip(result, exp_result):
		assert l_real.strip() == l_exp.strip()



if __name__ == "__main__":
	main(parse_args())
