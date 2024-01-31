# Galactico

## A pdf summarizer and helpful chatbot!

This project is an advanced chatbot. The main focus was to leverage a Large Language Model (LLM) to enhance interaction with a pdf, making it easier to understand its contents. The chatbot relies on the LLM's capabilities to interpret complex user queries and generate responses in the context of the pdf and summarise the topics for more clarity.

Got a pdf that is too long to go through? Want answers or clarity on specific topics? Upload your pdf and have a chat with our bot to clarify all your doubts and confusions!

## Authors

- [@AdwaitaBasuBal](https://github.com/AdwaitaBasuBal)
- [@AnanyaBt](https://github.com/AnanyaBt)
- [@priyanshupant](https://github.com/priyanshupant)

## Features

- Q & A casual and pdf related
- Summarization
- Context page retrieval

## Installation

Clone or download the zip files from the repository.

Make sure you have [Python](https://www.python.org/) and [pip](https://pypi.org/project/pip/) installed on your device.

Import all the necessary libraries:-

- `streamlit`
- `pathlib`
- `openai`
- `PyPDF2`
- `langchain`

## Environment Variables

Import dotenv and set up your virtual environment.

```bash
python -m venv .venv
```

Create your API key from the OpenAI site and add it to the newly created `.env` file. This only needs to be done the first time you execute the program.

## Deployment

Run the program through streamlit

```bash
streamlit run [path to your program].py
```

The chatbot is ready for you!

## Screenshots

The homepage for the chatbot.

![Chatbot ss 1](https://github.com/AdwaitaBasuBal/adwaitabasubal.github.io/assets/109857501/7d60b9ce-ae6e-4a43-bfbd-76338e842276)

Small talk

![normal convo](https://github.com/AdwaitaBasuBal/AdwaitaBasuBal/assets/109857501/4e161763-90a6-4620-bf04-b6af2b4f53a8)

Asking questions!

![chatbot ss 2](https://github.com/AdwaitaBasuBal/adwaitabasubal.github.io/assets/109857501/d781ba36-4820-489f-95f2-864f3b80bc4a)

The summarizing tool

![chatbot ss 3](https://github.com/AdwaitaBasuBal/adwaitabasubal.github.io/assets/109857501/fe6b1fbe-2a9d-41cc-b5cd-7f9964cf1c8a)

Page referencing
![Page number given](https://github.com/AdwaitaBasuBal/AdwaitaBasuBal/assets/109857501/6614eb53-a77f-4bdb-94f4-46f89a1cfa1b)

## Acknowledgements

Special thanks to [Rohan Sir](https://www.linkedin.com/in/rohan-shah-315366153/) for his guidance and support with the project.
