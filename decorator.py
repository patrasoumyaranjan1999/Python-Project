def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print('thanks for usinng function')
    return mfx
@greet
def hello():
    print("hello world")
    
hello()