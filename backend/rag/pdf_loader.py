import fitz


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts all text from the uploaded PDF.

    Args:
        pdf_path (str): Path to uploaded PDF.

    Returns:
        str: Complete extracted text.
    """

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text