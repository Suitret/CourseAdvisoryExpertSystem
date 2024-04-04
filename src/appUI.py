import tkinter as tk
from tkinter import *
from pyswip import Prolog

from PIL import ImageTk, Image


titleFont = "Helvetica", 16, 'bold'
titleText = 'Welcome to Course Advisory Expert System'
headingFont = "Helvetica", 12, 'bold'
btnFont = "Helvetica", 10
basicFont = "Helvetica", 11
baseColor = '#a11b00'#lightblue
textColor = 'white'
titleBg = '#00195c'
titleFg = '#ffa000'


class PrologBackend:
    def __init__(self, prolog_file):
        self.prolog = Prolog()
        self.prolog.query("trace")
        self.prolog.consult(prolog_file)
        
        #self.prolog.query("debug.")
        #self.prolog.query('set_prolog_flag("debug", "on")')
        #self.prolog.load(prolog_file)
        #self.prolog.query("set_prolog_flag(debug, off)")

    def get_compulsory200(self):
        return list(course['X'].decode('utf-8') for course in self.prolog.query("(compulsory(X); uni_course(X); nuc_course(X)), course200a(X)"))

        
    def get_nonCompulsory200(self):
        return list(course['X'].decode('utf-8') for course in self.prolog.query("course200a(X), elective(X)"))


    def add_fact(self, predicate, arg):
        fact = f"{predicate}({arg})"
        self.prolog.assertz(fact)

    def get_fullName(self, courseCode):
        dict_courses = {
                            "acc111": "ACC111 Principles of Accounting",
                            "csc111": "CSC111 Introduction to Computer Science",
                            "ecn111": "ECN111 Introduction to Economics",
                            "mat111": "MAT111 Algebra",
                            "mat112": "MAT112 Trigonometry and Analytical Geometry",
                            "phy111": "PHY111 Mechanics and Properties of Matter",
                            "cst111": "CST111 Use of Library, Study Skills and ICT I",
                            "gst111": "GST111 Communication in English",
                            "cit111": "CIT111 Microsoft Office Specialist",
                            "eds111": "EDS111 Entrepreneurial Development Studies",
                            "tmc111": "TMC111 Total Man Concept I",
                            "tmc112": "TMC112 Total Man Concept - Sports I",
                            "bfn211": "BFN211 Business Finance",
                            "bus211": "BUS211 Principles of Management I",
                            "cit211": "CIT211 Java Foundations Certified Junior Associate",
                            "csc211": "CSC211 Computer Progamming",
                            "csc213": "CSC213 Structured Programming",
                            "csc214": "CSC214 High Performance Computing & Database Management I",
                            "cbs111": "CBS111 Mathematics for Business and Social Sciences I",
                            "mat214": "MAT214 Linear Algebra",
                            "gst211": "GST211 Logic Philosophy and Human Existence",
                            "dld111": "DLD111 Foundations of Leadership Development",
                            "eds211": "EDS211 Entrepreneurial Development Studies III",
                            "tmc211": "TMC211 Total Man Concept III",
                            "tmc212": "TMC212 Total Man Concept - Sports III"       
                                                                                    }
        return dict_courses[courseCode]


    def get_failed_courses(self):
        courseCodes = [course['X'] for course in self.prolog.query("failed(X)")]
        return courseCodes

    def credit_course(self, course):
        credit = [cred['X'] for cred in self.prolog.query(f'credit("{course}", X)')]
        return credit[0]

    def sum_credits(self, course_codes):
        total_credits = 0
        for course_code in course_codes:
            query = f'credit("{course_code}", Credits)'
            for result in self.prolog.query(query):
                total_credits += int(result['Credits'])
        return total_credits

    def get_recommended_courses(self):
        return






