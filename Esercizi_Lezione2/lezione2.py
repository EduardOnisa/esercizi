# Eduard Onisa 18/04/2024 

#Use a variable to represent a person's name, and print a message to that person. Your message should be simple, such as, "Hello Eric, would you like to learn some Python today?"

# Questa variabile contiene il nome
name: str= "Alex"

# Questa variabile contiene il messaggio
message: str= f"Hello {name}, would you like to learn some Python today?"

print(message)



#Use a variable to represent a person's name, and then print that person's name in lowercase, uppercase, and title case

#Questa è una variabile che contiene il nome di una persona
name: str= "Alex"

#Questa variabile contiene il nome minuscolo
name_lower: str = name.lower()

#Questa variabile contiene il nome maiuscolo
name_upper: str = name.upper()

print (f"{name}, {name_upper}, {name_lower}")