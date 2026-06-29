import fitz  # PyMuPDF
import os

pdf_path = "/Users/max/Waste/marketing/brochure.pdf"
output_dir = "/Users/max/Waste/marketing/images"

doc = fitz.open(pdf_path)
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=150)  # Render at 150 DPI for clear text and layout
    output_path = os.path.join(output_dir, f"inspect_page_{i+1}.png")
    pix.save(output_path)
    print(f"Rendered Page {i+1} to {output_path}")
