import tkinter as tk
from tkinter import ttk

def get_response(user_input):
    user_input = user_input.lower()

    hellow = ["hi", "hello", "hello there"]
    ug_keywords = ["ug", "undergraduate", "bachelor", "courses offered in ug", "branches for ug"]
    pg_keywords = ["pg", "postgraduate", "masters", "m.tech", "mba", "courses offered in pg", "branches for pg"]
    doctoral_keywords = ["phd", "doctoral", "research", "doctoral programmes"]
    eligibility_keywords = ["eligibility", "requirements", "criteria"]
    affiliation_keywords = ["affiliations", "accreditation", "affiliated"]
    admission_keywords = ["admission process", "admission dates", "admission open", "begin and close"]
    classes_keywords = ["classes start", "classes begin"]
    process_keywords = ["admission", "entrance exam", "kcet", "comed-k"]
    hostel_keywords = ["hostel", "accommodation", "facilities"]
    career_keywords = ["placement", "career support", "job opportunities"]
    company_keywords = ["companies visit", "recruiters", "placement companies","companies"]
    library_keywords = ["library timings", "library hours","library"]

    placement_keywords = ["average placement", "placement statistics", "placement package","average pakage"]
    skills_keywords = ["soft skill trainers", "placement guidance", "training for placements"]
    canteen_keywords = ["canteen", "cafeteria", "ccd", "food court"]
    auditorium_keywords = ["auditorium", "dwani", "events", "cultural activities"]

    if any(kw in user_input for kw in hellow):
        return "Hello! How may I help you?"
    elif any(kw in user_input for kw in ug_keywords):
        return "UG courses:\n\tComputer Science Engineering\n\tInformation Science Engineering\n\tElectronics & Communication Engineering\n\tElectrical & Electronics Engineering\n\tCivil Engineering\n\tMechanical Engineering\n\tArtificial Intelligence and Machine Learning\n\tArtificial Intelligence and Data Science"
    elif any(kw in user_input for kw in pg_keywords):
        return "PG courses:\n\tMCA | Masters of Computer Applications\n\tMBA | Masters of Business Administration\n\tM.Tech | VLSI Design and Embedded Systems"
    elif any(kw in user_input for kw in doctoral_keywords):
        return "Doctoral programs:\n\tPh.D | Computer Applications\n\tPh.D | Business Administration\n\tPh.D | Engineering\n\tPh.D | Sciences\n\tPh.D | Civil Engineering"
    elif any(kw in user_input for kw in eligibility_keywords):
        return "To know about the admission criteria email at: admission@cmrit.ac.in or call our admission hotline: 93429 00666"
    elif any(kw in user_input for kw in affiliation_keywords):
        return "Yes. The CMR Institute of Technology is affiliated to Visvesvaraya Technological University, and is approved by AICTE New Delhi. Recognizing the high standards maintained by the college in offering quality technical education, the National Board of Accreditation (NBA), a national body set up under AICTE, has awarded accreditation status to all departments at CMRIT."
    elif any(kw in user_input for kw in admission_keywords):
        return "The admission process usually begins in January and ends by September or October."
    elif any(kw in user_input for kw in classes_keywords):
        return "Classes start around August or September each year, but the exact dates are fixed by the University."
    elif any(kw in user_input for kw in process_keywords):
        return "One can take admission in this institute either through KCET or COMED-K."
    elif any(kw in user_input for kw in hostel_keywords):
        return "CMRIT provides hostel accommodation on the campus, with separate hostel facilities for boys and girls. Vigilant wardens and a team of round-the-clock security staff ensure the safety of students and maintain the security of the facilities. The hostel rooms are well-lit and well-ventilated. There is access to Wi-Fi internet.\n\tAn experienced team of kitchen staff cooks healthy and tasty meals of both North Indian and South Indian recipes. For students who stay in the hostel accommodation, three meals with snacks are provided daily.\n\tIn the case of any medical emergency, immediate arrangements will be made for the best medical care. The college library is open till 10.00 pm, and students may avail of this facility. There is also a well-equipped fitness centre on the campus."
    elif any(kw in user_input for kw in career_keywords):
        return "CMRIT's Career Guidance & Placement Bureau assists all CMR students in finding the best placement opportunities. The Placement Bureau has strong connections with a number of recruiting companies and assists numerous students in finding excellent job opportunities at leading corporates every year."
    elif any(kw in user_input for kw in company_keywords):
        return "Some of the major companies that have recruited CMRIT students in the past are: Tata Consultancy Services, Wipro, Subex, Sonata Software, Sungard, Sony, Microsoft, Sasken, Accord, I-Gate, Birlasoft, Mphasis, HP, HCL, Huawei Tech, Tech Mahindra, IBM, JP Morgan, Zenith Software, Tata Elxi, Patni Computers, DELL, Deloitte, Standard Chartered Bank, HDFC Bank, Metlife Insurance, GE Capital, L&T Infotech, ICICI Prudential, Bosch, Oracle, Max New York Life Insurance, Cap Gemini, Ernst & Young, Razor Think, Amazon, Marine Services Ltd, CISCO. Many Indian and multinational companies continue to visit the campus every year for recruitments."
    elif any(kw in user_input for kw in library_keywords):
        return "Library Timings:\n\tDuring Working Days: 7:30am to 10:30pm\n\tDuring Holidays: 7.30am to 4.30pm\n\tDuring Weekend and Vacation: 7.30am to 6.00pm\n\tDuring Examination: 7.30am to 12 midnight"
    
    elif any(kw in user_input for kw in placement_keywords):
        return "The average placement package at CMRIT is around 7 LPA (Lakhs Per Annum)."
    elif any(kw in user_input for kw in skills_keywords):
        return "Yes, we have soft skill trainers and placement guidance to help students prepare for their interviews and job placements."
    elif any(kw in user_input for kw in canteen_keywords):
        return "Yes, we have a well-maintained canteen and a Café Coffee Day (CCD) outlet on campus. The canteen offers a variety of food and snacks."
    elif any(kw in user_input for kw in auditorium_keywords):
        return "CMRIT has an auditorium named 'Dwani', which is used for cultural events, seminars, and conferences."
    
    else:
        return 'For any other enquiries visit our website: cmrit.ac.in'

def on_submit():
    user_input = question_combobox.get()
    response = get_response(user_input)
    response_text.delete(1.0, tk.END)
    response_text.insert(tk.END, response)

root = tk.Tk()
root.title("CMRIT College Guide")
root.geometry("600x600")
root.config(bg="#f0f0f0")

label = tk.Label(root, text="Genie-Hello!\nWelcome to CMR Institute of Technology!\nI am Genie, your college guide.\nI am here to assist you with the FAQs and your general queries about our institution.\n", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

questions = [
    "What are the branches offered in this institute for UG?",
    "What is the admission process?",
    "Does CMRIT have hostel facilities?",
    "Which companies visit CMRIT for placements?",
    "What is the average placement package?",
    "Is there a canteen or cafeteria?",
    "What is the average package of the college?"
]

question_combobox = ttk.Combobox(root, values=questions, width=50, font=("Arial", 12))
question_combobox.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
submit_button.pack(pady=10)

response_text = tk.Text(root, height=10, width=60, font=("Arial", 12), wrap=tk.WORD)
response_text.pack(pady=10)

scrollbar = tk.Scrollbar(root, command=response_text.yview)
response_text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

root.mainloop()
