 
# string

str= "aakansha"
print(len(str))

#slicing

str="hello world"     #slicing is always count from index 0
print(str[5:])
print(str[:5])
print(str[3:8])
print(str[-8:-3])     #slicing baackward counting
print(str[-9:-2])

str="aakansha hello"
print(str.endswith("lo"))               # return true if it ends with substr (True)
print(str.capitalize())                 # capatilize 1 st letter (Aakansha)
print(str.replace("hello" , "Hujare"))  # replace words or letter from old to new one(Hujare)
print(str.find("ll"))                   # find the str and write 1 index in 1 occurance(9) 
print(str.count("a"))                   # count the occurance of substr from whole str (4)
