def clean_corpus(filepath):
    cleaned_lines = []
    with open(filepath, 'r') as file:
        for line in file:
            cleaned_line = line.strip()  # Basic cleaning; modify as needed
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
    return cleaned_lines
