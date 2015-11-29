from pprint import pprint
import argparse


def _read_till(stream, char):
	c_char = ""
	result = ""
	while c_char != char:
		result += c_char
		c_char = stream.read(1)
	return result

def read_int(stream):
	return int(_read_till(stream, "e"))

def read_bytes(stream, r_b=""):
	size = int(r_b + _read_till(stream, ":"))
	return stream.read(size)

def read_list(stream):
	result = []
	while True:
		result.append(read_token(stream))
		if result[-1] is None:
			break
	result.pop()
	return result

def read_dict(stream):
	tokens = read_list(stream)
	keys = (k for n, k in enumerate(tokens) if not n % 2)
	values = (k for n, k in enumerate(tokens) if n % 2)
	return dict(zip(keys, values))

def read_token(stream):
	action = stream.read(1)
	token = None
	if action == "i":
		token = read_int(stream)
	elif action == "l":
		token = read_list(stream)
	elif action == "d":
		token = read_dict(stream)
	elif action == "e":
		token = None
	else:
		token = read_bytes(stream, r_b=action)

	return token




def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("torrent", type=argparse.FileType("r"))
	return parser.parse_args()


def main(args):
	pprint(read_token(args.torrent))

if __name__ == "__main__":
	main(parse_args())
