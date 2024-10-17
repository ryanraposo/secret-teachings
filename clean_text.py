from pdfminer.high_level import extract_text
import re

# Define file paths
pdf_path = "data/Manly-P-Hall_The-Secret-Teachings-of-All-Ages.pdf"
output_txt_path = "data/secret_teachings_cleaned_pdfminer.txt"


def clean_text(text):
    # Remove unwanted characters like newlines, extra spaces, and page numbers
    text = re.sub(r"\s+", " ", text)  # Replace multiple whitespace with a single space
    text = re.sub(r"([0-9]+)", "", text)  # Remove page numbers
    text = re.sub(r"[^A-Za-z0-9,.?!:;\-\(\)\'\s]", "", text)  # Keep basic punctuation
    return text.strip()


def extract_text_from_pdf_with_pdfminer(pdf_path):
    try:
        text = extract_text(pdf_path)
        return clean_text(text)
    except Exception as e:
        print(f"Failed to extract text: {e}")
        return ""


# Extract the text using PDFMiner
text_data = extract_text_from_pdf_with_pdfminer(pdf_path)

# Save the cleaned text into a .txt file
with open(output_txt_path, "w", encoding="utf-8") as f:
    f.write(text_data)

print(f"Text extracted and cleaned. Saved to {output_txt_path}.")
