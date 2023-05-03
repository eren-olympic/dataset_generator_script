# transformat.py
def transform_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
        current_category = ""
        for line in f_in:
            line = line.strip()
            if line.endswith("{"):
                current_category = line[:-1].strip()
            elif line.endswith("}"):
                current_category = ""
            elif ":" in line:
                sub_category, items = line.split(":", 1)
                items = items.strip().split("、")
                for item in items:
                    f_out.write(f"{current_category} > {sub_category.strip()} > {item.strip()}\n")

if __name__ == "__main__":
    transform_file("category.txt", "category2.txt")
