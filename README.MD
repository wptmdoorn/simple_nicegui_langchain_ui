# Simple Chat Interface with NiceGUI and LangChain

This project is a simple chat interface built using Python, the NiceGUI package, and the LangChain API. With this chat interface, you can easily send and receive messages in real-time. This README will guide you through the process of setting up the project on your local machine.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Chat Interface](#running)
5. [Video Showcase](#video-showcase)

<a name="prerequisites"></a>
## Prerequisites

Before proceeding with the installation, ensure that you have the following installed on your system:

- Git
- Python 3.6 or later

<a name="installation"></a>
## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**: Open a terminal or command prompt and run the following command to clone the repository:

```git clone https://github.com/wptmdoorn/simple_nicegui_langchain_ui.git```


2. **Install requirements**: Navigate to the project directory and run the following command to install the required packages:

```pip install -r requirements.txt```


<a name="configuration"></a>
## Configuration

1. **Create a .env file**: Rename the .envtemplate file to .env

2. **Add API Key**: Obtain an API key for OpenAI. Open the `.env` file and add replace the `OPENAI_API_KEY` with your actual API key


<a name="running"></a>
## Running the Chat Interface

To run the chat interface, simply execute the following command in the project directory:

```python main.py```


Now, you can interact with the chat interface using the NiceGUI window.

<a name="video-showcase"></a>
## Video Showcase

To get a better understanding of how the chat interface works, check out this short video showcasing the functionality of the project:

[video](https://user-images.githubusercontent.com/26939682/234681682-056a05b7-5202-4d93-8bab-4af189e07b60.mp4)

That's it! You now have a fully functional chat interface powered by NiceGUI and LangChain. Enjoy chatting!
