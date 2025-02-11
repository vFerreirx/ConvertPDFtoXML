import os
import fitz 
import xml.etree.ElementTree as ET


pasta_pdf = "pdfs"  
pasta_xml = "xmls"  

os.makedirs(pasta_xml, exist_ok=True)

def pdf_para_xml(pdf_path, xml_path):
    doc = fitz.open(pdf_path)
    root = ET.Element("documento")

    for num, page in enumerate(doc, start=1):
        pagina = ET.SubElement(root, "pagina", numero=str(num))
        pagina.text = page.get_text("text") 

    tree = ET.ElementTree(root)
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)

for arquivo in os.listdir(pasta_pdf):
    if arquivo.endswith(".pdf"):
        pdf_path = os.path.join(pasta_pdf, arquivo)
        xml_path = os.path.join(pasta_xml, arquivo.replace(".pdf", ".xml"))
        pdf_para_xml(pdf_path, xml_path)
        print(f"Convertido: {arquivo} -> {xml_path}")

print("Conversão concluída!")
