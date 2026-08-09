try:
    file_name = input("Enter the file name with extension: ")

    with open(file_name,'r') as f:
        print(f.read())


except FileNotFoundError:
    print("File not found. Please check the file name")


finally:
    print("File reading operation completed.")

