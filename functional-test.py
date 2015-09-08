from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase): #1

	def setUp(self): #2
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self): #3
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self): #4
		# edith menemukan web baru dan mencoba blah blah
		self.browser.get('http://localhost:8000')
		
		# dia sadar page titlenya itu nyebut to-do list
		self.assertIn('To-Do', self.browser.title) #5
		self.fail('Finish the test') #6

		# dia boleh memasukan item setelahnya
		# dan blah blah blah
		# more blah blah blah
		# blah blah blah blah

if __name__ == '__main__': #7
	unittest.main(warnings='ignore') #8
