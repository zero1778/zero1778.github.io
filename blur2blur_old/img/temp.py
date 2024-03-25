from pdf2image import convert_from_path

# Specify the path to your PDF file
name = "Overview"
pdf_file = "{}.pdf".format(name)

# Convert the PDF to images (default output format is JPEG)
images = convert_from_path(pdf_file)

# Save each image as a separate file (optional)
for i, image in enumerate(images):
    image.save(f"{name}.jpg", "JPEG")