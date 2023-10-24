# Main menu
def main_menu():
    while True:
        print('[1] Add task')
        print('[2] List tasks')
        print('[3] Remove task')
        print('[4] Exit program')

        choice = input('Enter your choice: ')

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            exit()
        else:
            print('Invalid choice. Please try again.')

# Function to add task to static txt fiile
def add_task():
    task = input('Enter your task: ')
    with open('list.txt', 'a') as list:
        list.write(f'{task}\n')
        print(f'Successfully added {task} to list!')

# Function to list out tasks from txt file
def list_tasks():
    with open('list.txt', 'r') as list:
        content = list.read()
        print(content)

# Function to remove tasks from list by showing tasks
def remove_task():
    list_tasks()
    remove = input('Enter the task you would like to remove: ')
    with open('list.txt', 'r') as list:
        content = list.read()

    newlist = content.replace(remove, '')

    with open('list.txt', 'w') as list:
        list.write(newlist.strip())
    print(f'Successfully removed {remove} from list.')

if __name__ == "__main__":
    main_menu()