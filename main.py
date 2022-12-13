import time
import pwinput
import re
from replit import db

#login
def login():
  '''Function allows users to log in to the database. If their username is not in the database they have the option to sign up'''
  username = input("Enter username or type sign up: ")

  if username in db:
    password = pwinput.pwinput(prompt="Enter your password: ", mask="*")
    checkPass(username, password)
  elif username.lower() == 'sign up':
    signup()
  else:
    print("Username does not exist")
    login()

db = {}

#checkPass
def checkPass(username, password):
  '''Takes username and password as input. Checks if the password entered by the user matches the user's username in the database. If username and password match, the user is granted access to the database. Otherwise, the user is prompted to re-enter their password'''
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
  '''Functions takes in password and checks it against an already established criteria. If password meets criteria, it is accepted as a valid password. Otherwise, the user is asked to enter a new password that meets the criteria.'''
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
  '''Functions allows to create new users in the database. If a username already exists, they login instead of signing up.'''
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
    '''This function is the initialization of the HospitalPersons class. It allows users to enter their personal information as defined within the scope of the class'''
    self.__name = name
    self.__age = age
    self.__gender = gender
    self.__DoB = DoB
    self.__department = department

  def viewPersonalInfo(self):
    '''Shows the personal information of the member of staff whose name is entered. Personal information is the name,age,gender,DoB, and their department'''
    print(f"Name: {self.__name}")
    print(f"Age: {self.__age}")
    print(f"Gender: {self.__gender}")
    print(f"Date of Birth: {self.__DoB}")
    print(f"Department: {self.__department}")

class HospitalManagement:
  __MAX_PATIENTS = 200

  def __init__(self):
    '''This function is the initialization of the HospitalManagement class. It allows hospital administration/personnel to update and view the list of patients currently registered in the hospital. There is a maximum limit of 200 patients within the hospital.'''
    self.__patientList = []

  def viewPatientList(self):
    '''This function takes no arguments. It returns the list of patients currently registered at the hospital.'''
    return self.__patientList

  def enlistPatient(self, patientName):
    '''This function takes argument (type string) patientName. The patientName will be added to the list of registered patients in the hospital.'''
    if (len(self.__patientList) < HospitalManagement.__MAX_PATIENTS):
      self.__patientList.append(patientName)
      print(patientName, 'added')
      return self.__patientList
    else:
      raise ValueError('Hospital is at max patient capacity. ')

  def removePatient(self, patientName):
    '''This function takes argument (type string) patientName. If the patient is registered in the patientList, the patientName will be removed from the hospital's registered patients list.'''
    if patientName in self.__patientList:
      self.__patientList.remove(patientName)
      print(patientName, 'removed')
      return self.__patientList

