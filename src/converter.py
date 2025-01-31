class PDFConverter:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file

    def convert_to_audio(self, output_audio_file):
        import PyPDF2
        from gtts import gTTS

        # Read the PDF file
        with open(self.pdf_file, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()

        # Convert text to audio
        tts = gTTS(text=text, lang='en')
        tts.save(output_audio_file)