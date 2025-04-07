file_read_write.py

def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.replace("old_word", "new_word")  # Modify as needed
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"File successfully modified and saved to {output_filename}")
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
