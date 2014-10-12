from ABBYY import CloudOCR

ocr_engine = CloudOCR(application_id='Project-X', password='nPo5B3ezoaI9GgS5YuJWT1ZV')
pdf = open('img/Edited1.png', 'rb')
file = {pdf.name: pdf}
result = ocr_engine.process_and_download(file, exportFormat='xml,pdfTextAndImages', language='English')
print(result['pdfTextAndImages'])
print(result['xml'])