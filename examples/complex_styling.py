#!/usr/bin/env python3
"""
Example script demonstrating complex string styling in charstyle.
"""

from charstyle import (
    BOLD, ITALIC, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE,
    BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_BLUE, BG_BLUE,
    colored, style_split, style_complex, style_pattern_match, style_format,
    supports_color
)


def main():
    """
    Demonstrate the complex styling features.
    """
    # Check if terminal supports colors
    if not supports_color():
        print("Your terminal does not support colors.")
        return

    print("\n=== Basic Split Styling ===")
    # Style a "key: value" pair with different styles
    print(style_split("Status: OK", ":", BOLD, GREEN))
    print(
        style_split(
            "Error: File not found",
            ":",
            (RED, BOLD),  # Using a tuple of styles
            ITALIC,
        )
    )

    # Multiple delimiters with three styles
    print(style_split("Name: John Doe (Developer)", ":", CYAN, BOLD))

    print("\n=== Complex Pattern Styling ===")
    # Style with regular expression pattern
    print(
        style_complex(
            "Status: OK (processed)",
            r"(: |\()",
            BLUE,  # "Status"
            GREEN,  # "OK "
            YELLOW,
        )
    )  # "processed)"

    # Log entry styling
    print(
        style_complex(
            "[INFO] User login: admin",
            r"(\[|\] |\: )",
            CYAN,  # "INFO"
            MAGENTA,  # "User login"
            GREEN,
        )
    )  # "admin"

    # Server configuration
    print(
        style_complex(
            "Server=production; Port=8080; Active=true",
            r"(=|; )",
            (BLUE, BOLD),  # "Server"
            GREEN,  # "production"
            (BLUE, BOLD),  # "Port"
            YELLOW,  # "8080"
            (BLUE, BOLD),  # "Active"
            RED,
        )
    )  # "true"

    print("\n=== Pattern Matching with Named Groups ===")
    pattern = r"(?P<code>\d{3}) (?P<status>\w+) - (?P<message>.*)"
    style_map = {
        "code": (BRIGHT_RED, BOLD),
        "status": RED,
        "message": YELLOW,
    }
    print(
        style_pattern_match(
            "404 NotFound - The requested resource does not exist", pattern, style_map
        )
    )

    pattern = r"(?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+): (?P<message>.*)"
    style_map = {
        "time": BRIGHT_BLACK,
        "level": (GREEN, BOLD),
        "message": WHITE,
    }
    print(
        style_pattern_match(
            "14:25:36 INFO: User authentication successful", pattern, style_map
        )
    )

    print("\n=== Format-based Styling ===")
    # Format with positional arguments
    print(
        style_format("{} = {}", ("username", BLUE), ("admin", GREEN))
    )

    # Format with keyword arguments
    print(
        style_format(
            "HTTP/{version} {code} {status}",
            version=("1.1", BRIGHT_BLACK),
            code=("200", GREEN),
            status=("OK", (GREEN, BOLD)),
        )
    )

    # Command line example
    print(
        style_format(
            "{command} {arg1} {arg2}",
            command=("git", (RED, BOLD)),
            arg1=("commit", YELLOW),
            arg2=("-m", BLUE),
        )
    )


if __name__ == "__main__":
    main()
