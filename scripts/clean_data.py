data_file = 'data/first_10_poems.txt'
import re

def clean_text(input_file, output_file):
    with open(input_file, "r") as infile:
        text = infile.read()
        text = re.sub(r"[^\w\s']", "", text)
        text = re.sub(r"\n+", " ", text)

        text = text.lower()
    
    with open(output_file, "w") as outfile:
        outfile.write(text)
    print(f"Cleaned text saved to {output_file}")


clean_text(data_file, "cleaned_file.txt")