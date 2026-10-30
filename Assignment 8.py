
def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r") as file:
            lines = file.readlines()

        total_lines = len(lines)

        first_two_lines = lines[:2]

        print("Total number of lines:", total_lines)
        print("\nFirst two lines:")

        for line in first_two_lines:
            print(line.strip())

        with open(output_file, "w") as file:
            file.writelines(first_two_lines)

        print("\nFirst two lines successfully written to", output_file)

    except FileNotFoundError:
        print("Error: input.txt file not found.")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()