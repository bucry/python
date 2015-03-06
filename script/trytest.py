s=input("input your age:") 
if s=="": 
    raise Exception("input must not be empty.") 
 
try: 
    i=int(s) 
except Exception as err: 
    print(err) 
finally: 
    print("Goodbye!") 

s=input("input your age:")
if s=="":
 raise Exception("input must not be empty.")

try:
 i=int(s)
except Exception as err:
 print(err)
finally:
 print("Goodbye!")


try:
     file("hello.txt", "r")                  
     print "read"
except IOError:                              
     print "file not find"
except:                                 
     print "exception" 
