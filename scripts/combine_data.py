import os

folder_path = "data"

def create_dataset(folder_path, output_file, num_files=None):
    with open(output_file, "w") as outfile:
        count = 0
        for filename in sorted(os.listdir(folder_path)):  
            if filename.endswith(".txt"):
                with open(os.path.join(folder_path, filename), "r") as infile:
                    outfile.write(infile.read() + "\n\n")  
                    count += 1
                    if num_files and count >= num_files:
                        break
    print(f"Dataset saved to {output_file}")

create_dataset(folder_path, "first_10_poems.txt", num_files=10)
create_dataset(folder_path, "first_20_poems.txt", num_files=20)
create_dataset(folder_path, "all_poems.txt")
