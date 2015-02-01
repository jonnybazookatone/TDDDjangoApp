from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):

        # The user goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refereshes, and there is an error message saying
        # that list items cannot be blank

        # The user tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # The user receives a similar warning on the list page

        # The user can correct it by filling some text in
        self.fail('write me!')