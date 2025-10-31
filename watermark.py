import fitz  
input_pdf = "input.pdf"        
output_pdf = "output_clean.pdf" 
WATERMARK_AREA = fitz.Rect(150, 780, 450, 820) 

doc = fitz.open(input_pdf)
for page in doc:
    page.draw_rect(WATERMARK_AREA, color=(1, 1, 1), fill=(1, 1, 1))
doc.save(output_pdf)

print("✅ Done! Watermark hidden in all pages →", output_pdf)
