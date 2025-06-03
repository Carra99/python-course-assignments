import sys

colors = ["blue", "green", "yellow", "white"]

selected_color = None

# Try to get user input from command line
if len(sys.argv) > 1:
    arg = sys.argv[1]

    if arg.isdigit():
        index = int(arg)
        if 0 <= index < len(colors):
            selected_color = colors[index]
        else:
            print(f"Error: Index {index} is out of range.")
            sys.exit(1)
    else:
        arg_lower = arg.lower()
        if arg_lower in colors:
            selected_color = arg_lower
        else:
            print(f"Error: '{arg}' is not a valid color name.")
            sys.exit(1)

else:
    print("Choose a color:")
    for i, color in enumerate(colors):
        print(f"{i}: {color}")

    while True:
        choice = input("Enter the number of your color: ")
        if choice.isdigit():
            index = int(choice)
            if 0 <= index < len(colors):
                selected_color = colors[index]
                break
            else:
                print("That number is out of range. Try again.")
        else:
            print("Invalid input. Please enter a valid number.")

# Append selected color to colors.txt
with open("colors.txt", "a") as f:
    f.write(selected_color + "\n")

print(f"Selected color saved: {selected_color}")
