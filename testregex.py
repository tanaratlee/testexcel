import re
result = re.search(r'aza',"plaza")
print(result)
if result is not None: print("คนหาเจอ")
else : print("คนหาไม่เจอนะครับ")

result = re.search(r'azaa',"plaza")
print(result)
if result is not None: print("คนหาเจอ")
else : print("คนหาไม่เจอนะครับ")


txtinput = 'dรหัส= 123-349,388338 ,4523,432ds \n'
print(txtinput)
txtinput=re.sub(r"\s+","",txtinput)  #cleaning whitespace
print(txtinput)


result = re.search(r'รหัส=([\w\s\-\,]*)',txtinput)
print(result)
strParts = ""
if result is not None:
  print(result[0])
  print(result[1])
  strParts=result[1]
  lstParts= strParts.split(',')
  print(lstParts) 
else:
  print("Not Match")





