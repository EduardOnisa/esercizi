# Eduard Onisa 18/04/2024

#2.3 Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"

# Questa variabile contiene il nome
name: str= "Alex"

# Questa variabile contiene il messaggio
message: str= f"Hello {name}, would you like to learn some Python today?"

print(message)



#2.4 Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case

#Questa è una variabile che contiene il nome di una persona
name: str= "Alex"

#Questa variabile contiene il nome minuscolo
name_lower: str = name.lower()

#Questa variabile contiene il nome maiuscolo
name_upper: str = name.upper()

print (f"{name}, {name_upper}, {name_lower}")



#2.5 Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, "A person who never made a mistake never tried anything new"

#Questa è una variabile che contiene il nome di una persona 
name: str= "Fabrizio Caramagna"

#Questa è la citazione
cit: str= "The sea is the only labyrinth that contains thousands of exits"

print (f"{name}, once said {cit}")



#2.8 Python has a removesuffix() method that works exactly likeremoveprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension , like some file browsers do

filename: str= "python_nothes.txt"

print (filename.removesuffix(".txt"))

#3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
# Definisco la lista dei nomi
names = ["Gianluca", "Andrea", "Marco", "Giulia", "Alice"]

# Stampo il nome di ogni persona 
for name in names:
    print(name)

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.
#Lista dei nomi
names = ["Gianluca", "Andrea", "Marco", "Giulia", "Alice"]

#Stampo
for name in names:
    print(f"Hello, {name}! How are you today?")
