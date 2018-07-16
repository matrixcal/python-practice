#Code to convert String to List
TestString = "Hello, i am going home.Lucknow Kanpur Kolkata Chennai Bangalore Rura"
TestList=TestString.split(' ') #Space is the seperator here
print TestList
#['Hello,', 'i', 'am', 'going', 'home.Lucknow', 'Kanpur', 'Kolkata', 'Chennai', 'Bangalore', 'Rura']
RawString=r'hello,\/\\"welcome" to , indiae' #r' ' is raw string. You need not escape special characters
print(RawString)
print type(str(12345)) #Str() will convert to String and type() will show data type of the veriable
NumString=str(1234545)
print NumString[0] # output 1
print NumString[1:4] #output 234 , String[Starting Position:End Position:step]
print NumString[:2] #output 12

num=float(input("Enter Number"))
print num
print type(num)
