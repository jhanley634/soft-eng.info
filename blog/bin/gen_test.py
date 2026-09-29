from pathlib import Path
import unittest

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

    def test_format_blog(self) -> None:
        folder = Path("/tmp/k")
        for suffix in ["", "common", "out"]:
            (folder / suffix).mkdir(exist_ok=True)

        md = folder / "hello.md"
        with open(md, "w") as fout:
            fout.write("hello [world](https://world.com)")
        with open(folder / "common" / "footer.md", "w") as fout:
            fout.write("footer\n")

        bf = BlogFormatter(folder)
        bf.format_blog(md)

        html = folder / "out" / "hello.html"
        self.assertEqual(
            self.expected_hello.lstrip(),
            html.read_text(),
        )
