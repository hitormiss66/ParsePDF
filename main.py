import re
import pdfplumber


# Function to extract 7-digit numbers from a PDF
def extract_numbers_from_pdf(pdf_path):
    numbers = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Find all 7-digit numbers
                found_numbers = re.findall(r'\b\d{7}\b', text)
                numbers.extend(found_numbers)
    return numbers


# Function to save numbers to a TXT file
def save_numbers_to_txt(numbers, txt_path):
    # Remove duplicates using set
    unique_numbers = list(set(numbers))
    with open(txt_path, 'w') as f:
        for number in unique_numbers:
            f.write(f"{number}\n")


# Main execution
if __name__ == "__main__":
    pdf_path = input("Enter the path to the PDF file: ")
    txt_path = input("Enter the path for the output TXT file: ")

    # Extract numbers and save to TXT
    extracted_numbers = extract_numbers_from_pdf(pdf_path)
    save_numbers_to_txt(extracted_numbers, txt_path)

    print(f"Extracted {len(extracted_numbers)} numbers and saved to {txt_path}.")
