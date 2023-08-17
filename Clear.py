try:
    with open("results.txt", "w") as results_file:
        results_file.truncate(0)
        print("Results file cleared.")
except Exception as e:
    print(f"An error occurred: {e}")
