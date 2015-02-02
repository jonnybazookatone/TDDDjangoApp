from .base import FunctionalTest


class LayOutAndStyling(FunctionalTest):

    def test_layout_and_styling(self):
        # The user goe to the web page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # The user notices the input box is centred
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2.0,
            512,
            delta=10
        )

        # The user enters a new item and see this is nicely centred too
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width']/2.0,
            512,
            delta=10
        )
