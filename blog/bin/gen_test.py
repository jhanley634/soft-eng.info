import unittest

from blog.bin.gen import BlogFormatter


class GenTest(unittest.TestCase):
    def test_href(self) -> None:
        bf = BlogFormatter
        self.assertEqual(
            '<a href="https://example.com">example</a>',
            bf._href("https://example.com", "example"),
        )
