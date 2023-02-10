import pyttsx3
from PyPDF2 import PdfReader

def convAll(numPages, reader):
    print("Converting all the pdf")
    pag=0
    longtext=''
    clean_text=''
    for pag in range(numPages):
        page=reader.pages[pag-1]
        text = page.extract_text(0)
        clean_text=clean_text+text.strip().replace('\n', ' ')
        longtext=longtext+text
    speaker.save_to_file(clean_text, 'pdfDocument.mp3')
    speaker.runAndWait()
    speaker.stop()
    print("Process Finished :D")

def convSingle(numPages, reader):
    print("This option are are 'Convert a single page")
    try:
        pag=int(input("wich page would you want to convert?\n=> "))
    except ValueError:
        print("Invalid page, I will convert the first page", ValueError)
        pag=1
    if pag>numPages:
        pag=numPages
    elif pag<=0:
        pag=1
    page=reader.pages[pag-1]
    text = page.extract_text(0)
    clean_text=text.strip().replace('\n', ' ')
    speaker.save_to_file(clean_text, 'pdfSinglePage.mp3')
    speaker.runAndWait()
    speaker.stop()
    print("Process Finished :D")

def convInterval(numPages, reader):
    print("This option are are 'Convert a interval of pages in pdf'")
    try:
        pag=int(input("from wich page would you want to convert?\n=> "))
    except ValueError:
        print("Invalid page, I will convert from the first page", ValueError)
        pag=1
    try:
        pag2=int(input("to wich page would you want to convert?\n=> "))
    except ValueError:
        print("Invalid page, I will convert to the last page", ValueError)
        pag2=numPages
    #el intervalo puede ser inverso (primero pag 2 antes que pag)
    if pag2<=pag:
        print("Invalid interval, I will convert from the first page to second page")
        pag=1
        pag2=2
    #el intervalo es correcto pero pag2 está fuera de numPages (pag2>numPages)
    elif pag<pag2 and pag2>numPages:
        pag2=numPages
        print(f"Invalid interval, I will convert from page {pag} to {numPages}")
    #el intervalo es correcto pero pag está fuera de numPages (es menor a cero)
    elif pag<pag2 and pag<=0:
        pag=1
        print(f"Invalid interval, I will convert from page {pag} to {numPages}")
    longtext=''
    clean_text=''
    for pag in range(pag, pag2):
        page=reader.pages[pag-1]
        text = page.extract_text(0)
        clean_text=clean_text+text.strip().replace('\n', ' ')
        longtext=longtext+text
    speaker.save_to_file(clean_text, 'pdfRangeDocument.mp3')
    speaker.runAndWait()
    speaker.stop()
    print("Process Finished :D")

print("First. Make you shure that pdf that would be converted on mp3 are on this current folder")
nameofpdf=input("Hey! can you show me what's the name of your book? pls end with '.pdf' => ")
reader=''
if nameofpdf.endswith('.pdf'):
    nameofpdf=nameofpdf
else:
    nameofpdf=nameofpdf+".pdf"

try:
    reader = PdfReader(open(nameofpdf, "rb"))
    number_of_pages = len(reader.pages)
except ValueError:
    print("Can't open the file", nameofpdf)
optionToConvert=input("would you like to: \n [a] Convert all the pdf \n [b] Convert a single page \n [c] Convert a range of pages \n => ")
optionToConvert.lower()
speaker=pyttsx3.init()

if optionToConvert.startswith("a"):
    convAll(number_of_pages, reader)

elif optionToConvert.startswith("b"):
    convSingle(number_of_pages, reader)

elif optionToConvert.startswith("c"):
    print("This option are on maintenance")
    convInterval(number_of_pages, reader)