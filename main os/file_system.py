def files():
    # Get user input
    userinputname = input("Enter the name of the text file")
    user_input = input("Enter some text: ")

    # Open a file for writing
    with open(userinputname, 'w') as file:
        # Write the user input to the file
        file.write(user_input)

    print("User input has been written to ", userinputname)
