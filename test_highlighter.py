import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from highlighter import tokenize, to_html

class LexerTests(unittest.TestCase):
    def test_keywords_and_identifiers(self):
        result = tokenize("int total = 10;")
        self.assertIn(("keyword", "int"), result)
        self.assertIn(("identifier", "total"), result)

    def test_number_and_operator(self):
        result = tokenize("x += 25;")
        self.assertIn(("operator", "+="), result)
        self.assertIn(("number", "25"), result)

    def test_string_and_comment(self):
        result = tokenize('"hello" // note')
        self.assertIn(("string", '"hello"'), result)
        self.assertIn(("comment", "// note"), result)

    def test_html_escaping(self):
        page = to_html("if (a < b) return 1;")
        self.assertIn("&lt;", page)
        self.assertIn('class="keyword"', page)

if __name__ == "__main__":
    unittest.main()
