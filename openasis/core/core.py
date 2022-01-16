import re
import webbrowser

def take_query(raw_command):
    command = raw_command.lower().split()
    if command[0] == 'open':
        if command[1] == 'duckduckgo':
            webbrowser.open("https://duckduckgo.com/")
            return 'Opening duckduckgo.com'
        elif command[1] == 'google':
            webbrowser.open('https://google.com/')
            return 'Opening google.com'
    elif command[0] == 'search':
        if 'with duckduckgo' in raw_command.lower():
            webbrowser.open('https://duckduckgo.com/?q=' + replace_ignore_case( replace_ignore_case(raw_command, 'search',  ''), 'with duckduckgo', ''))
            return 'Searching...'
    else:
        return "I can't understand you."

def replace_ignore_case(text, what_to_replace, replace_with):
    compiled = re.compile(re.escape(what_to_replace), re.IGNORECASE)
    return compiled.sub(replace_with, text)