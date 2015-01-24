from selenium import webdriver
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
        self.fail('Finish the test')


        # She is invited to enter a to-do item straight away

        # She types 'buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1. Buy peacock feathers" as an item on the to-do list

        # There is still a textbox inviting the user to add another item. They enter
        # "use peacock feathers to make a fly"

        # The page updates and now both items show in the to-do list

        # The user wonders if it will save their list, it tells the user that a unique url has been created for them

        # The user visits that url - the to-do list is still there

        # Satisfied, the user closes the webpage

if __name__ == "__main__":
    unittest.main(warnings='ignore')