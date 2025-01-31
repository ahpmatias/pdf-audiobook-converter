import os
from converter import PDFConverter

def main():
    print("Welcome to the PDF-to-Audiobook Converter!")
    pdf_file = input("Please enter the path to the PDF file: ")

    if not os.path.isfile(pdf_file):
        print("The specified file does not exist. Please try again.")
        return

    converter = PDFConverter()
    audio_file = converter.convert_to_audio(pdf_file)

    if audio_file:
        print(f"Conversion successful! Audiobook saved as: {audio_file}")
    else:
        print("An error occurred during the conversion process.")

if __name__ == "__main__":
    main()