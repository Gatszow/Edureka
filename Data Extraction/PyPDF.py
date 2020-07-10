import PyPDF2 as p

with open(r'C:/Users/Takezaki/Desktop/Programowanie/Programy_stworzone/zadania1Python.pdf', 'rb') as file:
    pd = p.PdfFileReader(file)

    x = pd.getPage(0)
    y = pd.getPage(1)

    print(x.extractText())
    print(y.extractText())