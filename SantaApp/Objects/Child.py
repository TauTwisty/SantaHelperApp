class Child:

    def __init__(self, id, name, surname, gift):
        self.id = id
        self.name = name
        self.surname = surname
        self.gift = gift
    
    def GetId(self):
        return self.id

    def GetName(self):
        return str(self.name)

    def GetSurname(self):
        return str(self.surname)
    
    def GetGift(self):
        return str(self.gift)
    
    def GetFullName(self):
        return str(self.name+";"+self.surname)