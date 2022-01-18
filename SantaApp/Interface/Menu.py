import Objects.Child as Child
import Objects.Gift as Gift
import Methods.Methods as Methods

class Menu:

    def PlayMenu():
        while True:
            des = 10
            print("")
            print("1 - Print detailed registry information")
            print("2 - Add a new gift")
            print("3 - Add a new child")
            print("4 - Assign gift to a child")
            print("5 - Assign random gifts to children")
            print("6 - Assign random gifts to all children")
            print("0 - Exit")

            try:
                des = int(input("Selected action: "))
            except:
                print("Please write down a number.")
            if des == 0:
                print("Good luck Santa!")
                break
            
            #1
            if des == 1:
                des2 = 7
                print("")
                print("1 - Print the amount of assigned pairs")
                print("2 - Print all names and all gifts")
                print("3 - Number of unassigned children")
                print("4 - Number of unassigned gifts")
                print("0 - Return")
                try:
                    des2 = int(input("Selected action: "))
                except:
                    print("Please write down a number")

                if des2 == 1:
                    print("")
                    Methods.DisplayAssignedPairs()
                if des2 == 2:
                    print("----------------------------------------------------------------")
                    print("All gifts in Registry:")
                    print("----------------------------------------------------------------")
                    Methods.DisplayAllGifts()
                    print("\n----------------------------------------------------------------")
                    print("All children in Registry:")
                    print("----------------------------------------------------------------")
                    Methods.DisplayAllChildren()
                    print("\n----------------------------------------------------------------")

                if des2 == 3:
                    print("")
                    Methods.DisplayNumberOfUnassignedChildren()
                if des2 == 4:
                    print("")
                    Methods.DisplayNumberOfUnassignedGifts()
                if des2 == 0:
                    continue
                if des2 > 4:
                     print("Santa, there is no such action. \nPlease write down numbers from 1 to 4 or 0 if you want to return.")
                print("1st action is done")

            #2
            if des == 2:
                print("")
                Methods.AddNewGift()
                print("2nd action is done")

            #3
            if des == 3:
                print("")
                Methods.AddNewChild()
                print("3rd action is done")

            #4
            if des == 4:
                print("")
                Methods.AssignGift()
                print("7th action is done")

            #5
            if des == 5:
                print("")
                Methods.AssignToys(False)
                print("5th action is done")

            #6  
            if des == 6:
                print("")
                Methods.AssignToys(True)
                print("6th action is done")
            if des > 6:
                print("Santa, there is no such action. \nPlease write down numbers from 1 to 6 or 0 if you want to exit.")
                
