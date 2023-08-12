# Custom ChatBot
This repository allows you to have a conversation with your own data!

## Features:

-   **Support for Multiple File Types**: The system can process both `.pdf` and `.txt` files, allowing a wide range of documents to be used.
-   **Real-time Responses**: Using OpenAI's GPT API, the chatbot provides quick and accurate responses based on the content of your documents.
-   **Interactive UI**: A user-friendly interface built using Gradio's Blocks allows for a seamless chatting experience.

## Files in the Repository

1.  **create_index.py**:
    
    -   This script is responsible for creating a Faiss index from the text present in the files stored in the `uploads` directory.
    -   It can process both `.pdf` and `.txt` files.
    -   All Faiss indices are saved in a `indices.pkl` file.
    -   **Important**: This script should be run only once or whenever there are new documents you want the chatbot to reference.
    
2.  **bot.py**:
    
    -   This script initializes an interactive chatbot interface.
    -   The chatbot uses the Faiss indices to find documents similar to the user's input and generate responses.
    -   The chatbot uses OpenAI's GPT-3.5 model for generating responses.
    -   An interactive UI is built using Gradio's Blocks, which allows users to interact with the chatbot in real-time.

## Setup and Installation

1.  **Prerequisites**:
    
    -   Make sure you have Python 3.x installed.
    -   Set the OpenAI API key as an environment variable: `export OPENAI_API_KEY=your_api_key_here`.
2.  **Installation**:
    
    -   Clone this repository: `git clone https://github.com/your_repository_link.git`
    -   Navigate to the directory: `cd path_to_directory`
    -   Install the required packages: `pip install -r requirements.txt` (Note: You need to have a `requirements.txt` file with all necessary libraries listed.)
3.  **Usage**:
    
    -   Place the documents you want the chatbot to reference in the `uploads` directory.
    -   Run the `create_index.py` script to create the Faiss indices: `python create_index.py`
    -   Launch the chatbot interface: `python bot.py`
    -   Interact with the chatbot using the provided UI.

## Questions/Comments

Please direct any questions or comments to [Andre](https://www.linkedin.com/in/andre-lonardo/).

## License

This project is licensed under the MIT License. 
