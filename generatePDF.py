from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from textwrap import wrap

def GeneratePDF(nome_pdf, text):
    try:
        img_file = 'base.jpg' 
        
        pdf = canvas.Canvas(nome_pdf+'.pdf', pagesize="letter")
        x_start = 21*cm
        y_start = 29.7*cm
        pdf.drawImage(img_file, 0, 10, x_start, y_start ,mask='auto')
        
        pdf.setTitle(nome_pdf) 
        pdf.setFillColorRGB(1,1,1)
        pdf.setFont("Helvetica-Oblique", 27)
        pdf.drawString(80,700,nome.capitalize())

         
        pdf.setFillColorRGB(0,0,0) 
        wraped_text = "\n".join(wrap(text, 70))
        t = pdf.beginText()
        t.setFont('Helvetica', 10)
        t.setCharSpace(3)
        t.setTextOrigin(50, 400)   
        t.textLines(wraped_text) 
        pdf.drawText(t)
        pdf.showPage()
        pdf.save()


    except: 
        print('Erro ao gerar {}.pdf'.format(nome_pdf)) 

nome = input("Enter pdf file title: ")
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ac felis tincidunt mauris fermentum posuere. Nullam placerat scelerisque tortor sit amet pretium. Nulla facilisi. Aliquam quis magna accumsan, facilisis purus eget, tincidunt enim. Nulla ex sapien, facilisis in tempor vitae, elementum vitae eros. Sed volutpat auctor turpis, ut posuere nibh maximus at. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam vitae aliquet felis, ac congue tellus. Suspendisse ut consectetur ligula, a feugiat orci. Aenean fermentum accumsan vestibulum. Nam erat velit, faucibus ut neque vitae, vulputate porta ligula. Integer efficitur eu erat efficitur imperdiet. Morbi sed fringilla ex, ut dapibus risus. Pellentesque varius aliquet erat, non porttitor dolor posuere vel. Donec id enim ac ante tristique tincidunt vitae vel urna. Nam vehicula sit amet sem id blandit."
GeneratePDF(nome, text)