class Patient(HospitalPersons):
  def __init__(self, name, age, gender, DoB, department, height, weight, allergies, illnesses, medicines):
    '''This function instantiates the Patient object, it accepts patient attributes like height, weight, age, gender, and department, which are all strings, and  allergies, illnesses and medicines, which are lists. It also sends name, age, gender, DoB, and department to the parent class'''
    self.__height = height
    self.__weight = weight
    self.__allergies = allergies
    self.__illnesses = illnesses
    self.__medicines = medicines
    self.__apptTime = ["date","time"]
    super().__init__(name, age, gender, DoB, department)

  def getHeight(self):
    '''This method returns the patient's height'''
    return str(self.__height)

  def setHeight(self, height):
    '''This method changes the patient's height and confirms that it has been changed'''
    self.__height = str(height)
    print("Height set to " + str(height))

  def getWeight(self):
    '''This method returns the patient's weight'''
    return str(self.__weight)

  def setWeight(self, weight):
    '''This method changes the patient's weight and confirms that it has been changed'''
    self.__weight = str(weight)
    print("Weight set to " + str(weight))

  def getAllergies(self):
    '''This method returns the list of the patient's allergies'''
    return self.__allergies

  def addAllergies(self, allergy):
    '''This method adds an item (which is given as a string) to the list of the patient's allergies and confirms that is has been changed'''
    self.__allergies.add(allergy)
    print(allergy + " allergy added")

  def removeAllergy(self, allergy):
    '''This method removes a specified item from the list of the patient's allergies and confirms that is has been removed'''
    self.__allergies.remove(allergy)
    print(allergy + " allergy removed")

  def getIllnesses(self):
    '''This method returns the list of the patient's illnesses'''
    return self.__illnesses

  def addIllness(self, illness):
    '''This method adds an item (which is given as a string) to the list of the patient's illnesses and confirms that is has been changed'''
    self.__illness.append(illness)
    print(illness + " illness added")

  def removeIllness(self, illness):
    '''This method removes a specified item from the list of the patient's illnesses and confirms that is has been removed'''
    self.__illness.remove(illness)
    print(illness + " illness removed")

  def setAppointment(self, name, DOB, date, time):
    '''This method sets a patient's appointment to the given date and time, which are given as strings. The name and DOB are also given as strings to access the patient's information in the database'''
    accessName = name+" "+DOB
    self.__apptTime = [date, time]
    if accessName in db.keys():
      db[accessName] = db[accessName]+self.__apptTime
    print("Appointment set")

  def getAppointment(self):
    '''This method returns the patient's appointment time as a string'''
    return self.__apptTime

  def viewMedRecord(self):
    '''This method prints the patient's medical record as a table of strings'''
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

  #unfinished
  def viewSchedule(self):
  '''Returns all patient appointments'''
    for key in db:
      if " " in key:
        print(db[key].getAppointment())

  def editSchedule(self):
    '''Allows user to change the time and date of a patient's appointment.'''
    patName = input("Patient name: ")
    patDoB = input("Patient DoB: ")
    if (patName+" "+patDoB) not in db.keys():
      print("Patient not found")
    else:
      schChoice = input("Choose schedule attribute (time, date): ").lower()
      if schChoice == "time":
        newTime = input("Input new time: ")
        #patient object is not iterable. ask about __apptTime in db
        for list in db[patName+" "+patDoB]:
          list[1] = newTime
        print("Time updated")
      if schChoice == "date":
        newDate = input("Input new date: ")
        for list in db[patName+" "+patDoB]:
          list[0] = newDate
        print("Date updated")

  def changeAttribute(self):
    '''Allows user to change height, weight, allergies, illnesses, and medicine properties of Patient object. Calls methods in patient class to change attributes.'''
    patName = input("Patient name: ")
    patDoB = input("Patient DoB: ")
    attChoice = input("Choose attribute (height, weight, allergies, illnesses, medicine): ").lower()
    if attChoice == "height":
      newHeight = input("Input new height: ")
      db[patName + " " + patDoB].setHeight(newHeight)
    elif attChoice == "weight":
      newWeight = input("Input new weight: ")
      db[patName + " " + patDoB].setWeight(newWeight)
    elif attChoice == "allergies":
      addOrRemove = input("Add or remove: ").lower()
      if addOrRemove == "add":
        newAllergy = input("Input new allergy: ")
        db[patName + " " + patDoB].addAllergies(newAllergy)
      elif addOrRemove == "remove":
        newAllergy = input("Input allergy to remove: ")
        db[patName + " " + patDoB].removeAllergies(newAllergy)
    elif attChoice == "illnesses":
      addOrRemove = input("Add or remove: ").lower()
      if addOrRemove == "add":
        newIllness = input("Input new illness: ")
        db[patName + " " + patDoB].addIllness(newIllness)
      elif addOrRemove == "remove":
        newIllness = input("Input illness to remove: ")
        db[patName + " " + patDoB].removeIllness(newIllness)
    elif attChoice == "medicine":
      addOrRemove = input("Add or remove: ").lower()
      if addOrRemove == "add":
        newMedicine = input("Input new medicine: ")
        db[patName + " " + patDoB].addMedicine(newMedicine)
      elif addOrRemove == "remove":
        newMedicine = input("Input medicine to remove: ")
        db[patName + " " + patDoB].removeMedicine(newMedicine)
  
  def addPatient(self): 
    '''Allows user to add a new patient along with the accompanying information: Name, age, gender, date of birth, department, height, weight, allergies, illnesses, and medicines.'''
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
    print("Patient added!")
    

#patientA = Patient("Samantha Chu", 22, "F", "01-01-2000", "Hematology", 70, 150,['Penicillin', 'Pollen'],['Sickle Cell Disease: Severe', 'Low Blood Pressure: Benign'],['Ramipril', 'Hydroxyurea'])
#print(patientA.viewMedRecord())

#doctor object that can be used to call doctor functions
db.update({"hi":["age", "gender", "DoB", "department", "password"]})
testDoctor = Doctor("name", "age", "gender", "DoB", "department")
db["bob" + " " + "9"] = Patient("bob","9","9","9","9","9","9","","","")
    
#menu
def menu():
  '''Displays all the options available to choose from'''
  print("1. View personal information")
  print("2. Add Patient Info")
  print("3. Doctor functions")
  print("4. View/Edit Registered Patient List")
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
  if selection == '3':
    print("1. View schedule")
    print("2. Edit schedule")
    print("3. Change patient attribute")
    choice = input("Enter a number: ")
    if choice == '1':
      dis_guy = input("Enter your name to view the schedule: ")
      doctorInfo = Doctor(dis_guy, db[dis_guy][0], db[dis_guy][1],db[dis_guy][2], db[dis_guy][3])
      doctorInfo.viewSchedule()
    if choice == '2':
      dis_guy = input("Enter your name to edit the schedule: ")
      doctorInfo = Doctor(dis_guy, db[dis_guy][0], db[dis_guy][1],db[dis_guy][2], db[dis_guy][3])
      doctorInfo.editSchedule()
    if choice == '3':
      testDoctor.changeAttribute()
  if selection == '4':
    print('1. View Registered Patients')
    print('2. Register New Patient')
    print('3. Unregister Patient')
    choose = input('Enter a Number: ')
    hm = HospitalManagement()
    if choose == '1':
      print(hm.viewPatientList())
    elif choose == '2':
      patientToAdd = input('Input the name of the patient to register: ')
      hm.enlistPatient(patientToAdd)
    elif choose == '3':
      patientToRemove = input('Input the name of the patient being discharged: ')
      hm.removePatient(patientToRemove)

    #Main function
def main():
  '''This is the main function call for the management system'''
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


