import PyPDF2 as pd
from gtts import gTTS
import streamlit as st


st.title("pdf reader")

path = open('Cracking_the_Coding_Interview_6th_Editio.pdf', 'rb')   # opening the pdf

pdfreader = pd.PdfFileReader(path)  # reading the pdf

paged = pdfreader.numPages  # paged object will contain the number of pages our pdf has

page = pdfreader.getPage(24)  # giving the page number of pdf which we wanna our computer to read

p_text = page.extractText()  # extracting the text from pdf and from given page number

P_lines=p_text.splitlines()  # since the extracted text has new line after every word so i first convert it into string -
line = "".join(P_lines)  # and then again to string

print(line)


# making and saving audio file
# obj = gTTS(f'{line}')
# obj.save('pdf25.mp3')
#



def convert_to_audio(text):
    audio =gTTS(text=text, lang='en', tld='com')
    audio.save("textaud.mp3")


convert_to_audio(line)

audio_file = open("textaud.mp3", "rb")

st.audio(audio_file.read())