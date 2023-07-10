import os
import requests
import webbrowser
import wikipediaapi

import ply.lex as lex
import ply.yacc as yacc
import speech_recognition as sr

from api_keys import GOOGLE_CUSTOM_SEARCH_API_KEY, GOOGLE_CUSTOM_SEARCH_CX_ID, OPEN_WEATHER_MAP_API_KEY
from AppOpener import close, open
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from youtube_search import YoutubeSearch

tokens = ("OPEN", "CLOSE", "PLAY", "DEFINE", "CHECK", "APP", "DOC", "WEBSITE", "SONG", "WORD", "WEATHER", "EXIT", "VOICE", "INPUT", "NAME")
t_ignore = " \t"


def t_OPEN(t):
    r'open'
    return t


def t_CLOSE(t):
    r'close'
    return t


def t_PLAY(t):
    r'play'
    return t


def t_DEFINE(t):
    r'define'
    return t


def t_CHECK(t):
    r'check'
    return t


def t_APP(t):
    r'app(lication)?'
    return t


def t_DOC(t):
    r'doc(ument)?'
    return t


def t_WEBSITE(t):
    r'web(site|page)'
    return t


def t_SONG(t):
    r'song|video'
    return t


def t_WORD(t):
    r'word'
    return t


def t_WEATHER(t):
    r'weather'
    return t


def t_EXIT(t):
    r'exit|quit'
    return t


def t_VOICE(t):
    r'voice|speech|audio'
    return t


def t_INPUT(t):
    r'input|recognition'
    return t


def t_NAME(t):
    r'.+'
    return t


def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)


def p_command(p):
    '''
    command : OPEN action
            | CLOSE action
            | PLAY action
            | DEFINE action
            | CHECK action
            | VOICE INPUT
    '''
    p[0] = (p[1], p[2])


def p_command_exit(p):
    'command : EXIT'
    p[0] = (p[1],)


def p_action(p):
    '''
    action : APP NAME
           | DOC NAME
           | WEBSITE NAME
           | SONG NAME
           | WORD NAME
           | WEATHER NAME
    '''
    p[0] = (p[1], p[2])


def p_error(p):
    print("Syntax error in input:", p)


def open_document(filename):
    extensions = (".txt", ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx")
    paths = (os.getcwd(), os.path.expanduser("~\\Documents"), os.path.expanduser("~\\Downloads"))
    for path in paths:
        for root, dirs, files in os.walk(path):
            matching_files = [file for ext in extensions for file in files if file.startswith(filename) and file.endswith(ext)]
            if matching_files:
                file_path = os.path.join(root, matching_files[0])
                try:
                    os.startfile(file_path)
                    return
                except FileNotFoundError:
                    pass
                except Exception as e:
                    print(e)
    print(f"File with name '{filename}' not found.")


def search_website(query):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_CUSTOM_SEARCH_API_KEY}&cx={GOOGLE_CUSTOM_SEARCH_CX_ID}"
    response = requests.get(url)
    results = response.json()
    if "items" in results:
        first_result = results["items"][0]
        print("Opening:", first_result["link"])
        webbrowser.open(first_result["link"])
    else:
        print("Website not found.")


def play_song(song_title):
    results = YoutubeSearch(song_title, max_results=1).to_dict()
    video_id = results[0]["id"]
    url = "https://www.youtube.com/watch?v=" + video_id
    webbrowser.open(url)


def get_definition(word, max_sent=5):
    wikipedia = wikipediaapi.Wikipedia(language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)
    page = wikipedia.page(word)
    if not page.exists():
        return f'No definition found for "{word}" on Wikipedia.'
    text_parser = PlaintextParser.from_string(page.text, Tokenizer("english"))
    summary = summarizer(text_parser.document, max_sent)
    return "\n".join([str(sentence) for sentence in summary])


def get_weather_info(location):
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPEN_WEATHER_MAP_API_KEY}&units=metric"
    response = requests.get(weather_api_url)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = f"Temperature in {location}: {weather_data['main']['temp']}°C."
        humidity = f"Humidity in {location}: {weather_data['main']['humidity']}%."
        pressure = f"Atmospheric pressure in {location}: {weather_data['main']['pressure']} hPa."
        description = f"Weather description in {location}: {weather_data['weather'][0]['description']}."
        return "\n".join([temperature, humidity, pressure, description])
    else:
        return f"Failed to retrieve weather information for {location}."


def voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio).casefold()
        parsed_text = parser.parse(text)
        if parsed_text:
            execute_command(parsed_text)
    except sr.UnknownValueError:
        print("Couldn't understand audio request.")
    except sr.RequestError as e:
        print("Request error:", e)


def execute_command(tokens):
    if tokens[0] == 'open':
        if tokens[1][0] in ('app', 'application'):
            open(tokens[1][1])
        elif tokens[1][0] in ('doc', 'document'):
            open_document(tokens[1][1])
        elif tokens[1][0] in ('website', 'webpage'):
            search_website(tokens[1][1])
    elif tokens[0] == 'close':
        if tokens[1][0] in ('app', 'application'):
            close(tokens[1][1])
    elif tokens[0] == 'play':
        if tokens[1][0] in ('song', 'video'):
            play_song(tokens[1][1])
    elif tokens[0] == 'define':
        if tokens[1][0] == 'word':
            definition = get_definition(tokens[1][1], max_sent=5)
            print(definition)
    elif tokens[0] == 'check':
        if tokens[1][0] == 'weather':
            weather_info = get_weather_info(tokens[1][1])
            print(weather_info)
    elif tokens[0] in ('voice', 'speech', 'audio'):
        if tokens[1] in ('input', 'recognition'):
            voice_input()
    elif tokens[0] in ('exit', 'quit'):
        exit()


if __name__ == '__main__':
    lexer = lex.lex()
    parser = yacc.yacc()
    summarizer = LsaSummarizer()
    recognizer = sr.Recognizer()
    while True:
        try:
            command = input("How can I help you?: ").casefold()
            result = parser.parse(command)
            if result:
                execute_command(result)
        except EOFError:
            continue
