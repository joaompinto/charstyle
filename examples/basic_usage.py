#!/usr/bin/env python3
"""
Example script demonstrating the basic usage of the charstyle library.
"""

import charstyle
from charstyle import BackgroundColor, ForegroundColor, Style, TextStyle, colored, supports_color


def main():
    """
    Demonstrate basic charstyle features using the enum-based approach.
    """
    # Check if terminal supports colors
    if not supports_color():
        print("Your terminal does not support colors.")
        return

    print("\n=== Basic Colors ===")
    # Using convenience functions
    print(charstyle.red("Red text"))
    print(charstyle.green("Green text"))
    print(charstyle.blue("Blue text"))

    # Using direct enum values with colored()
    print(colored("Yellow text", color=ForegroundColor.YELLOW))
    print(colored("Magenta text", color=ForegroundColor.MAGENTA))
    print(colored("Cyan text", color=ForegroundColor.CYAN))

    print("\n=== Bright Colors ===")
    print(colored("Bright Red", color=ForegroundColor.BRIGHT_RED))
    print(colored("Bright Green", color=ForegroundColor.BRIGHT_GREEN))
    print(colored("Bright Blue", color=ForegroundColor.BRIGHT_BLUE))

    print("\n=== Text Styles ===")
    # Using convenience functions
    print(charstyle.bold("Bold text"))
    print(charstyle.italic("Italic text"))
    print(charstyle.underline("Underlined text"))

    # Using direct enum values
    print(colored("Dim text", style=TextStyle.DIM))
    print(colored("Reversed text", style=TextStyle.REVERSE))
    print(colored("Strikethrough text", style=TextStyle.STRIKE))

    print("\n=== Background Colors ===")
    print(colored("Red background", bg_color=BackgroundColor.RED))
    print(colored("Green background", bg_color=BackgroundColor.GREEN))
    print(colored("Blue background", bg_color=BackgroundColor.BLUE))
    print(colored("Yellow background", bg_color=BackgroundColor.YELLOW))

    print("\n=== Combining Styles ===")
    # Combining styles and colors with colored()
    print(colored("Bold red text", color=ForegroundColor.RED, style=TextStyle.BOLD))

    # Combining directly with colored()
    print(colored("Bold blue text", color=ForegroundColor.BLUE, style=TextStyle.BOLD))

    # Using multiple styles with a tuple
    print(colored("Bold and italic text", style=(TextStyle.BOLD, TextStyle.ITALIC)))

    # Text and background colors
    print(
        colored(
            "White text on blue background",
            color=ForegroundColor.WHITE,
            bg_color=BackgroundColor.BLUE,
        )
    )

    print("\n=== Custom Styles ===")
    # Creating reusable style objects
    error_style = Style(color=ForegroundColor.BRIGHT_RED, style=TextStyle.BOLD)

    warning_style = Style(
        color=ForegroundColor.YELLOW, bg_color=BackgroundColor.BLACK, style=TextStyle.BOLD
    )

    success_style = Style(color=ForegroundColor.GREEN, style=TextStyle.BOLD)

    print(error_style("ERROR: Operation failed!"))
    print(warning_style("WARNING: Proceed with caution!"))
    print(success_style("SUCCESS: Operation completed!"))


if __name__ == "__main__":
    main()
