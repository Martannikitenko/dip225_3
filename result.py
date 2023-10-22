import os
import PyPDF2
import pathlib

folder="invoices"
nordpool_price=0.12575 #nordpool avarage price at 01.03.2023

adrese = pathlib.Path("invoices/invoice_2.pdf")
pdf_file=PyPDF2.PdfReader(open(adrese,"rb"))
number_of_pages=len(pdf_file.pages) 
#print (number_of_pages)
page1=pdf_file.pages[0]
text1=page1.extract_text()
pos1 = text1.find("Apmaksai:")
pos2 = text1.find("Elektroenerģijas patēriņš kopā")
pos3 = text1.find("kWh")
pos4 = text1.find("Elektroenerģijas pārvade un sadale")
#print (pos1, pos2)
summa = text1[pos1+10:pos2].rstrip()
summa=summa.strip()
summa=summa.replace(",",".")
summa=float (summa)
#print(summa)
kWh=text1[pos2+31:pos3].rstrip()
kWh=kWh.strip()
kWh=kWh.replace(",",".")
kWh=kWh.replace(" ","")
kWh=float (kWh)
#print (kWh)
parvade= text1[pos4+34:pos4+40].rstrip()
parvade=parvade.strip()
parvade=parvade.replace(",",".")
parvade=float(parvade)
#print (parvade)
nordpool_atmaksa = kWh*nordpool_price
#print(nordpool_atmaksa)
ietaupijums=summa-parvade-nordpool_atmaksa

print ("{:.1f}".format(ietaupijums))

