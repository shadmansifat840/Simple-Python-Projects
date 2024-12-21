# Importing some external modules.

import pyjokes
import pyttsx3

# code to print the joke.

jks = pyjokes.get_joke()
print(jks)

# code to listen the code.

engine = pyttsx3.init()
engine.say(jks)
engine.runAndWait()

"""Want to run this code, but don't know how ?
just run this command in your terminal.
command : pip install pyjokes pyttsx3
after it completes installing all the files,
you just have to copy and paste the above code."""

