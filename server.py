from ABBYY import CloudOCR
from PIL import Image
import pdb, traceback, code, sys

ocr_engine = CloudOCR(application_id='Project-X', password='nPo5B3ezoaI9GgS5YuJWT1ZV')
pdf = open('img/Edited1.png', 'rb')
file = {pdf.name: pdf}
result = ocr_engine.process_and_download(file, exportFormat='xml,pdfTextAndImages', language='English')

traceback.print_exc()
code.interact(local=locals())
print(result['pdfTextAndImages'])
print(result['xml'])


img = Image.open('./img/t1.jpeg')
img.save(result['pdfTextAndImages'], format='JPEG')