"""
charstyle - A simple library for styling terminal text output using ANSI escape sequences.

This library provides functions to add color, background color, and text styles
(bold, italic, underline, etc.) to text output in terminal applications.

This module implements the enum-based styling approach.
"""

import os
import platform
import sys

# Import enum-based styles
from charstyle.styles import BackgroundColor, ForegroundColor, TextStyle

# ANSI escape sequence prefix
_ESC = "\033["
_END = "m"

# Text colors (constants)
BLACK = ForegroundColor.BLACK
RED = ForegroundColor.RED
GREEN = ForegroundColor.GREEN
YELLOW = ForegroundColor.YELLOW
BLUE = ForegroundColor.BLUE
MAGENTA = ForegroundColor.MAGENTA
CYAN = ForegroundColor.CYAN
WHITE = ForegroundColor.WHITE
BRIGHT_BLACK = ForegroundColor.BRIGHT_BLACK
BRIGHT_RED = ForegroundColor.BRIGHT_RED
BRIGHT_GREEN = ForegroundColor.BRIGHT_GREEN
BRIGHT_YELLOW = ForegroundColor.BRIGHT_YELLOW
BRIGHT_BLUE = ForegroundColor.BRIGHT_BLUE
BRIGHT_MAGENTA = ForegroundColor.BRIGHT_MAGENTA
BRIGHT_CYAN = ForegroundColor.BRIGHT_CYAN
BRIGHT_WHITE = ForegroundColor.BRIGHT_WHITE

# Background colors (constants)
BG_BLACK = BackgroundColor.BLACK
BG_RED = BackgroundColor.RED
BG_GREEN = BackgroundColor.GREEN
BG_YELLOW = BackgroundColor.YELLOW
BG_BLUE = BackgroundColor.BLUE
BG_MAGENTA = BackgroundColor.MAGENTA
BG_CYAN = BackgroundColor.CYAN
BG_WHITE = BackgroundColor.WHITE
BG_BRIGHT_BLACK = BackgroundColor.BRIGHT_BLACK
BG_BRIGHT_RED = BackgroundColor.BRIGHT_RED
BG_BRIGHT_GREEN = BackgroundColor.BRIGHT_GREEN
BG_BRIGHT_YELLOW = BackgroundColor.BRIGHT_YELLOW
BG_BRIGHT_BLUE = BackgroundColor.BRIGHT_BLUE
BG_BRIGHT_MAGENTA = BackgroundColor.BRIGHT_MAGENTA
BG_BRIGHT_CYAN = BackgroundColor.BRIGHT_CYAN
BG_BRIGHT_WHITE = BackgroundColor.BRIGHT_WHITE

# Text styles (constants)
NORMAL = TextStyle.NORMAL
BOLD = TextStyle.BOLD
DIM = TextStyle.DIM
ITALIC = TextStyle.ITALIC
UNDERLINE = TextStyle.UNDERLINE
BLINK = TextStyle.BLINK
REVERSE = TextStyle.REVERSE
HIDDEN = TextStyle.HIDDEN
STRIKETHROUGH = TextStyle.STRIKE


