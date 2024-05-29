from fpdf import FPDF
import pandas as pd

# creating an fpdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    
    # set the header
    pdf.set_font(family="Times", size=20, style="B")
    pdf.set_text_color(231, 52, 78)
    pdf.cell(w=0, h=20, txt=row["Topic"], align='L', ln=1)
    pdf.line(10,25,200,25)    #for the horizontal line
    
    # set the footer
    pdf.ln(254)
    pdf.set_font(family="Times", size=12, style="B")
    pdf.set_text_color(231, 52, 78)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='R', ln=1)
    
    
    pageCount = row["Pages"]
    for i in range(pageCount-1):
        pdf.add_page()
        pdf.ln(274)
        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(231, 52, 78)
        pdf.cell(w=0, h=12, txt=row["Topic"], align='R', ln=1)
    
pdf.output("Output.pdf")