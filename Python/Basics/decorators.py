def announce(f):
    def wrapper():
        print("About to run this function")
        f()
        print("done with the function")
    return wrapper
    
@announce
def hello():
    print("Hello,world!")
   

hello()