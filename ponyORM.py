#    ponyORM required , please install ponyORM
#
#    pip install pony
#
# The entire set of classes and functions necessary for working with Pony
from pony.orm import *
from datetime import date
import re

# Creating the database object
db = Database()

#Defining entities
class Student(db.Entity):
    id = Optional(int)
    sid = PrimaryKey(int)
    name = Required(str)
    birthday = Required(date)
    midScore = Required(int)
    finalScore = Required(int)
    averageScore = Optional(int)
    grade = Optional(str)

    def get_average(self):
        ave = (self.midScore + self.finalScore) / 2
        return '%d' % ave

    def get_grade(self):
        if self.averageScore >= 90 :
            return "A"
        elif self.averageScore >= 80 :
            return "B"
        elif self.averageScore >= 70 :
            return "C"
        elif self.averageScore >= 60 :
            return "D"
        else :
            return "F"

    def after_insert(self):
        cnt = select(count(p) for p in Student)[:]
        self.averageScore = self.get_average()
        self.grade = self.get_grade()
        self.id  = cnt[0]
        commit()

    def after_delete(self):
        all = select(p for p in Student)
        all2 = all.order_by(Student.id)
        i = 1
        for a in all2:
            a.id = i
            i = i + 1
            commit()


# Database Binding, Use in-memory db
db.bind(provider='sqlite', filename=':memory:')

# Mapping entities to database tables
db.generate_mapping(create_tables=True)

# Using the debug mode( Only Develope mode)
set_sql_debug(False)

@db_session
def add_student(sid, name, birthday, midScore, finalScore):
    Student(sid=sid, name=name, birthday=birthday, midScore=midScore, finalScore=finalScore)
    commit()

@db_session
def find_all(sort=None):
    if sort is None:
        select(p for p in Student).order_by(Student.id)[:].show()
    elif sort == "name":
        select(p for p in Student).order_by(Student.name)[:].show()
    elif sort == "average":
        before = select(p for p in Student).order_by(desc(Student.averageScore))
        i = 1
        for a in before :
            a.id = i
            i = i + 1
            commit()
        select(p for p in Student).order_by(Student.id)[:].show()
    elif sort == "grade":
        select(p for p in Student).order_by(Student.grade, desc(Student.averageScore))[:].show()
    elif sort == "writer":
        return select(p for p in Student).order_by(Student.id)[:]

@db_session
def delete_student(sid=None, name=None):
    if not (sid is None):
        delete(p for p in Student if p.sid == sid)
        commit()
    elif not (name is None):
        delete(p for p in Student if p.name == name)
        commit()

@db_session
def find_student(sid=None, name=None):
    if not (sid is None):
        select((p.sid, p.name, p.averageScore, p.grade) for p in Student if p.sid == sid)[:].show()
    elif not (name is None):
        select((p.sid, p.name, p.averageScore, p.grade) for p in Student if p.name == name)[:].show()

@db_session
def modify_student(sid=None, name=None, midScore=None, finalScore=None):
    if not (sid is None):
        modi = Student.get(sid=sid)
        if not (midScore is None):
            modi.midScore = midScore
            modi.averageScore = Student.get_average(modi)
            modi.grade = Student.get_grade(modi)
            commit()
        else:
            modi.finalScore = finalScore
            modi.averageScore = Student.get_average(modi)
            modi.grade = Student.get_grade(modi)
            commit()

    elif not (name is None):
        modi = Student.get(name=name)
        if not (midScore is None):
            modi.midScore = midScore
            modi.averageScore = Student.get_average(modi)
            modi.grade = Student.get_grade(modi)
            commit()
        else:
            modi.finalScore = finalScore
            modi.averageScore = Student.get_average(modi)
            modi.grade = Student.get_grade(modi)
            commit()

# File Open
def file_open(filenm='./data.txt'):
    try:
        with open(filenm) as f:
            for line in f:
                contents = line.split()
                add_student(contents[1],contents[2],contents[3],contents[4],contents[5])
    except:
        print("Error occured during file open.")

