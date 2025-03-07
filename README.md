# Natural Language Processing Class - Project 2: Human Console
### Author: Dominik Mikołajczyk

## Project Overview
The Human Console project is a natural language processing application designed to interpret and execute user commands entered via the console or through voice input. The program can perform a variety of tasks, such as opening applications, documents, and websites, playing media, defining words, checking weather conditions, and more.

## Features
The application supports the following functionalities:

- **Open Applications**: Launches an application specified by the user.
  - Command: `OPEN APP/APPLICATION NAME`

- **Close Applications**: Closes an open application specified by the user.
  - Command: `CLOSE APP/APPLICATION NAME`

- **Open Documents**: Opens a document with the specified name (without an extension). Supported extensions include `.txt`, `.pdf`, `.doc`, `.docx`, `.ppt`, `.pptx`, `.xls`, and `.xlsx`. The program searches in the current directory, `C:\Users\username\Documents`, and `C:\Users\username\Downloads`.
  - Command: `OPEN DOC/DOCUMENT NAME`

- **Open Websites**: Opens a website using Google Custom Search. The user must provide their own API key and CX ID in the `api_keys.py` file.
  - Command: `OPEN WEBSITE/WEBPAGE NAME`

- **Play Media**: Plays a song or video on YouTube based on the specified name.
  - Command: `PLAY SONG/VIDEO NAME`

- **Define Words**: Retrieves and displays a summarized definition of a word from Wikipedia.
  - Command: `DEFINE WORD NAME`

- **Check Weather**: Provides basic weather information for a specified location, including temperature, humidity, pressure, and a brief description. This feature uses the Open Weather Map API, requiring the user to provide their own API key.
  - Command: `CHECK WEATHER LOCATION`

- **Exit Program**: Exits the application.
  - Command: `EXIT/QUIT`

- **Voice Recognition**: Initiates voice recognition to listen for and execute commands.
  - Command: `VOICE/SPEECH/AUDIO INPUT/RECOGNITION`

## Installation
To set up the project, ensure you have Python installed, and then install the required Python libraries:

```bash
pip install ply==3.11
pip install appopener==1.5
pip install speechrecognition==3.9.0
pip install sumy==0.11.0
pip install youtube_search==2.1.2
pip install wikipedia-api==0.5.8
```

## Configuration
Before running the application, you need to configure your API keys in the `api_keys.py` file:

```python:api_keys.py
GOOGLE_CUSTOM_SEARCH_API_KEY = "YOUR GOOGLE CUSTOM SEARCH API KEY"
GOOGLE_CUSTOM_SEARCH_CX_ID = "YOUR GOOGLE CUSTOM SEARCH CX ID"
OPEN_WEATHER_MAP_API_KEY = "YOUR OPEN WEATHER MAP API KEY"
```

## Usage
Run the `human_console.py` script to start the application. You can enter commands directly into the console or use voice input to execute commands.

```bash
python human_console.py
```

## How It Works
The application uses the `ply` library for lexical analysis and parsing, allowing it to interpret natural language commands. It integrates several APIs and libraries to perform actions such as opening applications, searching the web, and retrieving weather data. Voice commands are processed using the `speech_recognition` library.
