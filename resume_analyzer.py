import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        print("Error reading PDF:", e)
    return text

def analyze_resume(text):
    skills = ["Python", "Java", "C++", "Machine Learning", "Data Science"]
    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills

def main():
    file_path = input("Enter resume PDF path: ")
    text = extract_text_from_pdf(file_path)

    if text:
        skills = analyze_resume(text)
        print("\nDetected Skills:")
        for skill in skills:
            print("-", skill)
    else:
        print("No text extracted.")

if __name__ == "__main__":
    main()