# Eduard Onisa Esercizi

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

#3.3 Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.

mode_of_transportation= ["car", "train", "bus", "plane"]     #creo elenco

for mode in mode_of_transportation:                           #stampo affermazioni
    if mode == "car" :
        print ("I'm used to travelling by car")
    elif mode == "train" :
        print ("I like travelling by train")
    elif mode == "bus" :
        print ("I hate travelling by bus")
    elif mode == "plane" :
        print ("I haven't travelled by plane for a year")
    else:
        print ("I haven't travelled with this mode yet")


#3.4 Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guest_list = ["Albert Einstein", "Lino Banfi", "Catherine Middleton"]     #creo lista

for guest in guest_list:
    print (f"Hello dear", guest + ",", "you are invited to dinner at my home, I'll wait for you!")     #stampo inviti

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in your list.

guest_list = ["Albert Einstein", "Lino Banfi", "Catherine Middleton"]

guest_absent = guest_list.pop(0)
print (guest_absent, "doesn't come to dinner")
  
new_guest = "Cristoforo Colombo"  
guest_list.insert (0, new_guest)
print (f"Hello dear", new_guest + ",", "you are invited to dinner at my home, I'll wait for you!")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.

guest_list = ["Albert Einstein", "Lino Banfi", "Catherine Middleton"]

guest_absent = guest_list.pop(0)
print (guest_absent, "doesn't come to dinner")
  
new_guest = "Cristoforo Colombo"  
guest_list.insert (0, new_guest)

print ("I find a new dinner table!")
guest_list.insert(0, 'Leonardo Da Vinci') 
guest_list.insert(len(guest_list) // 2, 'Michelangelo')  
guest_list.append('Sergio Mattarella')
for guest in guest_list:
    print (f"Hello dear", guest + ",", "you are invited to dinner at my home, I'll wait for you!")


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
• Print a message to each of the two people still on your list, letting them know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ["Cristoforo Colombo", "Lino Banfi", "Catherine Middleton", "Leonardo Da Vinci", "Michelangelo", "Sergio Mattarella"]

print("Sorry, but I can only invite two people for dinner.")

while len(guest_list) > 2:
    remove_guest = guest_list.pop(0)
    print("Sorry", remove_guest + ",", "I can't invite you to dinner.")

for guest in guest_list:
    print("Dear", guest + ",", "You are invited to dinner.")

del guest_list[4:5]
print("Empty list:", guest_list)


#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse()  to change the order of your list. Print the list to show that its order has changed.
• Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse-alphabetical order.
Print the list to show that its order has changed.

places_to_visit = ["Japan", "Spain", "Australia", "Senegal", "Bolivia"]

print("Original order:", places_to_visit)

print("Alphabetical order:", sorted(places_to_visit))

print("Original order after sorted():", places_to_visit)

print("Reverse-alphabetical order:", sorted(places_to_visit, reverse=True))

print("Original order after sorted() for reverse-alphabetical order:", places_to_visit)

places_to_visit.reverse()
print("Reversed order:", places_to_visit)

places_to_visit.reverse()
print("Back to original order after second reverse():", places_to_visit)

places_to_visit.sort()
print("Alphabetical order after sort():", places_to_visit)

places_to_visit.sort(reverse=True)
print("Reverse-alphabetical order after sort():", places_to_visit)

#3-9. Dinner Guests: Working with one of the programs from Exercises 3, use len() to print a message indicating the number of people you’re inviting to dinner.
guest_list = ["Albert Einstein", "Lino Banfi", "Catherine Middleton", "Leonardo Da Vinci", "Michelangelo", "Sergio Mattarella"]

print("People invited:", len(guest_list))

for guest in guest_list:
    print("Dear", guest + ",", "you are invited to dinner at my home, I'll wait for you!")

#3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

things_list = ["Dolomiti", "Danubio", "Canada", "Genova", "HTML", "Peach"]

print("Original list:", things_list)

things_list.append("Genoa's acquarium")
print("After appending:", things_list)

things_list.insert(2, "Mississippi river")
print("After inserting:", things_list)

removed_item = things_list.pop(4)
print("Removed item:", removed_item)
print("After popping:", things_list)

things_list.remove("Peach")
print("After removing:", things_list)

things_list.sort()
print("After sorting:", things_list)

things_list.reverse()
print("After reversing:", things_list)

index = things_list.index("Mississippi river")
print("Index of 'Mississippi river':", index)

count = things_list.count("Canada")
print("Occurrences of 'Canada':", count)

things_list.clear()
print("After clearing:", things_list)

#6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

dictionary = {
  "first_name": "Eros",
  "last_name": "Ramazzotti",
  "age": 60,
  "city": "Rome",
}

print("First Name:", dictionary['first_name'])
print("Last Name:", dictionary['last_name'])
print("Age:", dictionary['age'])
print("City:", dictionary['city'])

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

favorite_number = {
    'Giovanni': 4,
    'Franco': 7,
    'Ivan': 10,
    'Marina': 15,
    'Nicole': 20
}

for person, number in favorite_number.items():
    print(person + "'s favorite number is", number)

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
• Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'variable': "A symbolic name that represents a value",
    'loop': "A programming structure that repeats a block of code",
    'function': "A block of reusable code designed to perform a specific task",
    'dictionary': "A data structure used to store and organize data in key-value pairs",
    'list': "A collection of ordered elements"
}

for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")

#6-7. People: Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

firstperson = {
    "first_name": "Eros",
    "last_name": "Ramazzotti",
    "age": 60,
    "city": "Rome",
}

secondperson = {
    "first_name": "Gerry",
    "last_name": "Scotti",
    "age": 67,
    "city": "Pavia",
}

thirdperson = {
    "first_name": "Luca",
    "last_name": "Laurenti",
    "age": 61,
    "city": "Roma",
}

people = [firstperson, secondperson, thirdperson]

for person in people:
    print("First Name:", person['first_name'])
    print("Last Name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])
    print() 

#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet. 

firstanimal = {"species": "dog", "owner": "Jack"}
secondanimal = {"species": "rabbit", "owner": "Mark"}
thirdanimal = {"species": "cat", "owner": "Harry"}

pets = [firstanimal, secondanimal, thirdanimal]

for animal in pets:
    print("Species:", animal["species"])
    print("Owner:", animal["owner"])
    print() 
