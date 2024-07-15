import tkinter as tk
from tkinter import messagebox

def get_response(user_input):
    user_input = user_input.lower()
    
    hellow = ["hi", "hello", "hello there"]
    ug = ["I want to know about the UG programmes offered", "what are the branches offered in this institute for UG", "courses offered in UG"]
    pg = ["I want to know about the PG programmes offered", "what are the branches offered in this institute for PG", "courses offered in PG"]
    doctoral = ["I want to know about the doctoral programmes offered", "what are the branches offered in this institute for doctoral", "doctoral programmes offered"]
    eligibility = ["what are the eligibility requirements at the UG level?", "what are the eligibility requirements at the PG level?", "what are the eligibility requirements at the doctoral level?"]
    affiliation = ["does CMRIT have necessary affiliations?", "what affiliations does CMRIT have?"]
    admission = ["when does the admission process begin and close?", "when does the admission process begin and end?"]
    classes = ["when do the classes begin?", "when do the classes start?"]
    process = ["what is the admission process to this institute?", "how can we get admission into this institute?", "which entrance exams does one need to give for admission in this institute?", "admission process"]
    hostel = ["is there any hostel facility available?", "what are the hostel facilities available?", "hostel facility"]
    career = ["what are the career placement facilities available in this college?", "career placement facilities"]
    company = ["which companies visit CMRIT for placements?", "visiting companies"]
    library = ["what are the library timings?", "library hours", "library timings"]

    if user_input in hellow:
        return "Hello! How may I help you?"
    elif user_input in ug:
        return "UG courses:\n\tComputer Science Engineering\n\tInformation Science Engineering\n\tElectronics & Communication Engineering\n\tElectrical & Electronics Engineering\n\tCivil Engineering\n\tMechanical Engineering\n\tArtificial Intelligence and Machine Learning\n\tArtificial Intelligence and Data Science"
    elif user_input in pg:
        return "PG courses:\n\tMCA | Masters of Computer Applications\n\tMBA | Masters of Business Administration\n\tM.Tech | VLSI Design and Embedded Systems"
    elif user_input in doctoral:
        return "Doctoral programs:\n\tPh.D | Computer Applications\n\tPh.D | Business Administration\n\tPh.D | Engineering\n\tPh.D | Sciences\n\tPh.D | Civil Engineering"
    elif user_input in eligibility:
        return "To know about the admission criteria email at: admission@cmrit.ac.in or call our admission hotline: 93429 00666"
    elif user_input in affiliation:
        return "Yes. The CMR Institute of Technology is affiliated to Visvesvaraya Technological University, and is approved by AICTE New Delhi. Recognizing the high standards maintained by the college in offering quality technical education, the National Board of Accreditation (NBA), a national body set up under AICTE, has awarded accreditation status to all departments at CMRIT."
    elif user_input in admission:
        return "The admission process usually begins in January and ends by September or October."
    elif user_input in classes:
        return "Classes start around August or September each year, but the exact dates are fixed by the University."
    elif user_input in process:
        return "One can take admission in this institute either through KCET or COMED-K."
    elif user_input in hostel:
        return "CMRIT provides hostel accommodation on the campus, with separate hostel facilities for boys and girls. Vigilant wardens and a team of round-the-clock security staff ensure the safety of students and maintain the security of the facilities. The hostel rooms are well-lit and well-ventilated. There is access to Wi-Fi internet.\n\tAn experienced team of kitchen staff cooks healthy and tasty meals of both North Indian and South Indian recipes. For students who stay in the hostel accommodation, three meals with snacks are provided daily.\n\tIn the case of any medical emergency, immediate arrangements will be made for the best medical care. The college library is open till 10.00 pm, and students may avail of this facility. There is also a well-equipped fitness centre on the campus."
    elif user_input in career:
        return "CMRIT's Career Guidance & Placement Bureau assists all CMR students in finding the best placement opportunities. The Placement Bureau has strong connections with a number of recruiting companies and assists numerous students in finding excellent job opportunities at leading corporates every year."
    elif user_input in company:
        return "Some of the major companies that have recruited CMRIT students in the past are: Tata Consultancy Services, Wipro, Subex, Sonata Software, Sungard, Sony, Microsoft, Sasken, Accord, I-Gate, Birlasoft, Mphasis, HP, HCL, Huawei Tech, Tech Mahindra, IBM, JP Morgan, Zenith Software, Tata Elxi, Patni Computers, DELL, Deloitte, Standard Chartered Bank, HDFC Bank, Metlife Insurance, GE Capital, L&T Infotech, ICICI Prudential, Bosch, Oracle, Max New York Life Insurance, Cap Gemini, Ernst & Young, Razor Think, Amazon, Marine Services Ltd, CISCO. Many Indian and multinational companies continue to visit the campus every year for recruitments."
    elif user_input in library:
        return "Library Timings:\n\tDuring Working Days: 7:30am to 10:30pm\n\tDuring Holidays: 7.30am to 4.30pm\n\tDuring Weekend and Vacation: 7.30am to 6.00pm\n\tDuring Examination: 7.30am to 12 midnight"
    else:
        return 'For any other enquiries visit our website: cmrit.ac.in'

def on_submit():
    user_input = entry.get()
    response = get_response(user_input)
    messagebox.showinfo("Genie", response)

# Set up the GUI
root = tk.Tk()
root.title("CMRIT College Guide")

label = tk.Label(root, text="Genie-Hello!\nWelcome to CMR Institute of Technology!\nI am Genie, your college guide.\nI am here to assist you with the FAQs and your general queries about our institution.\n\n")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
