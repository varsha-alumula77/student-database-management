user_list = []
user_tuple = ()

while True:

    print("----- MUTABILITY DEMO -----") 
    print("1. Create List")
    print("2. Create Tuple") 
    print("3. Modify List") 
    print("4. Modify Tuple") 
    print("5. Slice List") 
    print("6. Slice Tuple") 
    print("7. Exit")

    user_choice = int(input("Enter your choice : "))

    if user_choice == 1:
        user_list = list(map(int, input("Enter numbers separated by space   : ").split()))
        print(user_list, "YOUR LIST IS READY!!")

    elif user_choice == 2:
        user_tuple = tuple(map(int, input("Enter numbers separated by space : ").split()))
        print(user_tuple, "YOUR TUPLE IS READY!!")

    elif user_choice == 3:
        if not user_list:
            print("PLEASE CREATE THE LIST FIRST!")
            continue

        print("1. Add element") 
        print("2. Delete element") 
        print("3. Modify element")
        user_list_modification = int(input("enter the your choice : "))

        if user_list_modification == 1:
            user_val = int(input("enter the value to add : "))
            user_list.append(user_val)
            print(user_list, "LIST AFTER ADDING ELEMENTS")

        elif user_list_modification == 2:
            user_list.pop()
            print(user_list, "LIST AFTER REMOVING ELEMENTS ")

        elif user_list_modification == 3:
            user_index = int(input("enter the index which you want to modify : "))
            user_value = int(input("enter the value : "))
            user_list[user_index] = user_value
            print(user_list, "LIST AFTER MODIFYING ELEMENTS ")

        else:
            print("choose valid options")

    elif user_choice == 4:
        if not user_tuple:
            print("PLEASE CREATE THE TUPLE FIRST!")
            continue

        print("1. Add element") 
        print("2. Delete element") 
        print("3. Modify element")
        user_tuple_modification = int(input("enter the your choice : "))

        if user_tuple_modification == 1:
            try:
                user_val = int(input("enter the value to add : "))
                user_tuple.append(user_val)
                print(user_tuple, "tuple after adding element")

            except AttributeError:
                print("TUPLE IS IMMUTABLE SO YOU CANNOT ADD ELEMENTS!! ")

        elif user_tuple_modification == 2:
            try:
                user_tuple.pop()
                print(user_tuple, "tuple after removing elements")

            except AttributeError:
                print("TUPLE IS IMMUTABLE SO YOU CANNOT REMOVE ELEMENTS!! ")

        elif user_tuple_modification == 3:
            try:
                user_index = int(input("enter the index which you want to modify : "))
                user_value = int(input("enter the value : "))
                user_tuple[user_index] = user_value
                print(user_tuple, "Tuple after modifying  elements")

            except TypeError:
                print("TUPLE IS IMMUTABLE SO YOU CANNOT MODIFY ELEMENTS!! ")

            except IndexError:
                print("Invalid index!")

        else:
            print("choose valid options")

    elif user_choice == 5:
        if not user_list:
            print("PLEASE CREATE THE LIST FIRST!")
            continue

        start_index = int(input("enter the starting index : "))
        end_index = int(input("enter the ending index : "))
        print(user_list[start_index:end_index])

    elif user_choice == 6:
        if not user_tuple:
            print("PLEASE CREATE THE TUPLE !")
            continue

        start_index = int(input("enter the starting index : "))
        end_index = int(input("enter the ending index : "))
        print(user_tuple[start_index:end_index])

    elif user_choice == 7:
        break

    else:
        print("Choose an option from 1 to 7")
    
            