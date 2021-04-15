
import socket
import threading
from queue import Queue
import sys
import ipaddress
import time
import os

class Scanner(object):

	def scan(self):
		net4 = ipaddress.ip_network("10.0.0.0/24")
		for x in net4.hosts():
			try:
				HOST_UP  = True if os.system("ping -c 1 " + str(x) + "2>&1 >/dev/null") == 0 else False
				print(HOST_UP)
			except KeyboardInterrupt:
				sys.exit()

	def __init__(self, ip : str):
		self._ip = ip

		self.scan()

def main() -> int:

	scanner = Scanner("10.0.0.1")

	return 0

if __name__ == "__main__":
	exit(main())