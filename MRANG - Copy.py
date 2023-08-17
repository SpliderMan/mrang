import random
import os
import ctypes
import time
import string

# Set the console title to "rng" (Windows only)
# ctypes.windll.kernel32.SetConsoleTitleW("M-RANG")
N = "Names.txt"
V = "Verbs.txt"
A = "Adj.txt"

# Read names from the "Names.txt" file
try:
    with open(N, "r") as names_file:
        names = [line.strip() for line in names_file]
except Exception as e:
    print(f"Error reading 'Names.txt': {e}")
    names = []

# Read adjectives from the "Adj.txt" file
try:
    with open(A, "r") as adj_file:
        adjectives = [line.strip() for line in adj_file]
except Exception as e:
    print(f"Error reading 'Adj.txt': {e}")
    adjectives = []

# Read verbs from the "Verbs.txt" file
try:
    with open(V, "r") as verbs_file:
        verbs = [line.strip() for line in verbs_file]
except Exception as e:
    print(f"Error reading 'Verbs.txt': {e}")
    verbs = []

if not names or not adjectives or not verbs:
    print("No names, adjectives, or verbs found in the files.")
else:
    try:
        num_names = int(input("How many names do you want to generate? "))
        if num_names <= 1:
            print("You must enter more than 1 amount of names.")
        else:
            include_numbers = input("Do you want numbers in the names? (Y/N): ").lower()
            if include_numbers == "y":
                include_numbers = True
            else:
                include_numbers = False

            generated_count = 0
            print("Generating")

            start_time = time.time()  # Start the timer

            while generated_count < num_names:
                try:
                    random_name = random.choice(names)
                    random_name2 = random.choice(names)
                    random_adjective = random.choice(adjectives)
                    random_verb = random.choice(verbs) if random.random() < 0.3 else ""

                    # Generate a random password with only letters and numbers
                    random_password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

                    if include_numbers:
                        random_number = random.randint(1, 999)
                        random_choice = random.random()

                        if random_choice < 1/3:
                            new_name = f"{random_name}{random_name2}{random_number}"
                        elif random_choice < 2/3:
                            new_name = f"{random_adjective}{random_verb}{random_name}{random_number}"
                        else:
                            new_name = f"{random_adjective}{random_name}{random_number}"
                    else:
                        random_choice = random.random()

                        if random_choice < 1/3:
                            new_name = f"{random_name}{random_name2}"
                        elif random_choice < 2/3:
                            new_name = f"{random_adjective}{random_verb}{random_name}"
                        else:
                            new_name = f"{random_adjective}{random_name}"
                    new_nameWithPassword= f"{new_name}:{random_password}"
                    if len(new_name) > 20:
                        continue  # Regenerate the name if it's over 20 characters

                    with open("results.txt", "a") as results_file:
                        results_file.write(new_nameWithPassword + "\n")

                    generated_count += 1

                except Exception as e:
                    print(f"An error occurred: {e}")

            end_time = time.time()  # End the timer
            elapsed_time = end_time - start_time
            print(f"Generated {num_names} names in {elapsed_time:.2f} seconds.")
            time.sleep(1)  # Wait for 1 second

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nGeneration interrupted.")
