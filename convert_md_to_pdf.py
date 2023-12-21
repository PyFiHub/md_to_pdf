import markdown
import pdfkit #https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf

def markdown_to_pdf(md_file, pdf_file):
    # Read Markdown file content
    with open(md_file, "r", encoding="utf-8") as file:
        md_text = file.read()

    # Convert Markdown to HTML
    html = markdown.markdown(md_text)

    # Write HTML to file
    html_file = "temp.html"
    with open(html_file, "w", encoding="utf-8") as file:
        file.write(html)

    # Convert HTML to PDF
    options = {
        'page-size': 'A4',
        'margin-top': '5mm',
        'margin-right': '5mm',
        'margin-bottom': '5mm',
        'margin-left': '5mm',
    }
    pdfkit.from_file(html_file, pdf_file, options=options)

if __name__ == "__main__":
    markdown_file_path = "markdown_file.md"
    pdf_file_path = "output.pdf"

    markdown_to_pdf(markdown_file_path, pdf_file_path)
