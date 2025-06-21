catNames = []

while True:
    name = input("\n print your cat name: " + str(len(catNames)+1) + " or write 'gg' to stop ")
    if name.lower() == 'gg':
        break
    catNames.append(name)
    print("The cat names are: ")
    for name in catNames:
        print('' + name)