class Interface(tk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.create_widgets()
        #self.checkedArray = []
        self.courseSelectionArray = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

    def create_widgets(self):
        welcomeFrame = tk.Frame(self)
        welcomeFrame.grid(row=0, column=0, sticky='N')
        welcomeFrame.config(
            bg=baseColor
        )
        self.frame = welcomeFrame

        # Add Title Frame to Welcome Page Frame
        titleFrame = tk.Frame(welcomeFrame, bg=titleBg)
        titleFrame.grid(row=0, column=0, sticky='N', ipadx=400, pady=20)

        # Add Welcome Text to Title Frame
        welcomeLbl = tk.Label(welcomeFrame, text=titleText,
                              font=titleFont,
                              height=3, bg=titleBg, fg=titleFg)
        welcomeLbl.grid(row=0, column=0, columnspan=6, sticky='nEW')

        # Add Form Frame To Welcome Page Frame
        formFrame = tk.Frame(welcomeFrame,
                             bg=baseColor
                             )
        formFrame.grid(row=1, column=0, sticky='N', pady=20)

        # PERSONAL INFORMATION
        PersonalInfoLabel = tk.Label(formFrame, text="Personal Information", font=headingFont, bg=baseColor,
                                     fg=textColor)
        PersonalInfoLabel.grid(row=0, column=0, columnspan=6, pady=27)

        # Last Name label
        lastNameLabel = tk.Label(formFrame, text="Last Name", font=basicFont, bg=baseColor, fg=textColor)
        lastNameLabel.grid(row=1, column=0, sticky='w', pady=5)

        # Last Name Field
        self.lastNameEntry = tk.Entry(formFrame)
        self.lastNameEntry.grid(row=1, column=1, sticky='w', pady=5)

        # Add Space
        SpaceLabel = tk.Label(formFrame, text="   ",
                              font=basicFont, bg=baseColor, fg=textColor)
        SpaceLabel.grid(row=1, column=2, pady=5)

        # First Name Label
        firstNameLabel = tk.Label(formFrame, text="First Name", font=basicFont, bg=baseColor, fg=textColor)
        firstNameLabel.grid(row=2, column=0, sticky='w', pady=5)

        # First Name Entry
        self.firstNameEntry = tk.Entry(formFrame)
        self.firstNameEntry.grid(row=2, column=1, sticky='w', pady=5)

        # Matricule Label
        matriculeLabel = tk.Label(formFrame, text="Matric Number", font=basicFont, bg=baseColor, fg=textColor)
        matriculeLabel.grid(row=1, column=3, sticky='w', pady=5)

        # Matricule Entry
        self.matriculeEntry = tk.Entry(formFrame)
        self.matriculeEntry.grid(row=1, column=4, sticky='w', pady=5)

        # Add Space
        SpaceLabel = tk.Label(formFrame,
                              text="                                                                                           ",
                              font=basicFont, bg=baseColor, fg=textColor)
        SpaceLabel.grid(row=2, column=2, pady=5)

        # HISTORY QUESTIONS
        historyLabel = tk.Label(formFrame, text="100 LEVEL COURSES\n(check the box if failed)", font=headingFont, bg=baseColor, fg=textColor)
        historyLabel.grid(row=4, column=0, columnspan=6, pady=15)

        # ACC111 Principles of Accounting
        acc111_Label = tk.Label(formFrame, text="ACC111 Principles of Accounting", font=basicFont, bg=baseColor,
                                     fg=textColor)
        acc111_Label.grid(row=5, column=0, sticky='w', pady=6, columnspan=2)
        self.acc111_History = StringVar()
        acc111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.acc111_History,
                                           command=lambda: self.sendData())
        acc111_HistoryCheck.deselect()
        acc111_HistoryCheck.grid(row=5, column=2, pady=6, sticky='w')


        # "CSC111 Introduction to Computer Science"
        self.csc111_History = StringVar()
        csc111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.csc111_History,
                                            command=lambda: self.sendData())
        csc111_HistoryCheck.deselect()
        csc111_HistoryCheck.grid(row=5, column=3, pady=6, sticky='w')

        csc111_HistoryLabel = tk.Label(formFrame, text="CSC111 Introduction to Computer Science", font=basicFont, bg=baseColor,
                                     fg=textColor)
        csc111_HistoryLabel.grid(row=5, column=4, sticky='w', pady=6, columnspan=2)


        # "ECN111 Introduction to Economics"
        ecn111_Label = tk.Label(formFrame, text="ECN111 Introduction to Economics", font=basicFont, bg=baseColor,
                                     fg=textColor)
        ecn111_Label.grid(row=6, column=0, sticky='w', pady=6, columnspan=2)
        self.ecn111_History = StringVar()
        ecn111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.ecn111_History,
                                           command=lambda: self.sendData())
        ecn111_HistoryCheck.deselect()
        ecn111_HistoryCheck.grid(row=6, column=2, pady=6, sticky='w')


        # "MAT111 Algebra"
        self.mat111_History = StringVar()
        mat111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.mat111_History,
                                            command=lambda: self.sendData())
        mat111_HistoryCheck.deselect()
        mat111_HistoryCheck.grid(row=6, column=3, pady=6, sticky='w')

        mat111_HistoryLabel = tk.Label(formFrame, text="MAT111 Algebra", font=basicFont, bg=baseColor,
                                     fg=textColor)
        mat111_HistoryLabel.grid(row=6, column=4, sticky='w', pady=6, columnspan=2)


        # "MAT112 Trigonometry and Analytical Geometry"
        mat112_Label = tk.Label(formFrame, text="MAT112 Trigonometry and Analytical Geometry", font=basicFont, bg=baseColor,
                                     fg=textColor)
        mat112_Label.grid(row=7, column=0, sticky='w', pady=6, columnspan=2)
        self.mat112_History = StringVar()
        mat112_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.mat112_History,
                                           command=lambda: self.sendData())
        mat112_HistoryCheck.deselect()
        mat112_HistoryCheck.grid(row=7, column=2, pady=6, sticky='w')


        # "PHY111 Mechanics and Properties of Matter"
        self.phy111_History = StringVar()
        phy111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.phy111_History,
                                            command=lambda: self.sendData())
        phy111_HistoryCheck.deselect()
        phy111_HistoryCheck.grid(row=7, column=3, pady=6, sticky='w')

        phy111_HistoryLabel = tk.Label(formFrame, text="PHY111 Mechanics and Properties of Matter", font=basicFont, bg=baseColor,
                                     fg=textColor)
        phy111_HistoryLabel.grid(row=7, column=4, sticky='w', pady=6, columnspan=2)


        # "CST111 Use of Library, Study Skills and ICT I"
        cst111_Label = tk.Label(formFrame, text="CST111 Use of Library, Study Skills and ICT I", font=basicFont, bg=baseColor,
                                     fg=textColor)
        cst111_Label.grid(row=8, column=0, sticky='w', pady=6, columnspan=2)
        self.cst111_History = StringVar()
        cst111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.cst111_History,
                                           command=lambda: self.sendData())
        cst111_HistoryCheck.deselect()
        cst111_HistoryCheck.grid(row=8, column=2, pady=6, sticky='w')


        # "GST111 Communication in English"
        self.gst111_History = StringVar()
        gst111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.gst111_History,
                                            command=lambda: self.sendData())
        gst111_HistoryCheck.deselect()
        gst111_HistoryCheck.grid(row=8, column=3, pady=6, sticky='w')

        gst111_HistoryLabel = tk.Label(formFrame, text="GST111 Communication in English", font=basicFont, bg=baseColor,
                                     fg=textColor)
        gst111_HistoryLabel.grid(row=8, column=4, sticky='w', pady=6, columnspan=2)


        # "CIT111 Microsoft Office Specialist"
        cit111_Label = tk.Label(formFrame, text="CIT111 Microsoft Office Specialist", font=basicFont, bg=baseColor,
                                     fg=textColor)
        cit111_Label.grid(row=9, column=0, sticky='w', pady=6, columnspan=2)
        self.cit111_History = StringVar()
        cit111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.cit111_History,
                                           command=lambda: self.sendData())
        cit111_HistoryCheck.deselect()
        cit111_HistoryCheck.grid(row=9, column=2, pady=6, sticky='w')


        # "EDS111 Entrepreneurial Development Studies"
        self.eds111_History = StringVar()
        eds111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.eds111_History,
                                            command=lambda: self.sendData())
        eds111_HistoryCheck.deselect()
        eds111_HistoryCheck.grid(row=9, column=3, pady=6, sticky='w')

        eds111_HistoryLabel = tk.Label(formFrame, text="EDS111 Entrepreneurial Development Studies", font=basicFont, bg=baseColor,
                                     fg=textColor)
        eds111_HistoryLabel.grid(row=9, column=4, sticky='w', pady=6, columnspan=2)


        # "TMC111 Total Man Concept I"
        tmc111_Label = tk.Label(formFrame, text="TMC111 Total Man Concept I", font=basicFont, bg=baseColor,
                                     fg=textColor)
        tmc111_Label.grid(row=10, column=0, sticky='w', pady=6, columnspan=2)
        self.tmc111_History = StringVar()
        tmc111_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.tmc111_History,
                                           command=lambda: self.sendData())
        tmc111_HistoryCheck.deselect()
        tmc111_HistoryCheck.grid(row=10, column=2, pady=6, sticky='w')


        # "TMC112 Total Man Concept - Sports I"
        self.tmc112_History = StringVar()
        tmc112_HistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.tmc112_History,
                                            command=lambda: self.sendData())
        tmc112_HistoryCheck.deselect()
        tmc112_HistoryCheck.grid(row=10, column=3, pady=6, sticky='w')

        tmc112_HistoryLabel = tk.Label(formFrame, text="TMC112 Total Man Concept - Sports I", font=basicFont, bg=baseColor,
                                     fg=textColor)
        tmc112_HistoryLabel.grid(row=10, column=4, sticky='w', pady=6, columnspan=2)

        # Next Button
        nextBtn = tk.Button(formFrame, text='Recommend',
                            command=self.controller.process_data, bg=titleFg,
                            fg=titleBg, font=btnFont
                            )
        nextBtn.grid(row=12, column=0, columnspan=6, pady=15, ipadx=40)

    
    def sendData(self):
        radioArray = [  int(self.acc111_History.get()), int(self.csc111_History.get()),
                        int(self.ecn111_History.get()), int(self.mat111_History.get()),
                        int(self.mat112_History.get()), int(self.phy111_History.get()),
                        int(self.cst111_History.get()), int(self.gst111_History.get()),
                        int(self.cit111_History.get()), int(self.eds111_History.get()),
                        int(self.tmc111_History.get()), int(self.tmc112_History.get())
                    ]
        self.courseSelectionArray = radioArray
        

    def get_details(self):
        return [ 
                 self.lastNameEntry.get(),
                 self.firstNameEntry.get(),
                 self.matriculeEntry.get(),
                 self.courseSelectionArray
                ]









