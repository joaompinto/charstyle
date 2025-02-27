#!/usr/bin/env python3
"""
Practical examples demonstrating real-world applications of charstyle's complex styling.
"""

import random
import time
from datetime import datetime

import charstyle


def simulated_log_output():
    """Simulates a log output with different log levels styled appropriately."""
    print("\n=== Log Output Example ===")

    # Define log level styles
    debug_style = charstyle.Style(color=charstyle.BRIGHT_BLACK)
    info_style = charstyle.Style(color=charstyle.BRIGHT_BLUE)
    warning_style = charstyle.Style(color=charstyle.YELLOW)
    error_style = charstyle.Style(color=charstyle.BRIGHT_RED)
    critical_style = charstyle.Style(
        color=charstyle.BRIGHT_WHITE, bg_color=charstyle.BG_RED, style=charstyle.BOLD
    )

    timestamp_style = charstyle.Style(color=charstyle.BRIGHT_BLACK)

    # Simulated log entries
    log_entries = [
        ("DEBUG", "Initialized database connection", debug_style),
        ("INFO", "User 'admin' logged in successfully", info_style),
        ("WARNING", "High memory usage detected (85%)", warning_style),
        ("ERROR", "Failed to connect to API endpoint", error_style),
        ("CRITICAL", "Database connection lost, retrying...", critical_style),
        ("INFO", "Application started in development mode", info_style),
        ("DEBUG", "Processing request from 192.168.1.100", debug_style),
    ]

    # Display log entries with timestamp
    for level, message, style in log_entries:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

        # Using style_pattern_match with regex named groups
        pattern = r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) (?P<level>\w+) (?P<message>.*)"
        log_entry = f"{timestamp} {level} {message}"

        style_map = {
            "timestamp": timestamp_style,
            "level": style,
            "message": charstyle.Style(),  # Default style for message
        }

        print(charstyle.style_pattern_match(log_entry, pattern, style_map))
        time.sleep(0.5)  # Simulated time between log entries


def system_status_dashboard():
    """Displays a system status dashboard with styled components."""
    print("\n=== System Status Dashboard ===")

    # Define status indicators
    status_ok = charstyle.Style(color=charstyle.GREEN, style=charstyle.BOLD)
    status_warning = charstyle.Style(color=charstyle.YELLOW, style=charstyle.BOLD)
    status_error = charstyle.Style(color=charstyle.RED, style=charstyle.BOLD)
    status_unknown = charstyle.Style(color=charstyle.BRIGHT_BLACK, style=charstyle.ITALIC)

    # Component styles
    component_style = charstyle.Style(color=charstyle.CYAN)
    metric_style = charstyle.Style(color=charstyle.BRIGHT_BLACK)
    charstyle.Style(color=charstyle.WHITE)

    # System components and their status
    components = [
        ("Web Server", "Running", "CPU: 25%", "Memory: 512MB", status_ok),
        ("Database", "Running", "CPU: 65%", "Memory: 1.2GB", status_warning),
        ("Cache", "Stopped", "CPU: 0%", "Memory: 0MB", status_error),
        ("API Gateway", "Running", "CPU: 15%", "Memory: 256MB", status_ok),
        ("Job Queue", "Unknown", "CPU: --", "Memory: --", status_unknown),
    ]

    # Header
    header = "Component Status CPU Usage Memory Usage".split()
    col_widths = [20, 10, 15, 15]

    # Print header
    header_style = charstyle.Style(style=charstyle.BOLD)
    header_row = "".join(
        f"{header_style(h):<{w}}" for h, w in zip(header, col_widths, strict=False)
    )
    print(header_row)
    print("-" * 60)

    # Print components with styling
    for component, status, cpu, memory, status_style in components:
        # Style each component's row with complex styling
        row = f"{component_style(component):<20}{status_style(status):<10}{metric_style(cpu):<15}{metric_style(memory):<15}"
        print(row)

    print("-" * 60)
    footer = f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    print(charstyle.italic(footer))


def interactive_cli_menu():
    """Simulates an interactive CLI menu with styled options."""
    print("\n=== Interactive CLI Menu ===")

    # Define menu styles
    title_style = charstyle.Style(color=charstyle.BRIGHT_CYAN, style=charstyle.BOLD)
    option_number_style = charstyle.Style(color=charstyle.YELLOW, style=charstyle.BOLD)
    option_text_style = charstyle.Style(color=charstyle.WHITE)
    selected_style = charstyle.Style(bg_color=charstyle.BG_BLUE, style=charstyle.BOLD)

    # Menu options
    options = [
        "View records",
        "Add new record",
        "Edit existing record",
        "Delete record",
        "Export to CSV",
        "Import from CSV",
        "Settings",
        "Help",
        "Exit",
    ]

    # Display menu title
    print(title_style("\nMAIN MENU"))
    print(title_style("=" * 9))

    # Display menu options
    for i, option in enumerate(options, 1):
        # Randomly select an option to show as "selected" for demo purposes
        is_selected = i == random.randint(1, len(options))

        # Use style_format to style the different parts of the menu item
        if is_selected:
            print(
                charstyle.style_format(
                    " {num} │ {option} ",
                    num=(str(i), selected_style),
                    option=(option, selected_style),
                )
            )
        else:
            print(
                charstyle.style_format(
                    " {num} │ {option}",
                    num=(str(i), option_number_style),
                    option=(option, option_text_style),
                )
            )

    # Footer
    print("\n" + charstyle.italic("Use arrow keys to navigate, Enter to select"))


