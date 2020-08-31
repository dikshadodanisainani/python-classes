introString=input("Enter string:")
characterCount=0
wordCount=1
for i in introString:
      print(i)
      characterCount=characterCount+1
      if(i ==' '):
            wordCount=wordCount+1
print("no of words in your name are " )
print( wordCount)
print("no of char in your name are ")
print( characterCount)