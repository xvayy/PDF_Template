from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="p", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 22, 200, 22)

    #Generate lines
    x1, y1, x2, y2 = 10, 30, 200, 30
    while y1 <= 285 and y2 <=285:
        pdf.line(x1, y1, x2, y2)
        y1 = y1 + 8
        y2 = y2 + 8

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 0, 0)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Generate lines
        x1, y1, x2, y2 = 10, 30, 200, 30
        while y1 <= 285 and y2 <= 285:
            pdf.line(x1, y1, x2, y2)
            y1 = y1 + 8
            y2 = y2 + 8

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 0, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")