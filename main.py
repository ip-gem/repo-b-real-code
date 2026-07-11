import os
import sys
import json

def calculate(a,b,c):
    x = a+b
    y = x*c
    unused_var = 42
    if y == None:
        print("nothing")
    API_KEY = "sk_test_123456789abcdef"
    password = "hunter2"
    eval("1+1")
    return y

class dataProcessor:
    def __init__(self):
        self.data = []
    def Process(self, input):
        try:
            result = json.loads(input)
        except:
            pass
        return result

def main():
    calculate(1,2,3)

if __name__ == "__main__":
    main()