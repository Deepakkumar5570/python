print('Welcome To Mini Contact Book App')
contacts = {}
while True:
    print('\nContact Book App')
    print('1. Create contact')
    print('2. View contact')
    print('3. Update contact')
    print('4. Delete contact')
    print('5. Search contact')
    print('6. Count contact')
    print('7. Exit contact')

    choice = input('Enter your choice = ')

    if choice == '1':
        name = input("Enter your name = ")
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter Age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter contact name to view = ')
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {contact["age"]}, Mobile Number: {contact["mobile"]}, Email: {contact["email"]}')
        else:
            print('Contact Not Found!')

    elif choice == '3':
        name = input('Enter name to update contact = ')
        if name in contacts:
            age = input('Enter Updated Age = ')
            email = input('Enter Updated email = ')
            mobile = input('Enter Updated mobile number = ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact {name} has been updated successfully!')
        else:
            print('Contact Not Found')

    elif choice == '4':
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted successfully!')
        else:
            print('Contact Not Found')

    elif choice == '5':
        search_name = input('Enter contact name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - Name: {name}, Age: {contact["age"]}, Mobile Number: {contact["mobile"]}, Email: {contact["email"]}')
                found = True
        if not found:
            print('No contact found with that name')

    elif choice == '6':
        print(f'Total contacts in your book: {len(contacts)}')

    elif choice == '7':
        print('Goodbye... Closing the program')
        break

    else:
        print('Invalid Input')
