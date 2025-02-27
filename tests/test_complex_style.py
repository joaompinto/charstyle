#!/usr/bin/env python3
"""
Unit tests for the complex styling functions in charstyle.
"""

import unittest

from charstyle import (
    BLUE,
    BOLD,
    GREEN,
    ITALIC,
    RED,
    YELLOW,
)
from charstyle.complex_style import style_complex, style_format, style_pattern_match, style_split

# NOTE: The order of ANSI style codes is important in these tests.
# The implementation combines styles in the following order:
# 1. Style codes (BOLD, ITALIC, etc.) are applied first
# 2. Foreground color codes are applied next
# 3. Background color codes are applied last


class TestComplexStyling(unittest.TestCase):
    """Test cases for complex styling functions."""

    def test_style_split(self):
        """Test style_split function."""
        # Basic split with two parts
        result = style_split("key:value", ":", BOLD, GREEN)
        # The result format should be: "<bold>key</bold>:<green>value</green>"
        self.assertIn("key", result)
        self.assertIn("value", result)
        self.assertIn("\033[1m", result)  # Bold code
        self.assertIn("\033[32m", result)  # Green code

        # Split with more parts than styles
        result = style_split("a:b:c", ":", RED, BLUE)
        # The result should contain styled a and b, but c is unstyled
        self.assertIn("\033[31m", result)  # Red code
        self.assertIn("\033[34m", result)  # Blue code
        self.assertIn("a", result)
        self.assertIn("b", result)
        self.assertIn("c", result)

        # Split with more styles than parts
        result = style_split("a:b", ":", RED, GREEN, BLUE)
        # The result should have styled a and b, but the third style isn't used
        self.assertIn("\033[31m", result)  # Red code
        self.assertIn("\033[32m", result)  # Green code
        self.assertIn("a", result)
        self.assertIn("b", result)

    def test_style_complex(self):
        """Test style_complex function."""
        # Basic regex split - splitting on the words in the middle
        text = "The value is 42 and status is OK"
        pattern = r"(value is \d+)|(status is \w+)"
        result = style_complex(text, pattern, RED, GREEN)

        # Check the text is present and styling is applied
        self.assertIn("The ", result)
        self.assertIn("value is 42", result)
        self.assertIn(" and ", result)
        self.assertIn("status is OK", result)
        self.assertIn("\033[31m", result)  # Red code
        self.assertIn("\033[32m", result)  # Green code

        # Simple case with numbers - styling the digits in the middle
        text = "test 123 test"
        pattern = r"(\d+)"
        result = style_complex(text, pattern, BOLD)

        self.assertIn("test ", result)
        self.assertIn("123", result)
        self.assertIn(" test", result)
        self.assertIn("\033[1m", result)  # Bold code

    def test_style_pattern_match(self):
        """Test style_pattern_match function."""
        # Test with named groups
        log_line = "2023-02-27 15:30:45 [INFO] User authenticated"
        pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) \[(?P<level>\w+)\] (?P<message>.*)"
        styles = {"date": BLUE, "time": GREEN, "level": YELLOW, "message": ITALIC}

        result = style_pattern_match(log_line, pattern, styles)

        # Check content and style codes
        self.assertIn("2023-02-27", result)
        self.assertIn("15:30:45", result)
        self.assertIn("INFO", result)
        self.assertIn("User authenticated", result)
        self.assertIn("\033[34m", result)  # Blue code for date
        self.assertIn("\033[32m", result)  # Green code for time
        self.assertIn("\033[33m", result)  # Yellow code for level
        self.assertIn("\033[3m", result)  # Italic code for message

        # Test with no match
        result = style_pattern_match("No match here", pattern, styles)
        self.assertEqual(result, "No match here")

        # Test with only some groups styled
        partial_styles = {"date": BLUE, "level": YELLOW}
        result = style_pattern_match(log_line, pattern, partial_styles)
        self.assertIn("2023-02-27", result)
        self.assertIn("15:30:45", result)
        self.assertIn("INFO", result)
        self.assertIn("User authenticated", result)
        self.assertIn("\033[34m", result)  # Blue code for date
        self.assertIn("\033[33m", result)  # Yellow code for level
        self.assertNotIn("\033[32m", result)  # No green code for time
        self.assertNotIn("\033[3m", result)  # No italic code for message

    def test_style_format(self):
        """Test style_format function."""
        # Basic format with styles
        template = "User {username} logged in from {ip}"

        # Use the correct parameter format: keyword args with (text, style) tuples
        result = style_format(template, username=("admin", BOLD), ip=("192.168.1.100", RED))

        self.assertIn("\033[1madmin\033[0m", result)
        self.assertIn("\033[31m192.168.1.100\033[0m", result)
        self.assertIn("User ", result)
        self.assertIn(" logged in from ", result)

        # Format with some unstylized values
        template = "{a} {b} {c}"
        result = style_format(
            template, a=("1", BOLD), b="2", c=("3", GREEN)  # No style, just a plain string
        )

        self.assertIn("\033[1m1\033[0m", result)
        self.assertIn("2", result)  # Plain text
        self.assertIn("\033[32m3\033[0m", result)

        # Test with positional args
        template = "{} {} {}"
        result = style_format(template, ("A", RED), "B", ("C", BLUE))

        self.assertIn("\033[31mA\033[0m", result)
        self.assertIn("B", result)  # Plain text
        self.assertIn("\033[34mC\033[0m", result)


if __name__ == "__main__":
    unittest.main()
