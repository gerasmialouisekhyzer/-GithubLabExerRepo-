def navigate_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error: {e}")
        return

    num_lines = len(lines)
    while True:
        print(f"The number of lines in the file is {num_lines}.")
        s = input(f"Enter a line number (1-{num_lines}) or 0 to quit: ")
        try:
            choice = int(s)
        except ValueError:
            print("Please enter an integer.")
            continue

        if choice == 0:
            break
        if 1 <= choice <= num_lines:
            print(lines[choice - 1].rstrip('\n'))
        else:
            print("Invalid line number.")

if __name__ == "__main__":
    navigate_file()
