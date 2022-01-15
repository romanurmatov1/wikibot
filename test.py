import wikipedia
 
# getting suggestions
result = wikipedia.search("Amir Temur", results = 5)
 
# printing the result
print(result)