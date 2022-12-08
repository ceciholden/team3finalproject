import time
import pwinput
import re
from replit import db


class HospitalManagement:
  __MAX_PATIENTS = 200

  def __init__(self, patientName):
    self.__patientName = patientName
    self.__patientList = []
    self.__doctorList = []

  def enlistPatient(self, patientName):
    if (len(self.__patientList) < HospitalManagement.__MAX_PATIENTS):
      self.__patientList.append(patientName)
    else:
      raise ValueError('Hospital is at max patient capacity. ')
      
#login
def login():
    username = input("Enter username or type sign up: ")

    if username in db: 
        password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
        checkPass(username, password)
    elif username.lower() == 'sign up':
        signup()
    else:
        print("Username does not exist")
        login()


#checkPass
def checkPass(username, password):
    trials = 0
    if db[username][4] == password:
      print("\nSUCCESSFULL LOGIN...WELCOME :)")
      

    while password != db[username][4] and trials<3:
      print("\nIncorrect password...Try again")
      password = pwinput.pwinput(prompt="Re-enter password: ", mask="*")
      trials = trials + 1

    while password != db[username][4] and trials>=3:
      print("Incorrect password...Wait 60 seconds to try again")
      time.sleep(60)
      password = pwinput.pwinput(prompt="Re-enter password: ", mask="*")
      trials = trials + 1
    


#passwordAuthentication
def passAuth(y,x):
    pass_pattern = "^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    pat = re.compile(pass_pattern)               
    mat = re.search(pat, x)
    if mat:
      print("Password is valid.")
        
      conf_pass = pwinput.pwinput(prompt="Confirm password: ", mask="*")
      if conf_pass == x:
        print("Passwords match")
        #db.update({y:x})
        print("Welcome")
        
      else:
        print("Passwords do not match")
        password = pwinput.pwinput(prompt="Create your password: ", mask="*")
        passAuth(y,password)
    else:
      print("Password invalid !!") 
      password = pwinput.pwinput(prompt="Create your password: ", mask="*")
      passAuth(y,password)


#signup
def signup():
    username = input("Create a username: ")
  
    if username in db:
        print('Username already taken,try another one')
        signup()
      
    else:
        print('Username accepted\n')
        age=input("Enter your age: ")
        gender=input("Enter your gender: ")
        DoB=input("Enter Date of Birth(Format: dd-mm-yyyy): ")
        department=input("Enter your department(doctor/staff): ")
      
        password = pwinput.pwinput(prompt="Create your password: ", mask="*")
        passAuth(username,password)
        db[username] = [age, gender, DoB, department, password]

class HospitalPersons:
  def __init__(self,name,age,gender,DoB,department):
    self.__name=name 
    self.__age=age
    self.__gender=gender
    self.__DoB=DoB
    self.__department=department
    
  def viewPersonalInfo(self):
    print(f"Name: {self.__name}")
    print(f"Age: {self.__age}")
    print(f"Gender: {self.__gender}")
    print(f"Date of Birth: {self.__DoB}")
    print(f"Department: {self.__department}")
      
  

#menu
def menu():
  print("1.View personal information")
  print("2. ....coming soon....")
  selection = input("Enter a number: ")

  if selection == '1':
        #View personal info
        dis_guy = input("Enter name to view their personal data: ")
        personInfo = HospitalPersons(dis_guy,db[dis_guy][0],db[dis_guy][1],db[dis_guy][2],db[dis_guy][3])
        personInfo.viewPersonalInfo()
#you guys add your methods

#Main function
def main():
  print("Type in Logout to exit")
  start = 'log in'
  while start.lower() != 'logout':
    start = input("Type Login or Sign Up: ")

    if start.lower() == 'login':
      login()
      menu()    
      
    if start.lower() == 'sign up':
        signup()
  else:
    print("Successful Logout")

main()