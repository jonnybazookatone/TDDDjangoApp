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

        # The user has heard about a really new and cool website and so goes to investigate it
        self.browser.get('http://localhost:8000')

        # They notice the title of the webpage mentions to-do lists
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types 'Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item on the to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy peacock feathers' for row in rows)
        )

        # There is still a textbox inviting the user to add another item. They enter
        # "use peacock feathers to make a fly"
        self.fail('Finish the test')

        # The page updates and now both items show in the to-do list

        # The user wonders if it will save their list, it tells the user that a unique url has been created for them

        # The user visits that url - the to-do list is still there

        # Satisfied, the user closes the webpage

if __name__ == "__main__":
    unittest.main(warnings='ignore')