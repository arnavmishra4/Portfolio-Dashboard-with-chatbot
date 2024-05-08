import os
import fitz  # PyMuPDF
import re

def extract_text(pdf_path):
    extracted_text = []
    try:
        pdf_document = fitz.open(pdf_path)
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            text = page.get_text("text")
            # Optional: filter non-printable characters
            text = re.sub(r'[^\x20-\x7E]+', '', text)
            extracted_text.append(text)
        pdf_document.close()
    except Exception as e:
        print(f"Error occurred while processing PDF '{pdf_path}': {e}")
    return extracted_text

def filter_text(text):
    unique_lines = set()
    for page_text in text:
        lines = page_text.split('\n')
        for line in lines:
            # Strip whitespace and check if the line is not empty
            if line.strip() and line.strip() not in unique_lines:
                unique_lines.add(line.strip())
    return '\n'.join(unique_lines)

# Path to the folder containing PDF files
folder_path = 'E:/Data2/'

# Output file path to save the combined text
output_file_path = 'extracted_text.txt'

# Iterate over each PDF file in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, file_name)
        try:
            extracted_text = extract_text(pdf_path)
            filtered_text = filter_text(extracted_text)
            
            # Save filtered text every iteration
            with open(output_file_path, 'a', encoding='utf-8') as output_file:
                output_file.write(filtered_text + '\n')
        except Exception as e:
            print(f"Error occurred while processing PDF '{pdf_path}': {e}")

print("Processing completed. Extracted and filtered text saved to", output_file_path)
