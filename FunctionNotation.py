# function named notation

def greeting(name , age =28,color = "red"):

    print(f"hello {name.capitalize()}, you are {age} years old")
    print(f"we hear you like color {color.lower()}!")


greeting("sush",27,"BLUE")
greeting(name ="sush",age =35,color = "RED")

