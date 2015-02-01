from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitor(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):

        # The user has heard about a really new and cool website and so goes to investigate it
        self.browser.get(self.server_url)

        # They notice the title of the webpage mentions to-do lists
        # import time
        # time.sleep(5)
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types 'Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, she is taken to a new URL
        # and now the page lists "1: Buy peacock feathers"
        # as an item in the to-do list table
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a textbox inviting the user to add another item. They enter
        # "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates and now both items show in the to-do list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # A new user arrives and we use a new browser session to make
        # sure that no information of the previous user's list comes
        # through the cookies
        self.browser.quit()

        self.browser = webdriver.Firefox()

        # They visit the home page
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # The new user enters their list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # The new user gets their unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotIn(francis_list_url, edith_list_url)

        # Again, there is no trace of the previous user's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, the user closes the webpage