def colored(
    text: str,
    color: ForegroundColor | None = None,
    bg_color: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """
    Apply color, background color, and/or style to text.

    Args:
        text (str): The text to style
        color (ForegroundColor, optional): Text color enum
        bg_color (BackgroundColor, optional): Background color enum
        style (TextStyle, tuple, or str, optional): Text style enum, a tuple of TextStyle enums,
            or a combined style string with semicolons

    Returns:
        str: The styled text
    """
    if not supports_color():
        return text

    styles = []

    if style:
        if isinstance(style, tuple):
            # Handle tuple of styles
            style = ";".join(map(str, style))
        styles.append(style)
    if color:
        styles.append(color)
    if bg_color:
        styles.append(bg_color)

    if not styles:
        return text

    # Join styles with semicolons
    style_str = ";".join(map(str, styles))
    return f"{_ESC}{style_str}{_END}{text}{_ESC}0{_END}"


# Color convenience functions
def black(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply black color to text."""
    return colored(text, BLACK, bg, style)


def red(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply red color to text."""
    return colored(text, RED, bg, style)


def green(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply green color to text."""
    return colored(text, GREEN, bg, style)


def yellow(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply yellow color to text."""
    return colored(text, YELLOW, bg, style)


def blue(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply blue color to text."""
    return colored(text, BLUE, bg, style)


def magenta(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply magenta color to text."""
    return colored(text, MAGENTA, bg, style)


def cyan(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply cyan color to text."""
    return colored(text, CYAN, bg, style)


def white(
    text: str,
    bg: BackgroundColor | None = None,
    style: TextStyle | tuple[TextStyle, ...] | str | None = None,
) -> str:
    """Apply white color to text."""
    return colored(text, WHITE, bg, style)


# Style convenience functions
def bold(text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None) -> str:
    """Apply bold style to text."""
    return colored(text, color, bg, BOLD)


def dim(text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None) -> str:
    """Apply dim style to text."""
    return colored(text, color, bg, DIM)


def italic(
    text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None
) -> str:
    """Apply italic style to text."""
    return colored(text, color, bg, ITALIC)


def underline(
    text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None
) -> str:
    """Apply underline style to text."""
    return colored(text, color, bg, UNDERLINE)


def blink(
    text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None
) -> str:
    """Apply blink style to text."""
    return colored(text, color, bg, BLINK)


def reverse(
    text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None
) -> str:
    """Apply reverse style to text."""
    return colored(text, color, bg, REVERSE)


def hidden(
    text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None
) -> str:
    """Apply hidden style to text."""
    return colored(text, color, bg, HIDDEN)


def strikethrough(
    text: str, color: ForegroundColor | None = None, bg: BackgroundColor | None = None
) -> str:
    """Apply strikethrough style to text."""
    return colored(text, color, bg, STRIKETHROUGH)


class Style:
    """A class for creating and applying custom text styles."""

    def __init__(
        self,
        color: ForegroundColor | None = None,
        bg_color: BackgroundColor | None = None,
        style: TextStyle | tuple[TextStyle, ...] | str | None = None,
    ) -> None:
        """
        Initialize a Style instance.

        Args:
            color (ForegroundColor, optional): Text color enum
            bg_color (BackgroundColor, optional): Background color enum
            style (TextStyle, tuple, or str, optional): Text style enum, a tuple of TextStyle enums,
                or a combined style string with semicolons
        """
        self.color = color
        self.bg_color = bg_color
        self.style: str | None = None

        # Handle tuple of styles
        if isinstance(style, tuple):
            self.style = ";".join(map(str, style))
        else:
            self.style = style

    def apply(self, text: str) -> str:
        """
        Apply this style to the given text.

        Args:
            text (str): The text to style

        Returns:
            str: The styled text
        """
        return colored(text, self.color, self.bg_color, self.style)

    def __call__(self, text: str) -> str:
        """
        Apply this style to the given text (callable shorthand).

        Args:
            text (str): The text to style

        Returns:
            str: The styled text
        """
        return self.apply(text)


def supports_color() -> bool:
    """
    Check if the current terminal supports colors.

    Returns:
        bool: True if the terminal supports colors, False otherwise
    """
    if os.environ.get("FORCE_COLOR", "0") == "1":
        return True

    if os.environ.get("NO_COLOR") is not None:
        return False

    if os.environ.get("TERM") == "dumb":
        return False

    # Check if running in a known terminal that supports colors
    plat = platform.system()
    if plat == "Windows":
        # Windows 10 build 14931+ supports ANSI colors in cmd.exe
        # Check if running in Windows Terminal, VSCode integrated terminal, or similar
        if os.environ.get("WT_SESSION") is not None:
            return True
        if os.environ.get("TERM_PROGRAM") is not None:
            return True
        try:
            # Check Windows version - crude but effective
            major, minor, build = platform.version().split(".")
            if int(build) >= 14931:
                return True
        except (ValueError, AttributeError):
            pass
    elif plat in ("Linux", "Darwin", "FreeBSD"):
        # Most Unix-like terminals support colors
        if sys.stdout.isatty():
            return True

    # Default to no color support
    return False
