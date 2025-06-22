birthdays = { "Alice": " Dec 12 ", "Anton": "Sep 22", "Lily": "11 Apr"}

while True:
    name = input("\n Enter a name: ('q' - to quit)")

    if name.lower == 'q':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthdays of ' + name)

    else: 
        print("I don`t have birthday information about for " + name)
        bday = input("What is your birthday? ")
        birthdays[name] = bday
        print("Birthday database updated.")