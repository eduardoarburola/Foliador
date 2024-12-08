from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj
from tkinter import filedialog as fd
import os
import tkinter

import tkinter as tk
from tkinter import simpledialog
ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
#USER_INP = simpledialog.askstring(title="Ceros iniciales",prompt="Cuantos digitos para el Foliado:")
# check it out
#print("Hello", USER_INP)
#losceros=int(USER_INP)
#print(losceros)

#input_file = fd.askopenfilename()
#output_file = fd.asksaveasfile()

#input_file = "/Users/eduardoarburola/Python/my_file.pdf"

input_file  = fd.askopenfilename()


#print(input_file[:-4])

#output_file = "/Users/eduardoarburola/Python/my_file_with_footer.pdf"
output_file = input_file[:-4] + "_FOLIADO.pdf"


# Get pages
reader = PdfReader(input_file)
pages = [pagexobj(p) for p in reader.pages]


# Compose new pdf
canvas = Canvas(output_file)

for page_num, page in enumerate(pages, start=1):
    pagnumcero=10000+page_num
    pagnumstr=str(pagnumcero)
    pagnumstr = pagnumstr[1:]
    # Add page
    canvas.setPageSize((page.BBox[2], page.BBox[3]))
    canvas.doForm(makerl(canvas, page))

    # Draw footer
    #footer_text = "FOLIO N.º %s of %s" % (page_num, len(pages))
    footer_text= "FOLIO N.º %s" %(pagnumstr)
    x = 128
    canvas.saveState()
    canvas.setStrokeColorRGB(0, 0, 0)
    canvas.setLineWidth(0.5)
   # canvas.line(66, 78, page.BBox[2] - 66, 78)
   # canvas.line(margen iz, altura, page.BBox[2] - margen de, altura)

    #canvas.line(66, 740, page.BBox[2] - 66, 740)
    canvas.setFont('Times-Roman', 10)
    canvas.drawString(page.BBox[2]-x, 750, footer_text)
    canvas.restoreState()

    canvas.showPage()

canvas.save()

tkinter.messagebox.showinfo(title="Foliador", message="Foliado Completo")

