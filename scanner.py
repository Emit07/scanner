
import socket
import threading
from queue import Queue
import argparse
import sys
import socket
import time
import os

class Scanner(object):

	def worker(self):
		while True:
			item = self._queue.get()
			port, attempt = self.scan(item)

			self._ports.append((port, attempt))

			self._queue.task_done()

	def scan(self, port) -> tuple:
		attempt = self._socket.connect_ex((self._host, port))

		return (port, attempt)

	def run(self):

		self._queue = Queue()
		self._ports = []

		for i in range(self.threads):
			t = threading.Thread(target=self.worker, daemon=True)
			t.start()

		for worker in range(1, 1000):
			self._queue.put(worker)

		self._queue.join()

	def display(self):

		self._ports.sort()

		for port in self._ports:
			# if port[1] == True:
			print(port[0], port[1])

	def repr(self):

		return "<{}>".format(self._host)

	def __init__(self, host, threads=100, ranges=(0,100)):

		self._start = time.time()

		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._host = host

		self._lock = threading.Lock()
		self.threads = 100

		socket.setdefaulttimeout(1)

		self.run()
		self.display()

		with self._lock: print(time.time() - self._start)

def parse() -> tuple:    

    if len(sys.argv) > 1: 
        host = sys.argv[1]
    else: 
        name = socket.gethostname()
        host = socket.gethostbyname(name)
    
    if len(sys.argv) > 2: 
        threads = sys.argv[2]
    else: 
        threads = 100
    
    if len(sys.argv) > 4: 
        ranges = (sys.argv[3], sys.argv[4])
    else: 
        ranges = (0, 100)

    return (host, threads, ranges)

def main() -> int:

    host, threads, ranges = parse()

	scanner = Scanner(host, threads, ranges)

    return 0

if __name__ == "__main__":
	exit(main())
