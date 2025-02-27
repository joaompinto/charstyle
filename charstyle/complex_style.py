"""
Complex string styling utilities for charstyle.

This module provides functions for styling complex strings with multiple components
using patterns and styles.
"""

import re
from re import Pattern
from typing import Any

# Import directly from charstyle.charstyle to avoid circular imports
from charstyle.charstyle import colored
from charstyle.styles import BackgroundColor, ForegroundColor, TextStyle

StyleType = ForegroundColor | BackgroundColor | TextStyle | tuple[TextStyle, ...]


def style_split(text: str, delimiter: str, *styles: StyleType) -> str:
    """
    Split text by a delimiter and apply different styles to each part.

    Args:
        text (str): The text to style
        delimiter (str): The delimiter to split on
        *styles: Variable number of style constants to apply to each part

    Returns:
        str: The styled text

    Example:
        >>> from charstyle import RED, GREEN, BLUE
        >>> style_split("Status: OK", ":", RED, GREEN)
        # This returns "Status" in red and " OK" in green
    """
    parts = text.split(delimiter, len(styles) - 1)
    styled_parts = []

    for i, part in enumerate(parts):
        if i < len(styles):
            styled_parts.append(colored(part, style=styles[i]))
        else:
            styled_parts.append(part)

    # Join with the delimiter
    return delimiter.join(styled_parts)


def style_complex(text: str, pattern: str | Pattern, *styles: StyleType) -> str:
    """
    Style text by splitting it with a regex pattern and applying different styles to each part.

    Args:
        text (str): The text to style
        pattern (str): Regular expression pattern to split on
        *styles: Variable number of style constants to apply to each part

    Returns:
        str: The styled text

    Example:
        >>> from charstyle import RED, GREEN, YELLOW
        >>> # Style "Status: OK (processed)" with different styles
        >>> style_complex("Status: OK (processed)", "(: | \\()", BLUE, GREEN, YELLOW)
        # This returns "Status" in blue, "OK " in green, and "processed)" in yellow
    """
    parts = re.split(pattern, text)
    result = []

    # Filter out None values that re.split might return
    parts = [p for p in parts if p is not None]

    # Process parts and apply styles
    for i in range(len(parts)):
        if i < len(styles):
            result.append(colored(parts[i], style=styles[i]))
        else:
            result.append(parts[i])

    return "".join(result)


def style_pattern_match(text: str, pattern: str | Pattern, style_map: dict[str, StyleType]) -> str:
    """
    Apply styles to parts of text that match named groups in a regex pattern.

    Args:
        text (str): The text to style
        pattern (str): Regular expression pattern with named groups
        style_map (dict): Mapping from group names to style constants

    Returns:
        str: The styled text

    Example:
        >>> from charstyle import RED, GREEN, BLUE
        >>> # Example of pattern matching with named groups
        >>> pattern = r"(?P<key>[a-z]+)=(?P<value>[a-z]+)"
        >>> style_map = {"key": BLUE, "value": GREEN}
        >>> style_pattern_match("user=admin", pattern, style_map)
        # This returns "user" in blue, "=" unchanged, and "admin" in green
    """
    match = re.match(pattern, text)
    if not match:
        return text

    result = text
    for name, style in style_map.items():
        if name in match.groupdict():
            span = match.span(name)
            # Replace the matched group with its styled version
            old_text = text[span[0] : span[1]]
            new_text = colored(old_text, style=style)
            result = result.replace(old_text, new_text, 1)

    return result


def style_format(template: str, *args: Any, **kwargs: Any) -> str:
    """
    Apply styles to a template string using format-style placeholders.

    Args:
        template (str): Template string with {} placeholders
        *args: Positional arguments to format, can be (text, style) tuples
        **kwargs: Keyword arguments to format, can be (text, style) tuples

    Returns:
        str: The styled text

    Example:
        >>> from charstyle import RED, GREEN
        >>> style_format("{} = {}", ("name", RED), ("value", GREEN))
        # This returns "name" in red and "value" in green
        >>> style_format("{key} = {value}", key=("name", RED), value=("value", GREEN))
        # Same result with keyword arguments
    """
    # Process positional arguments
    formatted_args = []
    for arg in args:
        if isinstance(arg, tuple) and len(arg) == 2:
            text, style = arg
            formatted_args.append(colored(text, style=style))
        else:
            formatted_args.append(arg)

    # Process keyword arguments
    formatted_kwargs = {}
    for key, value in kwargs.items():
        if isinstance(value, tuple) and len(value) == 2:
            text, style = value
            formatted_kwargs[key] = colored(text, style=style)
        else:
            formatted_kwargs[key] = value

    # Format the template with processed arguments
    return template.format(*formatted_args, **formatted_kwargs)
