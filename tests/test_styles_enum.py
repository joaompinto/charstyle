#!/usr/bin/env python3
"""
Unit tests for the StrEnum-based styles in charstyle.
"""

import unittest

from charstyle import Style, colored
from charstyle.styles import BackgroundColor, ForegroundColor, TextStyle

# NOTE: The order of ANSI style codes is important in these tests.
# The implementation combines styles in the following order:
# 1. Style codes (TextStyle.BOLD, etc.) are applied first
# 2. Color codes (ForegroundColor.RED, etc.) are applied second
# 3. Background color codes (BackgroundColor.RED, etc.) are applied last
# This results in strings like "\033[1;31;44mtext\033[0m" (bold, red text on blue background)


class TestStyleEnums(unittest.TestCase):
    """Test cases for StrEnum-based styles."""

    def test_foreground_color_enum(self):
        """Test using ForegroundColor enum."""
        # Test basic color
        result = colored("test", color=ForegroundColor.RED)
        expected = "\033[31mtest\033[0m"
        self.assertEqual(result, expected)

        # Test bright color
        result = colored("test", color=ForegroundColor.BRIGHT_GREEN)
        expected = "\033[92mtest\033[0m"
        self.assertEqual(result, expected)

    def test_background_color_enum(self):
        """Test using BackgroundColor enum."""
        # Test basic background color
        result = colored("test", bg_color=BackgroundColor.BLUE)
        expected = "\033[44mtest\033[0m"
        self.assertEqual(result, expected)

        # Test bright background color
        result = colored("test", bg_color=BackgroundColor.BRIGHT_YELLOW)
        expected = "\033[103mtest\033[0m"
        self.assertEqual(result, expected)

    def test_text_style_enum(self):
        """Test using TextStyle enum."""
        # Test basic text style
        result = colored("test", style=TextStyle.BOLD)
        expected = "\033[1mtest\033[0m"
        self.assertEqual(result, expected)

        # Test another text style
        result = colored("test", style=TextStyle.ITALIC)
        expected = "\033[3mtest\033[0m"
        self.assertEqual(result, expected)

    def test_combining_style_enums(self):
        """Test combining multiple style enums."""
        # Combine two text styles
        combined_style = TextStyle.BOLD + ";" + TextStyle.ITALIC
        result = colored("test", style=combined_style)

        # Verify components rather than exact string format
        self.assertIn(TextStyle.BOLD, result)
        self.assertIn(TextStyle.ITALIC, result)
        self.assertIn("test", result)
        self.assertTrue(result.startswith("\033["))
        self.assertTrue(result.endswith("\033[0m"))

        # Combine text style with colors
        result = colored(
            "test",
            color=ForegroundColor.RED,
            bg_color=BackgroundColor.WHITE,
            style=TextStyle.UNDERLINE,
        )

        # Verify components
        self.assertIn(ForegroundColor.RED, result)
        self.assertIn(BackgroundColor.WHITE, result)
        self.assertIn(TextStyle.UNDERLINE, result)
        self.assertIn("test", result)

        # Triple style combination
        triple_style = TextStyle.BOLD + ";" + TextStyle.ITALIC + ";" + TextStyle.UNDERLINE
        result = colored("test", style=triple_style)

        # Verify components
        self.assertIn(TextStyle.BOLD, result)
        self.assertIn(TextStyle.ITALIC, result)
        self.assertIn(TextStyle.UNDERLINE, result)
        self.assertIn("test", result)

    def test_style_class_with_enums(self):
        """Test Style class with enum values."""
        # Create a style with enums
        style = Style(
            color=ForegroundColor.MAGENTA, bg_color=BackgroundColor.BLACK, style=TextStyle.BOLD
        )

        # Test apply method
        result = style.apply("test")
        # Note: The order of style codes can vary, so we verify the components
        self.assertIn(ForegroundColor.MAGENTA, result)
        self.assertIn(BackgroundColor.BLACK, result)
        self.assertIn(TextStyle.BOLD, result)
        self.assertIn("test", result)
        self.assertTrue(result.startswith("\033["))
        self.assertTrue(result.endswith("\033[0m"))

        # Style with multiple text styles
        combined_style = Style(
            color=ForegroundColor.GREEN, style=TextStyle.BOLD + ";" + TextStyle.UNDERLINE
        )
        result = combined_style("test")
        # Verify components rather than exact string
        self.assertIn(ForegroundColor.GREEN, result)
        self.assertIn(TextStyle.BOLD, result)
        self.assertIn(TextStyle.UNDERLINE, result)
        self.assertIn("test", result)
        self.assertTrue(result.startswith("\033["))
        self.assertTrue(result.endswith("\033[0m"))

    def test_enum_string_conversion(self):
        """Test string behavior of StrEnum values."""
        # Verify enums behave like strings in string operations
        self.assertEqual(ForegroundColor.RED + "test", "31test")
        self.assertEqual("color:" + BackgroundColor.BLUE, "color:44")
        self.assertEqual(f"style={TextStyle.BOLD}", "style=1")


if __name__ == "__main__":
    unittest.main()
