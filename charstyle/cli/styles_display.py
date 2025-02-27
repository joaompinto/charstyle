"""
Style display functionality for charstyle CLI.
This module provides functions to display terminal styles.
"""


def show_styles() -> None:
    """Display all available terminal styles."""
    from charstyle import (
        BG_BLACK,
        BG_BLUE,
        BG_BRIGHT_BLACK,
        BG_BRIGHT_BLUE,
        BG_BRIGHT_CYAN,
        BG_BRIGHT_GREEN,
        BG_BRIGHT_MAGENTA,
        BG_BRIGHT_RED,
        BG_BRIGHT_WHITE,
        BG_BRIGHT_YELLOW,
        BG_CYAN,
        BG_GREEN,
        BG_MAGENTA,
        BG_RED,
        BG_WHITE,
        BG_YELLOW,
        BLACK,
        BLINK,
        BLUE,
        BOLD,
        BRIGHT_BLACK,
        BRIGHT_BLUE,
        BRIGHT_CYAN,
        BRIGHT_GREEN,
        BRIGHT_MAGENTA,
        BRIGHT_RED,
        BRIGHT_WHITE,
        BRIGHT_YELLOW,
        CYAN,
        DIM,
        GREEN,
        ITALIC,
        MAGENTA,
        RED,
        REVERSE,
        STRIKETHROUGH,
        UNDERLINE,
        WHITE,
        YELLOW,
        Style,
        colored,
        supports_color,
    )

    # Create style functions
    def bold(text: str) -> str:
        return colored(text, style=BOLD)

    def red(text: str) -> str:
        return colored(text, color=RED)

    def green(text: str) -> str:
        return colored(text, color=GREEN)

    def blue(text: str) -> str:
        return colored(text, color=BLUE)

    def yellow(text: str) -> str:
        return colored(text, color=YELLOW)

    def underline(text: str) -> str:
        return colored(text, style=UNDERLINE)

    print("\n=== Charstyle Demo ===")
    print("A library for styling terminal text using ANSI escape sequences")
    print()

    # Check if terminal supports colors
    if not supports_color():
        print("Your terminal does not support colors.")
        exit(1)

    print("=== Text Colors ===")
    colors = [
        ("BLACK", BLACK, "BRIGHT_BLACK", BRIGHT_BLACK),
        ("RED", RED, "BRIGHT_RED", BRIGHT_RED),
        ("GREEN", GREEN, "BRIGHT_GREEN", BRIGHT_GREEN),
        ("YELLOW", YELLOW, "BRIGHT_YELLOW", BRIGHT_YELLOW),
        ("BLUE", BLUE, "BRIGHT_BLUE", BRIGHT_BLUE),
        ("MAGENTA", MAGENTA, "BRIGHT_MAGENTA", BRIGHT_MAGENTA),
        ("CYAN", CYAN, "BRIGHT_CYAN", BRIGHT_CYAN),
        ("WHITE", WHITE, "BRIGHT_WHITE", BRIGHT_WHITE),
    ]

    for name, color, bright_name, bright_color in colors:
        regular_text = f"{name:<15}: {colored('This text is ' + name.lower(), color)}"
        bright_text = f"{bright_name:<15}: {colored('This text is bright ' + bright_name.split('_')[1].lower(), bright_color)}"
        print(f"{regular_text:<60} {bright_text}")

    print("\n=== Background Colors ===")
    bg_colors = [
        ("BG_BLACK", BG_BLACK, "BG_BRIGHT_BLACK", BG_BRIGHT_BLACK),
        ("BG_RED", BG_RED, "BG_BRIGHT_RED", BG_BRIGHT_RED),
        ("BG_GREEN", BG_GREEN, "BG_BRIGHT_GREEN", BG_BRIGHT_GREEN),
        ("BG_YELLOW", BG_YELLOW, "BG_BRIGHT_YELLOW", BG_BRIGHT_YELLOW),
        ("BG_BLUE", BG_BLUE, "BG_BRIGHT_BLUE", BG_BRIGHT_BLUE),
        ("BG_MAGENTA", BG_MAGENTA, "BG_BRIGHT_MAGENTA", BG_BRIGHT_MAGENTA),
        ("BG_CYAN", BG_CYAN, "BG_BRIGHT_CYAN", BG_BRIGHT_CYAN),
        ("BG_WHITE", BG_WHITE, "BG_BRIGHT_WHITE", BG_BRIGHT_WHITE),
    ]

    # Find the longest text for padding
    longest_regular_text = "This background is magenta"
    longest_bright_text = "This background is bright magenta"
    
    for name, bg_color, bright_name, bright_bg_color in bg_colors:
        regular_text = f"This background is {name.split('_')[1].lower()}"
        regular_text = regular_text.ljust(len(longest_regular_text))
        
        bright_text = f"This background is bright {bright_name.split('_')[2].lower()}"
        bright_text = bright_text.ljust(len(longest_bright_text))
        
        regular_bg = f"{name:<15}: {colored(regular_text, bg_color=bg_color)}"
        bright_bg = f"{bright_name:<20}: {colored(bright_text, bg_color=bright_bg_color)}"
        
        print(f"{regular_bg:<60} {bright_bg}")

    print("\n=== Text Styles ===")
    styles = [
        ("BOLD", BOLD),
        ("DIM", DIM),
        ("ITALIC", ITALIC),
        ("UNDERLINE", UNDERLINE),
        ("BLINK", BLINK),
        ("REVERSE", REVERSE),
        ("STRIKETHROUGH", STRIKETHROUGH),
    ]

    for name, style in styles:
        print(f"{name}: {colored('This text is ' + name.lower(), style=style)}")

    print("\n=== Combined Styles ===")
    print(f"BOLD + RED: {bold(red('Bold and red text'))}")
    print(
        f"UNDERLINE + GREEN + BG_YELLOW: {underline(colored('Underlined green text on yellow background', GREEN, BG_YELLOW))}"
    )

    # Style class example
    print("\n=== Style Class ===")
    error_style = Style(color=RED, bg_color=BG_BLACK, style=BOLD)
    print(f"Error style: {error_style('This is an error message')}")

    success_style = Style(color=GREEN, style=BOLD)
    print(f"Success style: {success_style('This is a success message')}")

    # Add a tip about the --icons option
    print(f"\nTip: Run {bold(blue('python -m charstyle --icons'))} to view a collection of fancy terminal icons!")
