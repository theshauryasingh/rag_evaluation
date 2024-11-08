def document_extractor(file_path):
    string_list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Remove surrounding quotes, trailing commas, and whitespace
            cleaned_line = line.strip().strip('",')
            string_list.append(cleaned_line)
    return string_list
