import unittest
from pathlib import Path

from blog.bin.gen import BlogFormatter


class GenTest(unittest.TestCase):

    def test_href(self) -> None:
        self.assertEqual(
            '<a href="https://example.com">example</a>',
            BlogFormatter._href("https://example.com", "example"),
        )

    expected_hello = """
<!DOCTYPE html>
<html lang="en">
 <head>
  <title>
   hello
  </title>
  <meta content="hello" name="description"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <meta content="#317efb" name="theme-color"/>
  <link href="asset/pandoc.min.css" media="screen" rel="stylesheet" type="text/css"/>
 </head>
 <body>
  <p>
   hello
   <a href="https://world.com">
    world
   </a>
  </p>
  <p>
   footer
  </p>
 </body>
</html>

"""

    def setUp(self) -> None:
        self.folder = Path("/tmp/k")
        for suffix in ["", "common", "out"]:
            (self.folder / suffix).mkdir(exist_ok=True)
        with open(self.folder / "common" / "footer.md", "w") as fout:
            fout.write("footer\n")

    def test_format_blog(self) -> None:
        md = self.folder / "hello.md"
        with open(md, "w") as fout:
            fout.write("hello [world](https://world.com)")

        bf = BlogFormatter(self.folder)
        bf.format_blog(md)

        html = self.folder / "out" / "hello.html"
        self.assertEqual(
            self.expected_hello.lstrip(),
            html.read_text(),
        )

    expected_index = """
<!DOCTYPE html>
<html lang="en">
 <head>
  <link href="/blog/asset/pandoc.min.css" rel="stylesheet" type="text/css"/>
  <meta content="width=device-width, initial-scale=1" name="viewport"/>
  <meta content="#317efb" name="theme-color"/>
  <meta content="soft-eng.info TOC" name="description"/>
  <title>
   soft-eng.info TOC
  </title>
 </head>
 <body>
  <h1>
   soft-eng.info
  </h1>
  <ul>
   <li>
    <a href="hello">
     hello
    </a>
   </li>
  </ul>
 </body>
</html>

"""

    def test_toc(self) -> None:
        bf = BlogFormatter(self.folder)
        bf.toc()

        index = self.folder / "out" / "index.html"
        self.assertEqual(
            self.expected_index.lstrip(),
            index.read_text(),
        )
