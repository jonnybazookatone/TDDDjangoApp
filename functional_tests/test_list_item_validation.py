from .base import FunctionalTest
from unittest import skip
from lists.forms import DUPLICATE_ITEM_ERROR


class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):

        # The user goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        error = self.get_error_element()
        self.assertEqual(error.text, 'You cannot have an empty list item')

        # The user tries again with some text for the item, which now works
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys('\n')

        # Perversely, she now decides to submit a second blank list item
        self.get_item_input_box().send_keys('\n')

        # The user receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, 'You cannot have an empty list item', error.text)

        # The user can correct it by filling some text in
        self.get_item_input_box().send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):

        # User goes to the page and stars a new list
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies')
        self.get_item_input_box().send_keys('\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # The user accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys('Buy wellies\n')

        # The user receives a helpful message that informs them
        # of their mistake
        error = self.get_error_element()
        self.assertEqual(error.text, DUPLICATE_ITEM_ERROR)

    def test_error_messages_are_cleared_on_input(self):

        # User starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # The user starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('a')

        # The user is pleased to see that the error message dissapears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())

    def test_error_messages_are_cleared_on_input_box_click(self):

        # User starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # The user starts typing in the input box to clear the error
        self.get_item_input_box().click()

        # The user is pleased to see that the error message dissapears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
