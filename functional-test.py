from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# dia memasukan to-do item satu per satu
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		# dia mengetikan "Buy Peacock feathers" pada textbox
		inputbox.send_keys('Buy peacock feathers')
		
		# saat dia menekan ENTER pagenya diupdate
		# "1: Buy peacock feathers" sebagai item pada to-do list
		inputbox.send_keys(Keys.ENTER)
		
		table = self.browser.find_elements_by_tag_name('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers') for row in rows
		)

		self.fail('Finish the test!')
		# dia boleh memasukan item setelahnya
		# dan blah blah blah
		# more blah blah blah
		# blah blah blah blah

if __name__ == '__main__': #7
	unittest.main(warnings='ignore') #8
