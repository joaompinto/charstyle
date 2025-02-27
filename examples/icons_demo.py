#!/usr/bin/env python3
"""
Example of using the charstyle Icon enum.
This demonstrates how to use terminal icons for status indicators, progress bars,
and simple UI elements.
"""

from charstyle import Icon, blue, bold, green, red, yellow


def main():
    """Main demo function."""
    print("\n=== charstyle Icons Demo ===\n")

    # Status indicators
    print(bold("Status Indicators:"))
    print(f"{green(Icon.CHECK)} {bold('Success:')} Operation completed")
    print(f"{red(Icon.CROSS)} {bold('Error:')} File not found")
    print(f"{yellow(Icon.WARNING)} {bold('Warning:')} Disk space is low")
    print(f"{blue(Icon.INFO)} {bold('Info:')} System is running normally")
    print()

    # Progress indicator
    print(bold("Progress Bar:"))
    progress = 7  # Out of 10
    bar = f"{Icon.BLOCK * progress}{Icon.LIGHT_SHADE * (10 - progress)}"
    print(f"Loading: [{green(bar)}] {progress * 10}%")
    print()

    # Simple box drawing
    print(bold("Box Drawing:"))
    title = "WELCOME"
    padding = 2
    width = len(title) + padding * 2

    print(f"{Icon.TOP_LEFT}{Icon.H_LINE * width}{Icon.TOP_RIGHT}")
    print(f"{Icon.V_LINE}{' ' * padding}{title}{' ' * padding}{Icon.V_LINE}")
    print(f"{Icon.BOTTOM_LEFT}{Icon.H_LINE * width}{Icon.BOTTOM_RIGHT}")
    print()

    # Menu example
    print(bold("Menu Example:"))
    print(f"{Icon.CIRCLE} {bold('Menu Item 1')}")
    print(f"{Icon.CIRCLE} {bold('Menu Item 2')}")
    print(f"{Icon.TRIANGLE} {bold(green('Selected Item'))}")
    print(f"{Icon.CIRCLE} {bold('Menu Item 4')}")
    print()

    # Table
    print(bold("Simple Table:"))
    print(f"{Icon.TOP_LEFT}{Icon.H_LINE * 12}{Icon.TOP_RIGHT}{Icon.H_LINE * 10}{Icon.TOP_RIGHT}")
    print(f"{Icon.V_LINE} {bold('Name')}      {Icon.V_LINE} {bold('Value')}  {Icon.V_LINE}")
    print(f"{Icon.V_LINE} Item 1     {Icon.V_LINE} 42      {Icon.V_LINE}")
    print(f"{Icon.V_LINE} Item 2     {Icon.V_LINE} 73      {Icon.V_LINE}")
    print(
        f"{Icon.BOTTOM_LEFT}{Icon.H_LINE * 12}{Icon.BOTTOM_RIGHT}{Icon.H_LINE * 10}{Icon.BOTTOM_RIGHT}"
    )

    # Mood indicators
    print("\n" + bold("Mood Indicators:"))
    print(f"{Icon.SMILE} {bold('Happy')}")
    print(f"{Icon.FROWN} {bold('Sad')}")
    print(f"{Icon.THUMBS_UP} {bold('Approved')}")
    print(f"{Icon.THUMBS_DOWN} {bold('Rejected')}")
    print(f"{Icon.FIRE} {red(bold('Hot'))}")
    print(f"{Icon.CLAP} {yellow(bold('Congratulations'))}")
    print()


if __name__ == "__main__":
    main()
