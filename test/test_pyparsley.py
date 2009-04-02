#!/usr/bin/env python2.6
import unittest
from pyparsley import PyParsley
from inspect import currentframe
from os.path import dirname

class TestPyParsley(unittest.TestCase):
	
	def setUp(self):
		self.parsley = PyParsley({'title': 'title'})
		self.alt_parsley = PyParsley('{"title": "title"}')
		self.a_parsley = PyParsley({'links': ['regexp:match(a @href, ".*sign.*")']})
		self.__file__ = currentframe().f_code.co_filename
		self.__dir__ = dirname(self.__file__)
		self.file = self.__dir__ + '/yelp.html'
		self.json = '{ "title": "\\t\\tNick\'s Crispy Tacos - Russian Hill - San Francisco, CA\\n" }'
		self.native = { "title": "\t\tNick's Crispy Tacos - Russian Hill - San Francisco, CA\n" }
		self.links = '{ "links": [ "\\/signup?return_url=%2Fuser_details", "\\/signup?return_url=%2Fwriteareview", "\\/signup?return_url=%2Finvite_friends", "\\/signup?return_url=%2Fmail", "\\/signup?return_url=%2Fprofile", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup", "\\/signup" ] }'
	
	def test_file_xml(self):	
		parsed = self.parsley.parse(file = self.file, output = "json")
		self.assertEquals(self.json, parsed)
		
	def test_pruning(self):
	  parsed = self.a_parsley.parse(file = self.file, output = "json")
	  self.assertEquals(self.links, parsed)
			
	def test_json_file_xml(self):	
		parsed = self.alt_parsley.parse(file = self.file, output = "json")
		self.assertEquals(self.json, parsed)
		
	def test_native(self):
		parsed = self.alt_parsley.parse(file = self.file, output = "python")
		self.assertEquals(self.native, parsed)		
		parsed = self.alt_parsley.parse(file = self.file)
		self.assertEquals(self.native, parsed)

if __name__ == '__main__':
	unittest.main()