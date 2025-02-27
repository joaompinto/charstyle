#!/usr/bin/env python3
"""
Examples demonstrating how to combine multiple styles in charstyle.
"""

from charstyle import (
    BG_BLACK,
    BLINK,
    BLUE,
    BOLD,
    BRIGHT_GREEN,
    BRIGHT_RED,
    ITALIC,
    RED,
    UNDERLINE,
    YELLOW,
    Style,
    bold,
    colored,
    italic,
    red,
    supports_color,
    underline,
)


def main():
    """Demonstrate various ways to combine styles in charstyle."""
    # Check if terminal supports colors
    if not supports_color():
        print("Your terminal does not support colors.")
        return

    print("\n=== Combining Multiple Text Styles ===")

    # Method 1: Using the style parameter with concatenated styles
    print("\n1. Using the style parameter with concatenated styles:")
    print(colored("Bold and Italic", style=BOLD + ";" + ITALIC))
    print(colored("Bold, Italic and Underlined", style=BOLD + ";" + ITALIC + ";" + UNDERLINE))

    # Method 2: Nesting style functions
    print("\n2. Nesting style functions:")
    print(bold(italic("Bold and Italic (nested)")))
    print(bold(italic(underline("Bold, Italic and Underlined (nested)"))))

    # Method 3: Using the Style class
    print("\n3. Using the Style class:")
    bold_italic = Style(style=BOLD + ";" + ITALIC)
    bold_italic_underline = Style(style=BOLD + ";" + ITALIC + ";" + UNDERLINE)

    print(bold_italic("Bold and Italic (Style class)"))
    print(bold_italic_underline("Bold, Italic and Underlined (Style class)"))

    # Method 4: Combining with colors
    print("\n4. Combining styles with colors:")

    # Using the colored function
    print(colored("Bold red italic", color=RED, style=BOLD + ";" + ITALIC))

    # Using style functions with parameters
    print(bold("Bold blue italic", color=BLUE, bg=None))

    # Nesting with multiple styles and colors
    print(bold(italic(red("Red bold italic (nested)"))))

    # Using Style class with colors and styles
    fancy_style = Style(color=BRIGHT_GREEN, bg_color=BG_BLACK, style=BOLD + ";" + UNDERLINE)
    print(fancy_style("Bold underlined bright green text on black background"))

    # Method 5: Creating reusable combined style functions
    print("\n5. Creating reusable combined style functions:")

    def bold_italic_text(text, color=None, bg=None):
        """Apply bold and italic styles to text."""
        return colored(text, color, bg, BOLD + ";" + ITALIC)

    def warning_text(text):
        """Create a standardized warning style."""
        return colored(text, YELLOW, None, BOLD + ";" + UNDERLINE)

    def error_text(text):
        """Create a standardized error style."""
        return colored(text, BRIGHT_RED, BG_BLACK, BOLD + ";" + BLINK)

    print(bold_italic_text("Custom bold italic function"))
    print(bold_italic_text("Custom bold italic cyan", color=BLUE))
    print(warning_text("Warning: This is a standardized warning style"))
    print(error_text("Error: This is a standardized error style"))


if __name__ == "__main__":
    main()
