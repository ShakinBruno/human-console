# Natural Language Processing Class - Project 2: Human Console
### author: Dominik Mikołajczyk

## The task the of project
The aim of the project was to write a program that responds to commands written in the console in a natural language chosen by the author, the purpose of which is to:
- run the program with the given name
- close the program with the given name
- open the document with the given name
- open the specified website in the browser
- optional: other actions

## Requirements:        
Install required python libraries:
    <!-- -->
    
        pip install ply==3.11
        pip install appopener==1.5
        pip install speechrecognition==3.9.0
        pip install sumy==0.11.0
        pip install youtube_search==2.1.2
        pip install wikipedia_api==0.5.8
        
## Functionalities
All commands are being processed by pure-Python implementation of tools lex and yacc. Each command can be triggered using voice input, to do that type correct command and say your desired command. Each component of the command must be separated by a space or tabulator and are processed case insensitive. All commands with their corresponding commands are as follows:
- OPEN APP/APPLICATION NAME - opens app with specified NAME.
- CLOSE APP/APPLICATION NAME - closes opened app with specified NAME.
- OPEN DOC/DOCUMENT NAME - opens document with specified NAME (without an extension). Supported extensions are: txt, pdf, doc, docx, ppt, pptx, xls, xlsx. Searched directories are: project directory, C:\Users\username\Documents, C:\Users\username\Downloads.
- OPEN WEBSITE/WEBPAGE NAME - opens website with specified NAME (without a domain) using Google Custom Search engine (you have to include your own API key and CX in code).
- PLAY SONG/VIDEO NAME - opens youtube.com in your browser and plays the video with the specified NAME.
- DEFINE WORD NAME - prints in console the summarized definition from wikipedia of word with specified NAME.
- CHECK WEATHER LOCATION - prints in console basic information about weather at specified LOCATION such as temperature, humidity, pressure and short description (it uses Open Weather Map API so you have to include your own API key in code).
- EXIT/QUIT - exits the program.
- VOICE/SPEECH/AUDIO INPUT/RECOGNITION - starts voice recognition and waits for user to say one of commands listed above.
