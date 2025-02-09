def main():
    # Get the text input from the user.
    # Note: The input should contain an '=' character somewhere to trigger the output.
    text = input("Input: ")

    total_sum = 0       # This will hold the cumulative sum.
    adder_active = True # The adder is initially active.
    i = 0               # 'i' as an index to traverse the string.

    while i < len(text):
        # Check for the "=" character.
        if text[i] == "=":
            print("Sum:", total_sum)
            return  # Exit the program.

        # If the current character is a digit, accumulate the entire number.
        if text[i].isdigit():
            num_str = ""
            # Collect all consecutive digits.
            while i < len(text) and text[i].isdigit():
                num_str += text[i]
                i += 1
            # If the adder is active, add the found number to the total.
            if adder_active:
                total_sum += int(num_str)
            # Continue with the next character (we already updated 'i').
            continue

        # If the current character is alphabetical, check for "Off" or "On".
        elif text[i].isalpha():
            # Check for "Off"
            if text[i:i+3].lower() == "off":
                adder_active = False
                i += 3  # Skip the characters that form "off".
                continue
            # Check for "On"
            elif text[i:i+2].lower() == "on":
                adder_active = True
                i += 2  # Skip the characters that form "on".
                continue

        # Ignore any other characters.
        i += 1

    # In case there's no '=' do nothing.
    print("No '=' character found.", total_sum)


if __name__ == "__main__":
    main()
