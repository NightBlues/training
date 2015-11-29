from pprint import pprint
from collections import deque
import argparse


class BencodeError(Exception):
	pass


class UnexpectedEnd(BencodeError):
	def __init__(self, msg="End of stream found during parsing."):
		super(UnexpectedEnd, self).__init__(msg)


class Bencoder(deque):
	def __init__(self, source):
		super(Bencoder, self).__init__(source)

	def parse(self):
		try:
			self.result = self.token()
		except IndexError:
			raise UnexpectedEnd()
		except:
			pprint(self)
			raise

		return self.result

	def _read_till(self, char):
		c_char = ""
		result = ""
		while c_char != char:
			result += c_char
			c_char = self.popleft()
		return result

	def read_int(self):
		return int(self._read_till("e"))

	def read_bytes(self):
		size = int(self._read_till(":"))
		return "".join(self.popleft() for i in range(size))

	def read_list(self):
		result = []
		next_char = self.popleft()
		while next_char != "e":
			self.appendleft(next_char)
			result.append(self.token())
			next_char = self.popleft()

		return result

	def read_dict(self):
		tokens = self.read_list()
		keys = (k for n, k in enumerate(tokens) if not n % 2)
		values = (k for n, k in enumerate(tokens) if n % 2)
		return dict(zip(keys, values))

	def token(self):
		action = self.popleft()
		token = None
		if action == "i":
			token = self.read_int()
		elif action == "l":
			token = self.read_list()
		elif action == "d":
			token = self.read_dict()
		else:
			self.appendleft(action)
			token = self.read_bytes()

		return token


def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("torrent", type=argparse.FileType("r"))
	return parser.parse_args()


def main(args):
	parser = Bencoder(args.torrent.read())
	pprint(parser.parse())

if __name__ == "__main__":
	main(parse_args())
