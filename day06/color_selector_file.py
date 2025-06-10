import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
color_file_path = os.path.join(script_dir, "colors.txt")
output_file_path = os.path.join(script_dir, "selected_colors.txt")

# Read available colors from colors.txt
try:
    with open(color_file_path, "r") as f:
        colors = [line.strip().lower() for line in f if line.strip()]
except FileNotFoundError:
    print("Error: 'colors.txt' not found.")
    sys.exit(1)

selected_colors = []

# Command-line mode
if len(sys.argv) > 1:
    args = sys.argv[1:]
    for arg in args:
        if arg.isdigit():
            index = int(arg) - 1  
            if 0 <= index < len(colors):
                selected_colors.append(colors[index])
            else:
                print(f"Error: Index {arg} is out of range.")
                sys.exit(1)
        else:
            arg_lower = arg.lower()
            if arg_lower in colors:
                selected_colors.append(arg_lower)
            else:
                print(f"Error: '{arg}' is not a valid color name.")
                sys.exit(1)

# Interactive mode
else:
    print("Choose one or more colors (by number or name):")
    for i, color in enumerate(colors, start=1):
        print(f"{i}: {color}")

    while True:
        input_str = input("Enter your colors (e.g. 1 2 blue red): ")
        entries = input_str.strip().split()
        temp_selection = []
        valid = True
        for entry in entries:
            if entry.isdigit():
                index = int(entry) - 1  
                if 0 <= index < len(colors):
                    temp_selection.append(colors[index])
                else:
                    print(f"That number {entry} is out of range. Try again.")
                    valid = False
                    break
            else:
                entry_lower = entry.lower()
                if entry_lower in colors:
                    temp_selection.append(entry_lower)
                else:
                    print(f"'{entry}' is not a valid color name. Try again.")
                    valid = False
                    break
        if valid:
            selected_colors = temp_selection
            break

# Append selected colors to selected_colors.txt
with open(output_file_path, "a") as f:
    for color in selected_colors:
        f.write(color + "\n")

print("Selected colors saved:", ", ".join(selected_colors))
