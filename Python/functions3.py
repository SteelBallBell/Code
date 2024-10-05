def person(name, **data):
    print(data)
    print('name ' + name)
    
    for i,j in data.items(): # this confused me at first but this is just how you work with key value pairs.
        print(i,j) # because age is i and 25 is j and country is i and usa is j and numero is i and 922890 is j it prints them line by line.

person('john',age=25 , country='USA', numero=922890)