def network_request_trace():
    """Simulates a network request trace with styled components."""
    print("\n=== Network Request Trace ===")

    # Define styles for different parts of the trace
    method_styles = {
        "GET": charstyle.Style(color=charstyle.BLUE, style=charstyle.BOLD),
        "POST": charstyle.Style(color=charstyle.GREEN, style=charstyle.BOLD),
        "PUT": charstyle.Style(color=charstyle.YELLOW, style=charstyle.BOLD),
        "DELETE": charstyle.Style(color=charstyle.RED, style=charstyle.BOLD),
    }
    url_style = charstyle.Style(color=charstyle.CYAN)
    status_styles = {
        "2": charstyle.Style(color=charstyle.GREEN),  # 2xx codes
        "3": charstyle.Style(color=charstyle.YELLOW),  # 3xx codes
        "4": charstyle.Style(color=charstyle.RED),  # 4xx codes
        "5": charstyle.Style(color=charstyle.BRIGHT_RED, style=charstyle.BOLD),  # 5xx codes
    }
    time_style = charstyle.Style(color=charstyle.BRIGHT_BLACK)

    # Simulated network requests
    requests = [
        ("GET", "https://api.example.com/users", 200, 78),
        ("POST", "https://api.example.com/users/new", 201, 145),
        ("GET", "https://api.example.com/products", 404, 32),
        ("PUT", "https://api.example.com/users/5", 204, 103),
        ("DELETE", "https://api.example.com/posts/10", 500, 89),
        ("GET", "https://api.example.com/search?q=test", 200, 312),
        ("POST", "https://api.example.com/login", 401, 55),
    ]

    # Display requests
    for method, url, status, response_time in requests:
        # Get appropriate styles
        method_style = method_styles.get(method, charstyle.Style())
        status_style = status_styles.get(str(status)[0], charstyle.Style())

        # Format request line with complex styling
        request_line = f"{method} {url} {status} ({response_time}ms)"

        # Using style_complex with regex pattern to style different parts
        pattern = r"(\s|\s\d+\s|\s\(\d+ms\))"
        print(
            charstyle.style_complex(
                request_line,
                pattern,
                method_style,  # Method (GET, POST, etc.)
                url_style,  # URL
                status_style,  # Status code
                time_style,
            )
        )  # Response time

        time.sleep(0.3)  # Simulated delay between requests


def git_status_output():
    """Simulates a git status command output with styled components."""
    print("\n=== Git Status Output ===")

    # Define styles for different file statuses
    added_style = charstyle.Style(color=charstyle.GREEN)
    modified_style = charstyle.Style(color=charstyle.BLUE)
    deleted_style = charstyle.Style(color=charstyle.RED)
    untracked_style = charstyle.Style(color=charstyle.BRIGHT_BLACK)
    branch_style = charstyle.Style(color=charstyle.BRIGHT_GREEN, style=charstyle.BOLD)

    # Simulated git status output
    branch = "feature/new-styling"

    # Using style_format for the branch name line
    print(charstyle.style_format("On branch {branch}", branch=(branch, branch_style)))
    print()
    print("Changes to be committed:")
    print('  (use "git restore --staged <file>..." to unstage)')

    # Format each file status line with appropriate styling based on status
    staged_files = [
        ("new file", "README.md"),
        ("modified", "src/main.py"),
        ("deleted", "tests/old_test.py"),
    ]

    for status, filename in staged_files:
        status_style = (
            added_style
            if status == "new file"
            else modified_style if status == "modified" else deleted_style
        )

        # Using style_split to style the status and filename differently
        print(
            f"        {charstyle.style_split(f'{status}:    {filename}', ':', status_style, charstyle.Style())}"
        )

    print()
    print("Changes not staged for commit:")
    print('  (use "git add <file>..." to update what will be committed)')
    print('  (use "git restore <file>..." to discard changes in working directory)')

    unstaged_files = [("modified", "src/utils.py"), ("modified", "docs/README.md")]

    for status, filename in unstaged_files:
        # Style different parts of the line
        print(
            f"        {charstyle.style_split(f'{status}:    {filename}', ':', modified_style, charstyle.Style())}"
        )

    print()
    print("Untracked files:")
    print('  (use "git add <file>..." to include in what will be committed)')

    untracked_files = ["src/new_feature.py", "docs/new_feature.md", "tests/test_new_feature.py"]

    for filename in untracked_files:
        print(f"        {untracked_style(filename)}")


def main():
    """Run all practical examples."""
    # Check if terminal supports colors
    if not charstyle.supports_color():
        print("Your terminal does not support colors.")
        return

    simulated_log_output()
    system_status_dashboard()
    interactive_cli_menu()
    network_request_trace()
    git_status_output()

    print("\nAll examples completed.")


if __name__ == "__main__":
    main()
