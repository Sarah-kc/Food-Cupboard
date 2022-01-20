# ----------------------------------------------------------
# --------            HW 8: Food Cupboard          ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name: Sarah Cryan
# Time spent on this problem: 4.5 hrs
#
# Collaborators and sources: Alan (in Open Lab)
#   (List any collaborators or sources here.)
#
# ----------------------------------------------------------
import string
import doctest

banner = """                        WELCOME TO THE HAMILTON
  ______              _    _____            _                         _ 
 |  ____|            | |  / ____|          | |                       | |
 | |__ ___   ___   __| | | |    _   _ _ __ | |__   ___   __ _ _ __ __| |
 |  __/ _ \ / _ \ / _` | | |   | | | | '_ \| '_ \ / _ \ / _` | '__/ _` |
 | | | (_) | (_) | (_| | | |___| |_| | |_) | |_) | (_) | (_| | | | (_| |
 |_|  \___/ \___/ \__,_|  \_____\__,_| .__/|_.__/ \___/ \__,_|_|  \__,_|
                                     | |                                
                                     |_|                                
"""

categories = ["Fruit", "Vegetable","Fruit", "Vegetable", "Grain","Grain", "Dairy", "Dairy"]
foods = ["Bananas", "Cauliflower", "Mangoes", "Cabbage", "Wheat bread", "Rice", "Yogurt", "Milk"]

def getValidInput(qString, numMax):
    '''(str, int) -> int
    Uses the string parameter to form the input question and integer parameter
    to set the maximum quantity an input could be. Asks users for an input
    until receiving a numerical input greater than 1 and less than the maximum.
    '''
    quantMax = numMax 
    attainQuant = input(qString+" do you want? ")
    while attainQuant not in string.digits or int(attainQuant)<1 or int(attainQuant)>quantMax:
    # will iterate until the input is a digit between 1 and the maximum
        print("Enter a number between 1 and", quantMax)
        attainQuant = input(qString+" do you want? ")
        
    return int(attainQuant) #casts attainQuant as an int so it can be used for indexing

def printCategories(categories):
    '''(lst) -> str
    The list passed contains the category of each food available to be selected. The
    function prints out all  categories and returns whichever category the
    user chooses as a string.
    '''
    print("Categories:")
    foodList = [] #list that will store the categories, excluding duplicates
    for item in categories:
        if item not in foodList: #makes sure the foodList has no repeat foods appended
            foodList.append(item)
    for pos in range(len(foodList)):
        print(str(pos+1)+".",foodList[pos])
        
    posCat = (getValidInput("Which category",len(foodList)))-1
    #gets the users desired category and subtract 1 because indexing starts at 0
        
    chosenFoodGroup = foodList[posCat]
    return chosenFoodGroup

def printFoodOptions(foodGroup, categories, foods):
    '''(str, lst, lst) -> str
    Creates a list of the foods that share the category selected by the user.
    Prints the foods within the category and returns the user's food purchase
    choice input.
    '''
    count = 1
    choiceList = [] #list that will store the foods in the selected category
    for i in range(len(foods)):
        if categories[i] == foodGroup: #checks for foods that share the same category as the category selected by the user
            choiceList.append(foods[i])
            print(str(count)+".",foods[i]) #prints the foods in the selected category
            count+=1 #counter keeps track of what number the food is on the list (i doesn't always correlate)
            
    posFood = (getValidInput("Which food",len(choiceList)))-1
    #gets the users desired food and subtract 1 because indexing starts at 0
    
    chosenFoodItem = choiceList[posFood] 
    return chosenFoodItem

def printUnitsUsed(unitsLeft):
    '''(int) -> int
    Informs user of the purchasing credits they have left and gets the number of credits
    the user would like to spend on the selected food item. Returns how many credits were
    used for that specific food item.
    '''
    print("Remaining credits:", unitsLeft)
    unitsUsed = getValidInput("How many units", unitsLeft) 
    return unitsUsed

def displaySummary(foodsPurchased, numFoodsPurchased):
    '''(lst, lst)
    Using a list of the users food purchases and how many of those
    foods they purchased, the function prints a summary of their shopping
    >>> displaySummary(["sheep", "cattle"],[2,4])
    Foods requested:
    * sheep (x2)
    * cattle (x4)
    >>> displaySummary(["chicken", "lamb"],[12,25])
    Foods requested:
    * chicken (x12)
    * lamb (x25)
    >>> displaySummary(["fish", "frog"],[1,34227])
    Foods requested:
    * fish (x1)
    * frog (x34227)
    '''
    print("Foods requested:")
    for foodPos in range(len(foodsPurchased)):
        print("*",foodsPurchased[foodPos],"(x"+str(numFoodsPurchased[foodPos])+")")
                            


def main():
    print(banner)
    pickedFoods=[] #stores foods selected (without repeats)
    numOfPickedFoods=[] #stores quantity of foods
    units = 10
    while units>0: #iterates while there are credits left to spend 
        chosenFoodGroup = printCategories(categories)
        chosenFoodItem = printFoodOptions(chosenFoodGroup, categories, foods)
        unitsUsed = printUnitsUsed(units)
        units-=unitsUsed 
        if chosenFoodItem not in pickedFoods: #appends only non-repeat foods and their quantity
            pickedFoods.append(chosenFoodItem)
            numOfPickedFoods.append(unitsUsed)
        else:
            numIndex = pickedFoods.index(chosenFoodItem)
            numOfPickedFoods[numIndex]+=unitsUsed #increases the num of picked foods for a repeat food choice
    displaySummary(pickedFoods, numOfPickedFoods)
                   

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
