while True:  # Run this loop indefinitely until we break out of it
    print('Who are you?')  # Ask the user for their name
    name = input()  # Get the user's name from the input
    if name != 'Joe':  # If the name is not Joe, skip to the next iteration
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')  # Ask Joe for the password
    password = input()  # Get the password from the input
    if password == 'swordfish':  # If the password is correct
        break  # Exit this loop
print('Access granted.')  # If we exited the loop, we're granted access