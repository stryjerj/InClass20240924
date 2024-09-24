# dictionaries.py
# This was really fun and I will treasure this time together with my peers


def demo():
    """
    Demonstate basic dictionary stuff
    """
    myDictionary = {"Cincinnati":"Bearcats", "Xavier":"Musketeers", "NKU":"Norse", "UC Clermont":"Cougars"}
    print(myDictionary)
    

    # Iterate over the dictionary by ket
    
    for key in myDictionary.keys():
        print(key)
        

    # Iterate by value
    
    for item in myDictionary.items():
        print(item)
        
    # Iterate by value
    
    for value in myDictionary.values():
        print(value)

    # Add a key/value pair to the dictionary
    
    myDictionary["Michigan State"] = "Spartans"
    
    print(len(myDictionary))
    
    # Cause an exception. Add try / except logic to handle this
    
    try:
        print(myDictionary["Ohio State"])
    except:
        # We end up here if exception is thrown in the try block
        print("Ohio State is a valid key")  
    

    # Remove Xavier from the list
    
    myDictionary.pop("Xavier")
    print(myDictionary)
    
    # Create another dictionary called newTeams
    # Add several key/value pairs
    #combine that with myDictionary and print the results
    
    newTeams = {"Ohio State":"Buckeyes", "Michigan":"Wolverines", "Indiana":"Hoosiers", "Purdue":"Boilermakers"}
    """
    # Brute Force
    
    for key in newTeams.keys():
        myDictionary[key] = newTeams[key]
    print(myDictionary)
    """
    

    myDictionary.update(newTeams)
    print(myDictionary)