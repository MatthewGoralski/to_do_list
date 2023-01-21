import json

todo_list = []

def save_list():
    with open('todo_list.json', 'w') as file:
        json.dump(todo_list, file)

def load_list():
    global todo_list
    try:
        with open('todo_list.json', 'r') as file:
            todo_list = json.load(file)
    except:
        pass

def add_item(item):
    todo_list.append(item)
    print("Item added: ", item)
    save_list()

def remove_item(item):
    todo_list.remove(item)
    print("Item removed: ", item)
    save_list()

def list_items():
    if len(todo_list) == 0:
        print("No items in the list.")
    else:
        for i in range(len(todo_list)):
            print(str(i+1) + ". " + todo_list[i])

def main():
    load_list()
    while True:
        action = input("What would you like to do? (add/remove/list/quit): ")
        if action == 'add':
            item = input("Enter item to add: ")
            add_item(item)
        elif action == 'remove':
            item = input("Enter item to remove: ")
            remove_item(item)
        elif action == 'list':
            list_items()
        elif action == 'quit':
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
