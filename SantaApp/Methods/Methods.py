#imports
import Objects.Child as Child
import Objects.Gift as Gift
import random
import os as os

#Attributes
gifts = []
children = []
Gifts_List = []
Children_List = []
assignedChildren = []

#Method - For reading lines
def ReadFile(fileName):
    f = open(fileName, 'r')
    result = f.readlines()
    f.close()
    return result

#Method - For displaying all gifts and children
gifts = ReadFile('Files/Gifts.txt')
children = ReadFile('Files/Children.txt')

for gift in gifts:
    splitted = gift.split(';')
    id = int(splitted[0])
    name = str(splitted[1])
    Gifts_List.append(Gift.Gift(id, name))

for child in children:
    splitted = child.split(';')
    id = int(splitted[0])
    name = str(splitted[1])
    surname = str(splitted[2])
    Children_List.append(Child.Child(id, name,surname,"0"))

def DisplayAllGifts():
    for gift in Gifts_List:
        print(str(gift.GetName()), end="")
    
def DisplayAllChildren():
    for child in Children_List:
        print(str(child.GetFullName()), end="")

#Method - Assign random toys to some/all children
def AssignToys(toAll):#Boolean parameter that determines if toys will be assigned to all children or some
    if toAll == False:#some
        for child in Children_List:
            r = random.randint(0, len(Gifts_List) - 1)
            assignedChildren.append(Child.Child(child.GetId(), child.GetName(), child.GetSurname(), Gifts_List[r].GetName()))
            
        if os.path.exists('Files/Assigned.txt'):
            os.remove('Files/Assigned.txt')

        f = open('Files/Assigned.txt', 'w')

        for a in assignedChildren:
            fName =   str(a.GetFullName()).strip()
            giftName = str(a.GetGift()).strip()    
            f.write( fName +";"+ giftName + "\n")

    if toAll == True:#all
        for child in Children_List:
            r = random.randint(1, len(Gifts_List) - 1)
            assignedChildren.append(Child.Child(child.GetId(), child.GetName(), child.GetSurname(), Gifts_List[r].GetName()))
            
        if os.path.exists('Files/Assigned.txt'):
            os.remove('Files/Assigned.txt')

        f = open('Files/Assigned.txt', 'w')

        for a in assignedChildren:
            fName =   str(a.GetFullName()).strip()
            giftName = str(a.GetGift()).strip()    
            f.write( fName +";"+ giftName + "\n")

#Method - Assign a certain gift to a specific children
def AssignGift():    
    name = str(input("Please write childs name: "))
    surname = str(input("Please write childs surname: "))  
    gift = str(input("Please write childs gift: "))  

    thereIs = False
    temp = ""

    assignedChildren = ReadFile("Files/Assigned.txt")

    for child in assignedChildren:
        splitted = child.split(';')
        oldName = str(splitted[0])
        oldSurname = str(splitted[1])          
        if oldName == name and oldSurname == surname:
            thereIs = True
            temp = str(splitted[2])
    
    if thereIs == True:

        with open("Files/Assigned.txt", 'r') as f:
            lines = f.readlines()
        with open("Files/Assigned.txt", 'w') as f:
            for line in lines:
                if str(line) != str(name+";"+surname+";"+str(temp)):
                    f.write(line)    
        f.close()
        f2 = open("Files/Assigned.txt", 'a')
        f2.write(str("\n"+name+";"+surname+";"+gift))        
        
        f2.close()
    else:
        print("Santa, this child does not exist in the registry. \nPlease add a new child.")
        print("If the child still does not exist in the registry, please do the following:")
        print("1st - Add a new child to the registry.")
        print("2nd - Assign random gifts to ALL children.")
        print("3rd - Try this action again.")

#Method - Add a new gift (can repeat)
def AddNewGift():
    newId = int(Gifts_List[len(Gifts_List) - 1].GetId() + 1)
    newGift = str(input("Please write a new gift: "))

    f = open("Files/Gifts.txt",'a')
    f.write(str(newId)+";"+newGift)
    f.close()
        

#Method - Add a new child (can not repeat)
def AddNewChild():
    newId = int(Children_List[len(Children_List) - 1].GetId() + 1)
    name = str(input("Please write childs name: "))
    surname = str(input("Please write childs surname: ")) 
    thereIs = False

    if name.isalpha() and surname.isalpha():

        for child in Children_List:
            oldName = str(child.GetName()).strip()
            oldSurname = str(child.GetSurname()).strip()          
            if oldName == name and oldSurname == surname:
                thereIs = True
        
        if thereIs == False:
            f = open("Files/Children.txt",'a')
            f.write(str(newId)+";"+name+";"+surname)
            f.close()
        else:
            print("Santa, this child is already in the registry.")
    else:
        print("Santa, no symbols or numbers. \nOnly alphabetical symbols.")

#Method - Assign gift to a child
def DisplayAssignedPairs():
    s = 0    
    assigned = ReadFile("Files/Assigned.txt")
    for child in assigned:
        splitted = child.split(';')
        cleaned = splitted[2].strip()
        if str(cleaned) != str('0'):
            s = s + 1        
    
    print("Number of assigned pairs: "+ str(s))

#Method - Number of unassigned children
def DisplayNumberOfUnassignedChildren():
    s = 0
    assigned = ReadFile("Files/Assigned.txt")
    for child in assigned:
        splitted = child.split(';')
        cleaned = splitted[2].strip()
        if str(cleaned) == str('0'):
            s = s + 1       
    print("Number of unassigned children: "+ str(s))

#Method - Number of unassigned gifts
def DisplayNumberOfUnassignedGifts():
    s = 0
    assigned = ReadFile("Files/Assigned.txt")
           
    for gift in Gifts_List:
        cleanedGift = str(gift.GetName()).strip()
        for a in assigned:
            splitted = a.split(';')
            cleaned = splitted[2].strip()
            if str(cleaned) != str('0') and str(cleaned) == cleanedGift:
                s = s + 1
                break
    
    giftCount = ReadFile("Files/Gifts.txt")
    result = len(giftCount) - s
    print("Number of unassigned gifts: " + str(result))
