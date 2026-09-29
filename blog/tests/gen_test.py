
import unittest

from blog.bin.gen import BlogFormatter, generate_blog_posts


class GenTest(unittest.TestCase):

    def test_blog_formatter(self):
        bf = BlogFormatter()

        self.assertGreater(len(bf.files), 2)
        self.assertEqual(bf.files, list(bf.prev.keys()))
        self.assertEqual(bf.files, sorted(bf.next.keys()))

        self.assertEqual('2021-12-14-complexity.html', bf._html_suffix(bf.files[0]))

    def test_generate(self):
        """This is an integration test, which side effects the filesystem.
        """

        # Formatting happens in spawned child, and thus no coverage counters are incremented.
        generate_blog_posts()

        # Formatting happens in current process, letting us observe counter increments.
        bf = BlogFormatter()
        list(map(bf.format_blog, bf.files))
