entries = []

user_selection = input("Enter 'a' to add an entry, or 'q' to quit: ")

while user_selection != 'q':
    if user_selection == 'a':
        entry_content = input("What did you learn today? ")
        entries.append(entry_content)
    user_selection = input("Enter 'a' to add an entry or 'q' to quit: ")

print(entries)