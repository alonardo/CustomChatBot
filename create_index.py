# Import necessary libraries and modules
import os
import pickle
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
import xml.etree.ElementTree as ET

# Set the OpenAI API key
api_key = os.environ["OPENAI_API_KEY"]

# Define a function to extract and return text from a PDF file
def handle_pdf(file_path):
    # Use PdfReader to read the PDF file
    reader = PdfReader(file_path)
    raw_text = ''
    # Extract text from each page of the PDF
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            raw_text += text
    return raw_text

# Define a function to read and return text from a .txt file
def handle_txt(file_path):
    with open(file_path, 'r', encoding='utf8', errors='ignore') as f:
        raw_text = f.read()
    return raw_text

# Define a function to create a Faiss index from text in a file
def create_faiss_index(file_path):
    # Handle file type accordingly and extract raw text
    if file_path.endswith('.pdf'):
        raw_text = handle_pdf(file_path)
    elif file_path.endswith('.txt'):
        raw_text = handle_txt(file_path)
    else:
        return None

    # Split the raw text into smaller chunks for processing
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=250, length_function=len)
    texts = text_splitter.split_text(raw_text)

    # Create embeddings from the split text using OpenAI Embeddings
    embeddings = OpenAIEmbeddings(disallowed_special=())
    # Create a Faiss index from these embeddings
    faiss_index = FAISS.from_texts(texts, embeddings)

    return faiss_index

# Define the main function to create and save Faiss indices for all files in a specified directory
def main():
    faiss_indices = []
    uploads_dir = 'uploads'

    # Create a Faiss index for each file in the uploads directory and add it to the list
    for file_name in os.listdir(uploads_dir):
        faiss_index = create_faiss_index(os.path.join(uploads_dir, file_name))
        if faiss_index:
            faiss_indices.append(faiss_index)

    # Save the list of Faiss indices to a .pkl file
    with open("indices.pkl", 'wb') as f:
        pickle.dump(faiss_indices, f)

# Run the main function if this script is the main entry point
if __name__ == '__main__':
    main()
