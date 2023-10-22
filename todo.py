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

if __name__ == "__main__":
    main_menu()