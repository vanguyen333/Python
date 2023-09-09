import pyttsx3
import PyPDF2
book = open('SE.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.numPages

bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice', voices[1].id)

for num in range(8, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()