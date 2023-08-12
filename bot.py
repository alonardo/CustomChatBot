# bot.py
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
import pickle
import gradio as gr

# Set the OpenAI API Key
api_key = os.environ["OPENAI_API_KEY"]

# Initialize an instance of OpenAI's GPT-3.5 model using ChatOpenAI class with specified temperature
chat = ChatOpenAI(temperature=0, model="gpt-4")

# Open and load the Faiss indices stored in 'indices.pkl' file
with open("indices.pkl", 'rb') as f: 
    faiss_indices = pickle.load(f)

# Initialize an empty list to keep a record of message history
message_history = []

# Define the main function to predict and generate response based on user's input
def predict(input):
    # Add extra newlines to the input to separate it from other content
    main_content = input + "\n\n"

    # For each Faiss index, find similar documents to the user's input (up to 6 documents)
    for faiss_index in faiss_indices:
        docs = faiss_index.similarity_search(input, K = 6)

        # For each found document, add its content to the main_content
        for doc in docs:
            main_content += doc.page_content + "\n\n"

    # Append the user's input message to the history
    message_history.append({"role": "user", "content": f"{input}"})

    # Generate an AI message and retrieve the content of the AI's response
    messages = [HumanMessage(content=main_content)]
    ai_response = chat(messages).content

    # Append the AI's response to the message history
    message_history.append({"role": "assistant", "content": f"{ai_response}"}) 

    # Prepare the formatted response, grouping user's messages and AI's responses
    response = [(message_history[i]["content"], message_history[i+1]["content"]) for i in range(0, len(message_history)-1, 2)]
    
    # Return the response to be displayed in the chat interface
    return response

# Start building the interactive UI using Gradio's Blocks
with gr.Blocks() as demo: 
    # Create an instance of a Chatbot interface component
    chatbot = gr.Chatbot() 

    # Start defining a row of UI components
    with gr.Row(): 
        # Add a Textbox for user input, without a label and with a placeholder text
        query = gr.Textbox(show_label=False, placeholder="Enter text and press enter")
    
    # Set the action when user submits a message: it triggers the predict function with the textbox and chatbot as arguments
    query.submit(predict, query, chatbot) 

    # Also, when user submits a message, the textbox is cleared. This is done through a JavaScript function assigned to the _js parameter.
    query.submit(None, None, query, _js="() => {''}") 
         
# Launch the created Gradio interface
demo.launch()
