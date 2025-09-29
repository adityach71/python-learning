import PyPDF2

def merge_pdfs(pdf_list, output):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output)
    merger.close()
    print(f"✅ PDFs merged successfully into {output}")

if __name__ == "__main__":
    pdfs = ["1.pdf", "2.pdf", "3.pdf"]  # put your pdf names here
    merge_pdfs(pdfs, "merged.pdf")