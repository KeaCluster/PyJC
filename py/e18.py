#Python Try Excep
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

#Raise an Exception
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")

#Diferencias inputs 
    #Python 3.6 
username=input("Entre el nombre: ")
print("USUARIO ES: " + username)
    #Python 2.7
username=raw_input("Entre el nombre")
print("USUARIO ES: " + username)
