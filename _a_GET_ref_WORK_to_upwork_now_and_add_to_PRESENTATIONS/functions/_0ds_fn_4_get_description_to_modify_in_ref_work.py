import PyPDF2

def read_ref_work_words(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    words = text.split()
    first_words = ' '.join(words[:how_many_words])
    return first_words
print('done')