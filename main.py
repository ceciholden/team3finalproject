import time
import pwinput
import re
from replit import db

db.update({"hi":["age", "gender", "DoB", "department", "password"]})

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

  while password != db[username][4] and trials < 3:
    print("\nIncorrect password...Try again")
    password = pwinput.pwinput(prompt="Re-enter password: ", mask="*")
    trials = trials + 1

  while password != db[username][4] and trials >= 3:
    print("Incorrect password...Wait 60 seconds to try again")
    time.sleep(60)
    password = pwinput.pwinput(prompt="Re-enter password: ", mask="*")
    trials = trials + 1


#passwordAuthentication
def passAuth(y, x):
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
      passAuth(y, password)
  else:
    print("Password invalid !!")
    password = pwinput.pwinput(prompt="Create your password: ", mask="*")
    passAuth(y, password)


#signup
def signup():
  username = input("Create a username: ")

  if username in db:
    print('Username already taken,try another one')
    signup()

  else:
    print('Username accepted\n')
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    DoB = input("Enter Date of Birth(Format: dd-mm-yyyy): ")
    department = input("Enter your department(doctor/staff): ")

    password = pwinput.pwinput(prompt="Create your password: ", mask="*")
    passAuth(username, password)
    db[username] = [age, gender, DoB, department, password]


class HospitalPersons:

  def __init__(self, name, age, gender, DoB, department):
    self.__name = name
    self.__age = age
    self.__gender = gender
    self.__DoB = DoB
    self.__department = department

  def viewPersonalInfo(self):
    print(f"Name: {self.__name}")
    print(f"Age: {self.__age}")
    print(f"Gender: {self.__gender}")
    print(f"Date of Birth: {self.__DoB}")
    print(f"Department: {self.__department}")

class HospitalManagement:
  __MAX_PATIENTS = 200

  def __init__(self):
    self.__patientList = []

  def enlistPatient(self, patientName):
    if (len(self.__patientList) < HospitalManagement.__MAX_PATIENTS):
      self.__patientList.append(patientName)
      return self.__patientList
    else:
      raise ValueError('Hospital is at max patient capacity. ')

  def viewPatientList(self):
    print(self.__patientList)



class Patient(HospitalPersons):

  def __init__(self, name, age, gender, DoB, department, height, weight, allergies, illnesses, medicines):
    self.__height = height
    self.__weight = weight
    self.__allergies = allergies
    self.__illnesses = illnesses
    self.__medicines = medicines
    super().__init__(name, age, gender, DoB, department)

  def getHeight(self):
    return str(self.__height)

  def setHeight(self, height):
    self.__height = str(height)

  def getWeight(self):
    return str(self.__weight)

  def setWeight(self, weight):
    self.__weight = str(weight)

  def getAllergies(self):
    return self.__allergies

  def addAllergies(self, allergy):
    self.__allergies.add(allergy)

  def removeAllergy(self, allergy):
    self.__allergies.remove(allergy)

  def getIllnesses(self):
    return self.__illnesses

  def addIllness(self, illness):
    self.__illness.append(illness)

  def removeIllness(self, illness):
    self.__illness.remove(illness)

  def setAppointment(self, name, DOB, date, time):
    accessName = name+" "+DOB
    self.__apptTime = (date, time)
    if accessName in db.keys():
      db[accessName] = db[accessName]+self.__apptTime

  def getAppointment(self):
    return self.__apptTime

  def viewMedRecord(self):
    super().viewPersonalInfo()
    string = "\nDetailed medical record is: \nHeight: "+self.getHeight()+" inches \nWeight: "+self.getWeight()+" lbs \n"+"Allergies include:"
    for x in self.__allergies:
      string = string+" "+x
    string=string+"\n"+"Illnesses include:"
    for y in self.__illnesses:
      string = string+" "+y+","
    string+="\n"+"Medicine List:"
    for z in self.__medicines:
      string = string+" "+z+","
    return string




class Doctor(HospitalPersons):
  def __init__(self,name,age,gender,DoB,department):
    super().__init__(name, age, gender, DoB, department)

  def viewSchedule(self):
    #returns all patient appointments
      #add patient attributes to variable
    for key in db:
      if " " in db.key():
        print(self.getAppointment(key))

  def editSchedule():
    #change name, dob, time, date
    patName = input("Patient name: ")
    patDoB = input("Patient DoB: ")
    schChoice = input("Choose schedule attribute: ").lower
    if schChoice == "time":
      newTime = input("Input new time: ")
      #change the appt time
    if schChoice == "date":
      newDate = input("Input new date: ")
      db[patName+" "+patDoB].__apptTime()
      #change the appt date

  def changeAttribute():
    #change height, weight, allergies, illnesses, medicine
      #calls set function in patient class
    #uses the set methods that will be made later
    patName = input("Patient name: ")
    patDob = input("Patient DoB: ")
    attChoice = input("Choose attribute: ").lower
    if attChoice == "height":
      return
    elif attChoice == "weight":
      return
    elif attChoice == "allergies":
      return
    elif attChoice == "illnesses":
      return
    elif attChoice == "medicine":
      return
  
  def addPatient(self): 
    nameInput = input("What is the patient's name? ")
    ageInput = input("What is the patient's age? ")
    genderInput = input("What is the patient's gender? (M/F/N) ")
    DoB = input("What is the patient's date of birth? (dd-mm-yyyy) ")
    departmentInput = input("What department is this patient in? ")
    heightInput = input("What is this patient's height in inches? ")
    weightInput = input("What is this patient's weight in lbs? ")
    allergiesNum = int(input("How many allergies do you want to input?"))
    allergies = []
    for x in range(allergiesNum):
      y = input("What is their allergy? ")
      allergies.append(y)
    illnessesNum = int(input("How many illnesses does the patient have?"))
    illnesses = []
    for x in range(illnessesNum):
      z = input("What is their illness and the severity? Write it in illness: severity form. ")
      illnesses.append(z)
    medsNum = int(input("How many meds does this patient take? "))
    medicines = []
    for x in range(medsNum):
      medicines.append(input("What medicine does this patient take?"))
    accessName = nameInput+" "+DoB
    db[accessName] = Patient(nameInput,ageInput,genderInput,DoB,departmentInput,heightInput,weightInput,allergies,illnesses,medicines)
    
    
#patientA = Patient("Samantha Chu", 22, "F", "01-01-2000", "Hematology", 70, 150,['Penicillin', 'Pollen'],['Sickle Cell Disease: Severe', 'Low Blood Pressure: Benign'],['Ramipril', 'Hydroxyurea'])
#print(patientA.viewMedRecord())


#menu
def menu():
  print("1.View personal information")
  print("2. Add Patient Info")
  print("3 .. coming soon ..")
  selection = input("Enter a number: ")
  
  if selection == '1':
    #View personal info
    dis_guy = input("Enter name to view their personal data: ")
    personInfo = HospitalPersons(dis_guy, db[dis_guy][0], db[dis_guy][1],db[dis_guy][2], db[dis_guy][3])
    personInfo.viewPersonalInfo()
    #you guys add your methods
  if selection == '2':
    dis_guy = input("Enter your name to add their personal data: ")
    doctorInfo = Doctor(dis_guy, db[dis_guy][0], db[dis_guy][1],db[dis_guy][2], db[dis_guy][3])
    doctorInfo.addPatient()
  #if selection == '3':

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


