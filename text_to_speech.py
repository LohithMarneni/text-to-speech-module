from gtts import gTTS
import os
def pronounce(list_of_words):
    speech=" ".join(list_of_words)
    tts=gTTS(text=speech,lang="en")
    tts.save("pronounciation.mp3")
    os.system("start pronounciation.mp3")

if __name__=="__main__":
    list_of_words=["The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the time module in Python and see how it can be used in different scenarios."]
    pronounce(list_of_words)