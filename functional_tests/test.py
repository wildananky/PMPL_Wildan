from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):
		# edith menemukan web baru dan mencoba blah blah
		self.browser.get(self.live_server_url)
		
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
		edith_list_url = self.browser.current_url
		self.assertRegex(edith_list_url, '/lists/.+')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
	
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
	
		self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
		self.assertIn(
			'2: Use peacock feathers to make a fly', [row.text for row in rows]
		)

		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		# dia boleh memasukan item setelahnya
		# dan blah blah blah
		# more blah blah blah
		# blah blah blah blah
		self.browser.quit()
		self.browser = webdriver.Firefox()

		self.browser.get(self.live_server_url)
		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('1: Buy peacock feathers', page_text)
		self.assertNotIn('make a fly', page_text)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Buy milk')
		inputbox.send_keys(Keys.ENTER)

		francis_list_url = self.browser.current_url
		self.assertRegex(francis_list_url, '/lists/.+')
		self.assertNotEqual(francis_list_url, edith_list_url)

		page_text = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Buy a peacock feathers', page_text)
		self.assertIn('Buy milk', page_text)

# if __name__ == '__main__': #7
	# unittest.main(warnings='ignore') #8
