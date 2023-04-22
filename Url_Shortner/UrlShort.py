#it is a module 
import pyshorteners

#Exception Handling...
try:
    Link=input("Enter a Url: ")
    genratedlink=pyshorteners.Shortener().tinyurl.short(Link)
    print(genratedlink)
   

except Exception as e:
    #print exact error or a usefull message to user
    print("Please try again")
    print(e)   