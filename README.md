LLM-powered HR Chatbot

This repository contains a full-stack application for an HR chatbot powered by a fine-tuned GPT-2 language model. The chatbot is designed to assist with HR-related queries and provide a seamless user experience through a modern, animated interface.

Table of Contents

-[Features](#Features)

-[Tech Stack](#TechStack)

-[Prerequisites](#Prerequisites)

-[Installation](#Installation)

-[Usage](#Usage)

-[Project Structure](#ProjectStructure)

-[Backend](#Backend)

-[Frontend](#Frontend)

-[Customization](#Customization)

-[Contributing](#Contributing)


## Features

Full-stack application with Flask backend and React frontend
GPT-2 based language model fine-tuned for HR-related queries
Animated and responsive user interface using Framer Motion
Real-time chat functionality
Mobile-friendly design

## TechStack

 Backend:

Python
Flask
PyTorch
Transformers (Hugging Face)


Frontend:

React
Framer Motion
Lucide React (for icons)
Tailwind CSS



## Prerequisites

Python 3.7+
Node.js 14+
npm or yarn

## Installation

Set up the backend:
Copycd backend
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

Set up the frontend:
Copycd ../frontend
npm install  # or yarn install

Download the fine-tuned model:
Place your fine-tuned GPT-2 model in a directory named hr_gpt2_model1 in the backend folder.

## Usage

Start the backend server:
Copycd backend
python app.py

In a new terminal, start the frontend development server:
Copycd frontend
npm start  # or yarn start

Open your browser and navigate to http://localhost:3000 to use the chatbot.

## Project Structure

Copyllm-hr-chatbot/

├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── hr_gpt2_model1/  # Fine-tuned model directory
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json
│   └── tailwind.config.js
└── README.md
## Backend

The backend is built with Flask and uses a fine-tuned GPT-2 model for generating responses. Key components:

app.py: Contains the Flask application and API endpoint for chat functionality.
HRChatbot class: Handles the interaction with the GPT-2 model.

## Frontend
The frontend is a React application with an animated interface. Key components:

App.js: Main component containing the chat interface and logic.
ChatMessage: Component for rendering individual chat messages.

## Customization

To customize the chatbot's responses, you can fine-tune the GPT-2 model on a different dataset or adjust the generation parameters in the get_response method of the HRChatbot class.
To modify the UI, edit the React components in App.js and update the Tailwind CSS classes.
To add new features, such as user authentication or message history, extend both the backend API and frontend components accordingly.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. 
