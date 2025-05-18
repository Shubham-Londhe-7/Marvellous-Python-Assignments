
def Converter(value):
    Far = (value * (9/5)) + 32
    return Far

def main():
    print("Enter temperature in Celsius : ")
    temp = int(input())

    ret = Converter(temp)

    print("Temperature in Fahrenheit is : ",ret,"°F")

if __name__ == "__main__":
    main()