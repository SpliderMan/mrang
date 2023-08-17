import random
import ctypes
import pyperclip

#ctypes.windll.kernel32.SetConsoleTitleW("Alt picker")

def pick_name(file_path):
    try:
        with open(file_path, 'r') as file:
            names = [line.strip() for line in file if line.strip()]
            if not names:
                print("No names found in the file.")
            else:
                while names:
                    random_name = random.choice(names)
                    pyperclip.copy(random_name)  # Copy the name to clipboard
                    print(f"Your alt name is {random_name}. It has been copied to your clipboard.")
                    
                    names.remove(random_name)  # Remove the chosen name from the list
                    
                    with open(file_path, 'w') as file:
                        file.write('\n'.join(names))  # Write the remaining names back to the file
                        
                    choice = input("Press Enter to choose another alt name or any other key to exit: ")
                    if choice == "":
                        continue  # Generate a new name and continue the loop
                    else:
                        break  # Exit the loop if any key other than Enter is pressed
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file_path = "results.txt"
    pick_name(input_file_path)
