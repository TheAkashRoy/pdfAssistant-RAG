import  PyPDF2 
from langchain.text_splitter import CharacterTextSplitter


def get_pdf_text(file_name):
    file_path = "./uploaded_files/" + file_name
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page_number in range(len(reader.pages)):
            text += reader.pages[page_number].extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

