import random
import string

def rString(length):
    result = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length)])
    return(result)

def rInt(min, max):
    return(random.randint(min, max))

def rFloat(min, max, precision):
    return(round(random.uniform(min, max), precision))

def rTupleInt(min, max, length):
    result = ()
    for index in range(length):
        result += (rInt(min, max),)
        index += 1
    return(result)

def rTupleStr(stringLength, length):
    result = ()
    if stringLength == 1:
        result += (rString(length).split(),)
    else:
        for index in range(length):
            result += (rString(stringLength),)
            index += 1
    return(result)

def main():
    while True:
        num = input("test>  ")
        if (not num or not num.isdigit()):
            continue
        else:
            break
    num = int(num)
    result_str = rString(num)
    result_float = rFloat(-num, num, 4)
    result_tuple = rTupleInt(0, 100, num)
    print((result_str, result_float, result_tuple))

if __name__ == "__main__":
    main()