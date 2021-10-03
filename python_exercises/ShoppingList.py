# Create a program that will keep track of items for a shopping list. The program should keep asking for new items until
# nothing is entered (no input followed by enter key). The program should then display the full shopping list.

shopping_list = []
item = None
while item != '':
    item = input('what do u wanna buy?')
    if item!= '':
        shopping_list.append(item)


print(shopping_list)