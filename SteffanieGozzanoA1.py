""""Steffanie Gozzano
9/4/2016
Hire an item program
https://github.com/Steffanie/SteffanieGozzanoA1.git

"""

MENU = """(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit

"""
FILENAME = "items.csv"


#main function to access selection
def main():
    items = load_items()
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "l":
            list_items(items)
        elif choice == "h":
            hire_an_item(items)
        elif choice == "r":
            return_items(items)
        elif choice == "a":
            add_new_item(items)
        else:
            print("Invalid choice, please try again: ")
        print(MENU)
        choice = input(">>>").lower()
    save_items(items)
    print("Have a nice day ")



"""function loadItems()
open “items.csv” as inFile for reading
itemsList = empty list
for line in inFile
	append line to itemsList
return itemList
"""

#loads file into each function
def load_items():
    inFile = open(FILENAME, "r")
    itemsList = []
    for line in inFile:
        itemsList.append(line.strip().split(","))
    return itemsList

#saves file onto csv file
def save_items(items):
    outFile = open(FILENAME, "w")
    for item in items:
        itemsAsAList = ",".join(item)
        outFile.write(itemsAsAList)
        outFile.write("\n")

#shows all the items in the file
def list_items(items):
    print("All items on file (* indicates item is currently out) ")
    count = -1
    for item in items:
        count += 1
        if item[3] == "out":
            print(count, "-","{:<12}".format(item[0]),"{:<30} ".format("("+item[1]+")"), "= $","{:6.2f} *".format(float(item[2])))
        else:
            print(count, "-","{:<12}".format(item[0]),"{:<30} ".format("("+item[1]+")"), "= $","{:6.2f}".format(float(item[2])))

#adds new item with details of description and cost
def add_new_item(items):
    moreItems = []
    itemName = input("Item name: ")
    descriptionOfItem = input("Description: ")
    valid = False
    while not valid:
        try:
            priceOfItemPerDay = float(input("Price per day: $"))
            if priceOfItemPerDay < 0:
                print("Price must be >= $0")
            else:
                valid = True
        except ValueError:
            print("Invalid input; enter a valid number")

#adding to list
    moreItems.append(itemName)
    moreItems.append(descriptionOfItem)
    moreItems.append (str(priceOfItemPerDay))
    moreItems.append("in")
    items.append(moreItems)
    print(itemName, "(" + descriptionOfItem + "), $" + "{:6.2f} now available for hire".format(priceOfItemPerDay))

#Removes item from availability to be hired
def hire_an_item(items):
    count = -1
    for item in items:
        count += 1
        if item[3] == "in":
            print(count, "-","{:<12}".format(item[0]),"{:<30} ".format("("+item[1]+")"), "= $","{:6.2f}".format(float(item[2])))

    valid = False
    while not valid:
        try:
            itemToHire = int(input("Make your selection: "))
            if itemToHire < 0:
                print("Invalid item number")
            else:
                valid = True
        except ValueError:
            print("Invalid input; enter a number")

#making sure selected item is available for hire and changes to an option to be returned
    if items[itemToHire][3] == "in":
        print(items[itemToHire][0], "hired for ", "${:6.2f}".format(float(items[itemToHire][2])))
        items[itemToHire][3] = "out"
    else:
        print("This item is not available for hire")

#returns an item to be available again
def return_items(items):
    count = -1
    for item in items:
        count += 1
        if item[3] == "out":
            print(count, "-","{:<12}".format(item[0]),"{:<30} ".format("("+item[1]+")"), "= $","{:6.2f}".format(float(item[2])))
    valid = False
    while not valid:
        try:
            itemToReturn = int(input("Make your selection: "))
            if itemToReturn < 0:
                print("Invalid item number")
            else:
                valid = True
        except ValueError:
            print("Invalid input; enter a number")
#making sure item is available to be returned and allows it to be hired again
    if items[itemToReturn][3] == "out":
        print(items[itemToReturn][0], "returned")
        items[itemToReturn][3] = "in"
    else:
        print("Invalid item number")

#calls main function
main()