def input_name():
    chk = True
    while(chk):
        a = input('Please Input the Student name : ')
        if isinstance(a, str):
            chk = False
        else:
            print('Wrong Character!')
            chk = True
    return a

def input_studentid():
    chk = True
    while(chk):
        try:
            a = input('Please Input the Student number : ')
            b = int(a)
            if isinstance(b, int) and len(a) == 8:
                chk = False
            else:
                print('Wrong Character or length! Student number consist of only number and length is 8')
                chk = True
        except:
            print('Wrong Character or length! Student number consist of only number and length is 8')
            chk = True
    return a

def input_birthday():
    chk = True
    p = re.compile('[0-9]{4}[-][01][0-9][-][0123][0-9]')
    while(chk):
        a = input("Please Input the Studen's birthday (ex: YYYYMMDD or YYYY-MM-DD) :")
        m = p.match(a)
        if len(a) == 8:
            year = int(a[0:4])
            month = int(a[4:6])
            day = int(a[6:8])
            chk = False
        elif len(a) == 10:
            a = a.replace('-','')
            year = int(a[0:4])
            month = int(a[4:6])
            day = int(a[6:8])
            chk = False
        else :
            print("Wrong Chracter!")
            chk = True
    return date(year,month,day)

def input_score(str="mid"):
    chk = True
    while(chk):
        a = input("Pleae input the " + str + "term score :")
        b = int(a)
        if isinstance(b, int) and len(a) == 2:
            chk = False
        else :
            print("Wrong Character!")
    return a

#### Main Program ####
#file_open()

while(True):
    print("A : add a new entry")
    print("D : delete an entry")
    print("F : find some item from entry")
    print("M : modify an entry")
    print("P : print the contents af all entries")
    print("R : read personal date from a file")
    print("S : sort entries")
    print("W : write the contents to the same file")
    print("Q : quit")
    ord = input('Choose one of the options below : ')
    ord = ord.lower()
    if ord == 'a':
        a = input_studentid()
        b = input_name()
        c = input_birthday()
        d = input_score('mid')
        e = input_score('final')
        add_student(a,b,c,d,e)
    elif ord =='d':
        ans = input('Input the Student ID or Name for finding student score : ')
        if ans.isdigit() :
            delete_student(ans,None)
        else :
            delete_student(None,ans)
    elif ord =='f':
        ans = input('Input the Student ID or Name for finding student score : ')
        if ans.isdigit() :
            find_student(ans,None)
        else :
            find_student(None,ans)
    elif ord =='m':
        ans = input('Input the Student ID or Name for modifying student score : ')
        ans2 = input("Mid(a) and Final(b) ? ")
        ans3 = input("Write new score : ")
        if ans2 == 'a':
            if ans.isdigit() :
                modify_student(ans,None,ans3,None)
            else:
                modify_student(ans, None, ans3, None)
        elif ans2 == 'b':
            if ans.isdigit() :
                modify_student(ans,None,None,ans3)
            else:
                modify_student(ans, None,None,ans3)
    elif ord =='p':
        find_all()
    elif ord =='r':
        ans = input('Input the file name for read (none is default) : ')
        if ans != '':
            filename = ans
            file_open(filename)
        else :
            file_open()
    elif ord =='s':
        ans = input("Sort Entries {Name(n), Average(a), Grade(g)} : ")
        ans = ans.lower()
        if ans == 'n':
            find_all("name")
        elif ans == 'a':
            find_all("average")
        elif ans == 'g':
            find_all("grade")
    elif ord =='q':
        print("Good Bye~!")
        break
    elif ord =='w':
        writer = find_all("writer")
        if not filename == None:
            file = filename
        else :
            file = "./data.txt"
        with open(file, "w") as f:
            for w in writer:
                f.write(str(w.id) + '\t' + str(w.sid) +'\t' + w.name + '\t' + str(w.birthday) + '\t' + str(w.midScore) +'\t' + str(w.finalScore))
                f.write('\n')
            f.close()
        continue
    else :
        continue
