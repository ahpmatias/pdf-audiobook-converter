import streamlit as st
import os
from converter import PDFConverter

def main():
    st.title("PDF-to-Audiobook Converter")
    st.write("Welcome to the PDF-to-Audiobook Converter!")

    pdf_file = st.file_uploader("Please upload the PDF file:", type=["pdf"])

    if pdf_file is not None:
        temp_dir = "temp"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
            st.write(f"Created directory: {temp_dir}")

        pdf_path = os.path.join(temp_dir, pdf_file.name)
        with open(pdf_path, "wb") as f:
            f.write(pdf_file.getbuffer())
            st.write(f"Saved PDF to: {pdf_path}")

        if os.path.isfile(pdf_path):
            st.write(f"File exists: {pdf_path}")
            converter = PDFConverter(pdf_path)
            audio_file = os.path.join(temp_dir, pdf_file.name.replace('.pdf', '.mp3'))
            converter.convert_to_audio(audio_file)

            if os.path.isfile(audio_file):
                st.success(f"Conversion successful! Audiobook saved as: {audio_file}")
            else:
                st.error("An error occurred during the conversion process.")
        else:
            st.error("The specified file does not exist. Please try again.")

if __name__ == "__main__":
    main()