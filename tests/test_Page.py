import unittest
from page_gen.Page import Page


class TestPage(unittest.TestCase):

    def test_that_page_contains_its_own_text(self):
        page = Page("some text", "")
        self.assertEqual("some text", page.text)

    def test_that_page_has_name(self):
        page = Page("some text", "Super Page")
        self.assertEqual("Super Page", page.name)


