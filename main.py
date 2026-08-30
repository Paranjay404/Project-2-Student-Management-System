class InvalidException(Exception):
    pass

class Student:
    def __init__(self,name,stu_ID,stu_PSWD,attendance,marks):
        self.name=name
        self.stu_ID=stu_ID
        self.stu_PSWD=stu_PSWD
        self.attendance=attendance
        self.marks=marks
    
    def total(self):
        total_marks=0
        for i,j in self.marks.items():
            total_marks=j+total_marks
        return total_marks
    
    def avg_marks(self):
        total_marks=self.total()
        avg_marks=total_marks/len(self.marks.items())
        return avg_marks
    def highest_marks(self):
        highest_marks=max(self.marks.values())
        return highest_marks
    def lowest_marks(self):
        lowest_marks=min(self.marks.values())
        return lowest_marks

        
# function to calc avg, high and low
    def marks_detail(self):
        avg_marks=self.avg_marks()
        highest_marks=self.highest_marks()
        lowest_marks=self.lowest_marks()

        
        lowest_marks=min(self.marks.values())
        print("_"*50,"\n")
        print("MARKS DETAIL","\n")
        print("_"*50,"\n")
        print("Average Marks: ",avg_marks,"\n")
        print("Highest Marks: ",highest_marks,"\n")
        print("Lowest Marks: ",lowest_marks)
        print("_"*50)

#grade calc class : decides pass/fail from avg marks and custom each subject marks, grade, result, remarks, scholarship
class Grade():
    
    def __init__(self,pass_marks):

        self.pass_marks=pass_marks
    def Grade_Assignment(self,stu_obj):
        a=stu_obj.avg_marks()
        if a>=95 and 100>=a:
            return "Grade A+"
        if a>=90 and 95>a:
            return "Grade A"
        elif a>=85 and 90>a:
            return "Grade B+"
        elif a>=80 and 85>a:
            return "Grade B"
        elif a>=75 and 80>a:
            return "Grade C+"
        elif a>=70 and 75>a:
            return "Grade C"
        elif a>=65 and 70>a:
            return "Grade D+"
        elif a>=50 and 65>a:
            return "Grade D"
        elif a>=self.pass_marks and 50>a:
            return "Grade E"
        elif a>=0 and self.pass_marks>a:
            return "Grade F"
        else:
            raise InvalidException("Invalid Marks")
    
    def Remark_Assignment(self,stu_obj,grade):
        return {"Grade A+":"Excellent","Grade B+":"Very Good","Grade C+":"Good","Grade D+":"Can be improved","Grade E":"Needs Improvement","Grade F":"Fail: Re-write the exam or repeat grade","Grade A":"Excellent","Grade B":"Very Good","Grade C":"Good","Grade D":"Needs Improvement"}[grade]
    
    def Result_Assignment(self,stu_obj):
            b=stu_obj.avg_marks()
            if b<self.pass_marks and b>=0:
                return "Fail"
            elif b<=100 and b>=33:
                return "Pass"
            else:
                raise InvalidException("Invalid Marks")

class Email():
    def __init__(self,sender_name,sender_email):
        self.s_name=sender_name
        self.s_ID=sender_email
        
    def send_report(self,stu_obj,grade):
        print("From: ",self.s_name,f" <{self.s_ID}>")
        print(f"To: [{stu_obj.name}]")
        print("_"*50)
        print(grade)

class Report_printer():
    def __init__(self,title):
        self.title=title
    def print_report(self,stu_obj,grade,result,remarks):
        print("==========================================================================================")
        print(self.title)
        print("==========================================================================================")
        print(f"Name: {stu_obj.name} | Roll No.: {stu_obj.stu_ID} | Attendance: {stu_obj.attendance}")
        for i,j in stu_obj.marks.items():
            print(f"{i}:{j}")
        print(f"Total: {stu_obj.total()} | Avg: {stu_obj.avg_marks()}| Highest: {stu_obj.highest_marks()}| Lowest: {stu_obj.lowest_marks()}\n")
        print(f"Grade: {grade} | Result: {result} | Remarks: {remarks}")
        print("==========================================================================================")
        
# ========================================
#         Grade 9 Progress Report         
# ========================================
# Neha | Roll No.: 123 | Attendance: 23.0
# English     : 22.0
# Mathematics : 34.0
# Science     : 45.0
# Computer    : 56.0
# History     : 78.0
# Total 235.0 | Avg 47.0 | High 78.0 | ƒLow 22.0

# Grade D Result FAIL Remarks Needs Improvement
# =============================================

class StudentManager:
    def __init__(self,name,calc,printer,email):
        self.name=name; 
        self.students=[]
        self.calc=calc; 
        self.printer=printer; 
        #self.repo=repo; 
        self.email=email
    def add_student(self,s): 
        self.students.append(s)
        
    def find_student(self,stu_ID,stu_PSWD):
        for student in self.students:
            if student.stu_ID == stu_ID and student.stu_PSWD == stu_PSWD:
                return student
        return None
    def process_student(self,s):
        g=self.calc.Grade_Assignment(s);
        r=self.calc.Result_Assignment(s);
        print(g,r)
        rem=self.calc.Remark_Assignment(s,g)
        self.printer.print_report(s,g,r,rem)
        #self.repo.save(s,g,r)
        self.email.send_report(s,g)

def input_student():
    name=input("Name: "); 
    # def __init__(self,name,stu_ID,stu_PSWD,marks,attendance):
    #     self.name=name
    #     self.stu_ID=stu_ID
    #     self.stu_PSWD=stu_PSWD
    #     self.attendance=attendance
    #     self.marks=marks
    stu_ID=int(input("Roll: ")); 
    stu_PSWD=(input("Password: ")); 
    att=float(input("Attendance: "))
    subs=["English","Mathematics","Science","Computer","History"]
    marks = {sub: float(input(sub + ": ")) for sub in subs}
    return Student(name,stu_ID,stu_PSWD,att,marks)

def make_manager(label,pass_marks):
    return StudentManager(label,
        Grade(pass_marks),
        Report_printer(f"{label} Progress Report"),
        #StudentFileRepository(label.lower().replace(" ","_")+".txt"),
        Email(f"{label} Office",label.lower().replace(" ","")+"@school.com"))
        
def main():
    managers={"9":make_manager("Grade 9",40),"10":make_manager("Grade 10",50)}
    
    while True:
        print("\n1.Add 2.Process ")
        ch=input("Choice: ")
        if ch=="7": 
            break
        grade=input("Enter Grade (9/10): ")
        m=managers[grade]
        if ch=="1":
            m.add_student(input_student())
        elif ch=="2":
            r=int(input("Roll: ")); 
            p=input("Password: ");
            s=m.find_student(r,p)
            print("Not found") if not s else m.process_student(s)

main()







st1=Student("R","123","123",{"a":12,"b":100,"c":2},92)
print(st1.total())
st1.marks_detail()


#grade