class ResultsInterface(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.create_widgets()

    def create_widgets(self):
        resultsFrame = tk.Frame(self
                                , bg=baseColor
                                )
        resultsFrame.grid(row=0, column=0, sticky='N', ipady=50)
        resultsFrame.config(
            # bg='grey'
        )

        # Add Title Frame to Results Page Frame
        titleFrame = tk.Frame(resultsFrame)
        titleFrame.grid(row=0, column=0, sticky='N', pady=50, padx=550)

        # Add Welcome Text to Title Frame
        welcomeLbl = tk.Label(resultsFrame, text="Course Recommendation",
                              font=titleFont,
                              height=3, anchor='center', bg=titleBg, fg=titleFg)
        welcomeLbl.grid(row=0, column=0, columnspan=6, sticky='nEW')

        # Add Form Frame To Welcome Page Frame
        formFrame = tk.Frame(resultsFrame,
                             bg=baseColor
                             )
        formFrame.grid(row=1, column=0, sticky='N', pady=(2, 64), padx=12)

        # Courses Recommended Label
        recommendLabel = tk.Label(formFrame, text='Recommended Courses', font=headingFont, anchor='center', bg=baseColor,
                                   fg=textColor)
        recommendLabel.grid(row=1, column=0, columnspan=7, pady=15, sticky='n')

        # Courses Recommended Text Label
        self.recommendation = tk.StringVar()

        recommendTextLabel = tk.Label(formFrame,
                                       textvariable=self.recommendation,
                                       font=basicFont, bg=baseColor, fg=textColor, anchor='center')

        recommendTextLabel.grid(row=2, column=0, pady=5, columnspan=5)

        # Elective Title Label
        electiveLabel = tk.Label(formFrame, text='Elective Courses\nSelect one of them', font=headingFont, anchor='center', bg=baseColor,
                                   fg=textColor)
        electiveLabel.grid(row=3, column=0, columnspan=7, pady=15, sticky='n')

        # Elective Text Label
        self.electives = tk.StringVar()

        electiveTextLabel = tk.Label(formFrame,
                                       textvariable=self.electives,
                                       font=basicFont, bg=baseColor, fg=textColor, anchor='center')

        electiveTextLabel.grid(row=4, column=0, pady=5, columnspan=5)
       
        nextBtn = tk.Button(formFrame, text='Finish', command=lambda: root.destroy(), bg=titleFg,
                            fg=titleBg, font=btnFont)
        nextBtn.grid(row=12, column=0, columnspan=7, pady=15, ipadx=40)

        
       


    def display_courses(self, courses, credits):
        elective_course = ["CBS111 Mathematics for Business and Social Sciences I", "MAT214 Linear Algebra"]
        flag = 0
        if (elective_course[0] in courses):
            courses.remove("CBS111 Mathematics for Business and Social Sciences I")
            courses.remove("MAT214 Linear Algebra")
            elec_credit = [credits[-2], credits[-1]]
            flag = 1
        # Calculate the width for the course column
        max_course_length = max(len(course) for course in courses)
        course_column_width = max_course_length + 10  # Add some padding

        # Format each course and its units
        courses_text = ""
        for course, credit in zip(courses, credits):
            # Format the course name and units with appropriate padding
            course_line = f"{course.ljust(course_column_width)} {credit} units\n"
            courses_text += course_line

        # Calculate total units
        total_units = sum(credits)

        # Add total units to the text
        total_line = f"\nTotal Units = {total_units}\n"
        courses_text += total_line

        # Set the formatted text in the interface
        self.recommendation.set(courses_text)

        if flag == 1:
            courses_text = ""
            for course, credit in zip(elective_course, elec_credit):
                # Format the course name and units with appropriate padding
                course_line = f"{course.ljust(course_column_width)} {credit} units\n"
                courses_text += course_line

            # Calculate total units
            total_units = sum(elec_credit)

            # Add total units to the text
            total_line = f"\nTotal Elective Units = {total_units}\n"
            courses_text += total_line

            # Set the formatted text in the interface
            self.electives.set(courses_text)







class Controller:
    def __init__(self, root):
        self.root = root
        self.root.title('Course Advisory Expert System')
        self.backend = PrologBackend("../archit/kb_updated.pl")
        self.create_interface()
        self.maxReg = 26

    def create_interface(self):
        self.interface = Interface(self.root, self)
        self.interface.grid(row=0, column=0, padx=20, pady=20, sticky="N")

    def process_data(self):
        details = self.interface.get_details()
        failedCourses = []
        coursesAlpha100 = ["acc111", "csc111", "ecn111", "mat111", "mat112", "phy111",
                        "cst111", "gst111", "cit111", "eds111", "tmc111", "tmc112"]
        
        #adding failed courses dynamically to KB
        for count, elem in enumerate(details[3]):
            if elem == 1:
                self.backend.add_fact("failed", coursesAlpha100[count])
                failedCourses.append(coursesAlpha100[count])


        #failed courses sorted by course code
        courseCodes = []
        if failedCourses:
            courseCodes = sorted(self.backend.get_failed_courses())
            print(courseCodes)

        #print(self.backend.sum_credits(courseCodes))

        #200 level compulsory courses
        if self.backend.sum_credits(courseCodes) < self.maxReg:
            comp200Courses = self.backend.get_compulsory200()
            #dict of compulsory courses and their credits
            course_credit = {code:self.backend.credit_course(code) for code in comp200Courses}
            print(course_credit)
            #sorting the compulsory courses in descending order
            comp200Courses = sorted(comp200Courses, key=lambda x: course_credit[x], reverse=True)
            print(comp200Courses)

            for c in comp200Courses:
                if self.backend.sum_credits(courseCodes) + self.backend.credit_course(c) < self.maxReg:
                    courseCodes.append(c)

            nonComp200Courses = self.backend.get_nonCompulsory200()
            print("Non comp", nonComp200Courses)
            if self.backend.sum_credits(courseCodes) < self.maxReg:
                for c in nonComp200Courses:
                    if self.backend.sum_credits(courseCodes) + self.backend.credit_course(c) < self.maxReg:
                        courseCodes.append(c)

        print("Recommendation")
        completeCourse = [self.backend.get_fullName(elem) for elem in courseCodes]
        print(completeCourse)

        #print([course['X'] for course in self.backend.prolog.query('levelcourse("cst111", X)')])
        #.decode('utf-8')
        #courses = []
        #for c in courseCodes:
        #    courses.append(self.backend.get_fullName(c))

        credits = []
        for c in courseCodes:
            credits.append(self.backend.credit_course(c))
        
        self.display_results(completeCourse, credits)



    def display_results(self, recommended_courses, credits):
        self.interface.pack_forget()
        self.results_interface = ResultsInterface(self.root)
        self.results_interface.grid(row=0, column=0, padx=20, pady=20, sticky="N")
        self.results_interface.display_courses(recommended_courses, credits)

if __name__ == "__main__":
    root = tk.Tk()
    
    #root.iconbitmap('logo.ico')
    root.columnconfigure(0, weight=1)
    root.geometry('960x680')

    # Add background image to root frame
    backgroundImg = ImageTk.PhotoImage(Image.open("../graphics/expert_sys.jpg"))
    imgCont = tk.Label(root, image=backgroundImg)
    imgCont.grid(row=0, column=0, sticky='news')

    app = Controller(root)
    root.mainloop()
