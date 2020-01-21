#Modulos
import modulo
modulo.saludo("Joaquin")
a = modulo.persona1["Edad"]
print(a)
#Datos Sistemas
import platform
x = platform.system()
print(x)
x = dir(platform)
print(x)
#Datos fechas
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
""""
%a	Weekday, short version	Wed	 
%A	Weekday, full version	Wednesday	 
%w	Weekday as a number 0-6, 0 is Sunday	3	 
%d	Day of month 01-31	31	 
%b	Month name, short version	Dec	 
%B	Month name, full version	December	 
%m	Month as a number 01-12	12	 
%y	Year, short version, without century	18	 
%Y	Year, full version	2018	 
%H	Hour 00-23	17	 
%I	Hour 00-12	05	 
%p	AM/PM	PM	 
%M	Minute 00-59	41	 
%S	Second 00-59	08	 
%f	Microsecond 000000-999999	548513	 
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	 
%U	Week number of year, Sunday as the first day of week, 00-53	52	 
%W	Week number of year, Monday as the first day of week, 00-53	52	 
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	 
%x	Local version of date	12/31/18	 
%X	Local version of time	17:41:00
"""
#MODULO JSON
import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)

#MODULO REGEX
import re 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)