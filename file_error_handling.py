file_error_handling.py

def get_file_contents():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
