from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# edith menemukan web baru dan mencoba blah blah
		self.browser.get('http://localhost:8000')
		
		# dia sadar page titlenya itu nyebut to-do list
		self.assertIn('To-Do lists', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Web Pribadi Wildan Anky', header_text)
		self.fail('Finish the test')

		# dia boleh memasukan item setelahnya
		# dan blah blah blah
		# more blah blah blah
		# blah blah blah blah

if __name__ == '__main__': #7
	unittest.main(warnings='ignore') #8
