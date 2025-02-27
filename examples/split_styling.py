#!/usr/bin/env python3
"""
Simple examples of using the style_split function for different use cases.
"""

import sys

from charstyle import (
    BLUE,
    BOLD,
    BRIGHT_BLACK,
    BRIGHT_GREEN,
    BRIGHT_RED,
    CYAN,
    GREEN,
    ITALIC,
    NORMAL,
    RED,
    YELLOW,
    Style,
    style_split,
)


def main():
    """Demonstrate various ways to use style_split."""
    # Check if terminal supports colors
    if not sys.stdout.isatty():
        print("Your terminal does not support colors.")
        return

    print("\n=== Basic Split Styling Examples ===")

    # Simple key-value pair
    print("1. Basic key:value styling:")
    print(style_split("Status: OK", ":", BLUE, GREEN))

    # Error message
    print("\n2. Error message styling:")
    error_style = Style(color=RED, style=BOLD)
    print(style_split("Error: File not found", ":", error_style, ITALIC))

    # Configuration setting
    print("\n3. Configuration setting:")
    print(style_split("debug_mode = True", " = ", CYAN, YELLOW))

    # Command with arguments
    print("\n4. Command with arguments:")
    cmd_style = Style(color=BRIGHT_GREEN, style=BOLD)
    print(style_split("git commit -m 'Update README'", " ", cmd_style, NORMAL))

    # URL components
    print("\n5. URL components:")
    print(style_split("https://www.example.com/path?query=value", "://", GREEN, BLUE))

    # Multiple delimiters (chaining style_split calls)
    print("\n6. Multiple delimiters (nested):")
    inner_styled = style_split("name=John age=30", " ", NORMAL, NORMAL)

    key_style = Style(color=CYAN, style=BOLD)
    result = style_split(inner_styled, "=", key_style, YELLOW)
    print(result)

    # IP address
    print("\n7. IP address octets:")
    print(style_split("192.168.1.100", ".", RED, GREEN, BLUE, YELLOW))

    # Table row
    print("\n8. Table row with multiple columns:")
    name_style = Style(color=BRIGHT_GREEN)
    age_style = Style(color=YELLOW)
    job_style = Style(color=BRIGHT_BLACK, style=BOLD)
    print(style_split("John | 25 | Developer", " | ", name_style, age_style, job_style))

    # Date components
    print("\n9. Date components:")
    year_style = Style(color=BRIGHT_GREEN, style=BOLD)
    month_style = Style(color=YELLOW)
    day_style = Style(color=RED)
    print(style_split("2023-02-27", "-", year_style, month_style, day_style))

    # Log level
    print("\n10. Log level:")
    log_level_style = Style(color=BRIGHT_GREEN, style=BOLD)
    print(style_split("[INFO] User authentication: successful", "] ", log_level_style, NORMAL))


if __name__ == "__main__":
    main()
