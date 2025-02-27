#!/usr/bin/env python3
"""
Unit tests for the charstyle library.
"""

import unittest

import charstyle


class TestCharstyle(unittest.TestCase):
    """Test cases for charstyle library."""

    def setUp(self):
        """Set up the test case."""
        # Ensure color is supported for tests
        charstyle._supports_color = True

    # NOTE: The order of ANSI style codes is important in these tests.
    # The implementation combines styles in the following order:
    # 1. Style codes (BOLD, ITALIC, etc.) are applied first
    # 2. Color codes (RED, GREEN, etc.) are applied second
    # 3. Background color codes (BG_RED, BG_GREEN, etc.) are applied last
    # This results in strings like "\033[1;31;44mtext\033[0m" (bold, red text on blue background)

    def test_colored(self):
        """Test the colored function."""
        # Test with color only
        result = charstyle.colored("test", charstyle.RED)
        expected = "\033[31mtest\033[0m"
        self.assertEqual(result, expected)

        # Test with background color only
        result = charstyle.colored("test", bg_color=charstyle.BG_BLUE)
        expected = "\033[44mtest\033[0m"
        self.assertEqual(result, expected)

        # Test with style only
        result = charstyle.colored("test", style=charstyle.BOLD)
        expected = "\033[1mtest\033[0m"
        self.assertEqual(result, expected)

        # Test with all parameters
        result = charstyle.colored(
            "test", charstyle.GREEN, charstyle.BG_YELLOW, charstyle.UNDERLINE
        )
        expected = "\033[4;32;43mtest\033[0m"
        self.assertEqual(result, expected)

    def test_convenience_functions(self):
        """Test the convenience color functions."""
        # Test red
        result = charstyle.red("test")
        expected = "\033[31mtest\033[0m"
        self.assertEqual(result, expected)

        # Test green with background
        result = charstyle.green("test", bg=charstyle.BG_BLACK)
        expected = "\033[32;40mtest\033[0m"
        self.assertEqual(result, expected)

        # Test blue with style
        result = charstyle.blue("test", style=charstyle.BOLD)
        expected = "\033[1;34mtest\033[0m"
        self.assertEqual(result, expected)

    def test_style_functions(self):
        """Test the style convenience functions."""
        # Test bold
        result = charstyle.bold("test")
        expected = "\033[1mtest\033[0m"
        self.assertEqual(result, expected)

        # Test bold with color
        result = charstyle.bold("test", color=charstyle.YELLOW)
        expected = "\033[1;33mtest\033[0m"
        self.assertEqual(result, expected)

        # Test underline with color and background
        result = charstyle.underline("test", color=charstyle.CYAN, bg=charstyle.BG_RED)
        expected = "\033[4;36;41mtest\033[0m"
        self.assertEqual(result, expected)

    def test_style_class(self):
        """Test the Style class."""
        # Create a style
        style = charstyle.Style(
            color=charstyle.MAGENTA, bg_color=charstyle.BG_WHITE, style=charstyle.BOLD
        )

        # Test apply method
        result = style.apply("test")
        expected = "\033[1;35;47mtest\033[0m"
        self.assertEqual(result, expected)

        # Test call method
        result = style("test")
        expected = "\033[1;35;47mtest\033[0m"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
