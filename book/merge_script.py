from pypdf import PdfReader, PdfWriter

def merge_pdfs():
    main_pdf = PdfReader('main.pdf')
    front_pdf = PdfReader('front page.pdf')
    last_pdf = PdfReader('last page.pdf')
    
    writer = PdfWriter()
    
    # 1. Add front page.pdf
    for page in front_pdf.pages:
        writer.add_page(page)
        
    # 2. Add main.pdf but skip the first page (index 0)
    for i, page in enumerate(main_pdf.pages):
        if i == 0:
            continue
        writer.add_page(page)
        
    # 3. Add last page.pdf
    for page in last_pdf.pages:
        writer.add_page(page)
        
    # Save to a new file
    with open('main_final.pdf', 'wb') as f:
        writer.write(f)
        
if __name__ == "__main__":
    merge_pdfs()
    print("Merged successfully into main_final.pdf")
