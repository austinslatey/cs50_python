from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')

def generate_shirtificate(name):
    pdf = Shirtificate('P', 'mm', 'A4')
    pdf.add_page()

    # Set font for the name
    pdf.set_font('Arial', 'B', 24)

    # Calculate position for name
    name_width = pdf.get_string_width(name)
    name_x = (210 - name_width) / 2  # Center horizontally
    name_y = 160  # Position on top of the shirt

    # Add name to the shirt
    pdf.set_text_color(255, 255, 255)  # White color
    pdf.text(name_x, name_y, name)

    # Add shirt image
    pdf.image('shirtificate.png', x=30, y=50, w=150)

    # Save PDF to file
    pdf_file = 'shirtificate.pdf'
    pdf.output(pdf_file)
    print(f"Shirtificate generated for {name} as '{pdf_file}'.")

if __name__ == "__main__":
    name = input("Enter your name: ")
    generate_shirtificate(name)
