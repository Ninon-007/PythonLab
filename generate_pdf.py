from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        if self.page_no() == 1:
            self.cell(0, 10, 'Python String Programs', 0, 1, 'C')
            self.ln(10)

    def chapter_title(self, label):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, label, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                txt = f.read()
            self.set_font('Courier', '', 10)
            self.multi_cell(0, 5, txt)
            self.ln()
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

pdf = PDF()
pdf.add_page()

# Questions mapping
questions = {
    "string1.py": "1. Write a program to remove all vowels from a string.",
    "string2.py": "2. Write a program to remove characters at odd index positions from a string.",
    "string3.py": "3. Check whether a string is palindrome or not.",
    "string4.py": "4. Write a program to replace all the spaces in the input string with * or if no spaces found, put $ at the start and end of string.",
    "string5.py": "5. Write a program to slice string into two separate strings; one with all the characters in the odd indices and one with all characters in even indices.",
    "string6.py": "6. Write a program to remove all occurrence of a substring from a string.",
    "string7.py": "7. Write a program to convert all lowercase into uppercase.",
    "string8.py": "8. Write a program to reverse first and second half of a string separately.",
    "string9.py": "9. Write a program to replace all occurrence of a substring with a new substring.",
    "string10.py": "10. Write a python program to check validity of password given by user.\nPassword should satisfy following criteria :-\n- Contains atleast one letter between 'a' and 'z'.\n- Contains atleast one number between 0 and 9.\n- Contains atleast one letter between A and Z.\n- Contains atleast one special character from $, #, @\n- Minimum length of password : 6"
}

# List of files to include
files = [f"string{i}.py" for i in range(1, 11)]

for file in files:
    if os.path.exists(file):
        question = questions.get(file, "")
        pdf.chapter_title(f"Program: {file}")
        
        # Print Question
        pdf.set_font('Arial', 'I', 11)
        pdf.multi_cell(0, 5, f"Question: {question}")
        pdf.ln(4)
        
        # Print Code
        pdf.chapter_body(file)
        
        if files.index(file) < len(files) - 1:
            pdf.add_page()
    else:
        print(f"Warning: {file} not found")

output_file = "String_Programs_Lab_With_Questions.pdf"
pdf.output(output_file)
print(f"PDF generated successfully: {output_file}")
