import pdfplumber

def extract_pdf_layout(pdf_path):
    pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            words = page.extract_words(
                use_text_flow=True,
                x_tolerance=2,
                y_tolerance=2,
                keep_blank_chars=False
            )

            pages.append({
                "page": i + 1,
                "width": page.width,
                "height": page.height,
                "words": words
            })

    return pages
