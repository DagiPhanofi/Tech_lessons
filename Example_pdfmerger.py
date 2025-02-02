#%%
import PyPDF2
import os

merger = PyPDF2.PdfWriter()

pdf_files_folder = 'C:/Users/DagmawiAlemayehu/Downloads/test_pdf'


#for file in os.listdir(os.curdir):
for file in os.listdir(pdf_files_folder):    
    if file.endswith(".pdf"):
        print(f'PDF file: {file}')
        pdf_obj = PyPDF2.PdfReader(pdf_files_folder +'/'+file)
        merger.append(pdf_obj)

merger.write("combined.pdf")
merger.close()



# %%
