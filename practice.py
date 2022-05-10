import PyPDF2 as pd
from gtts import gTTS

path = open('Cracking_the_Coding_Interview_6th_Editio.pdf', 'rb')   # opening the pdf

pdfreader = pd.PdfFileReader(path)  # reading the pdf

paged = pdfreader.numPages  # paged object will contain the number of pages our pdf has

page = pdfreader.getPage(25)  # giving the page number of pdf which we wanna our computer to read

p_text = page.extractText()  # extracting the text from pdf and from given page number

P_lines=p_text.splitlines()  # since the extracted text has new line after every word so i first convert it into string -
line = "".join(P_lines)  # and then again to string

print(line)


# making and saving audio file
obj = gTTS(f'{line}')
obj.save('pdf25.mp3')
