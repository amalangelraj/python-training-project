class BaseError(Exception):
    pass  # Base Class
class FormulaError(BaseError):
    pass  # Raise for invalid input values

def extract_values(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

# Addition
def add(a,b):
    return a+b

# Subtraction
def sub(a,b):
    return a-b

# Multiplication
def mul(a,b):
    return a*b

operators={'+':add,
           '-':sub,
           }

def mathwork(strinput):
    try:
        # Input_Number = strinput[0]
        # if not Input_Number.isdigit():
        #     raise Not_Suitable_value_exception
        # break
        if ((len(strinput)-strinput.count(" ") == 3)):
            word = strinput[2]
            # print(word)
            # for word in strinput.split(" "):
            # word = strinput[2]
            if ( (word in operators.keys()) and ((word == '+') or (word == '-')) ) :
                try:
                    program_inputs = extract_values(strinput)
                    calculate = operators[word.upper()] (program_inputs[0],program_inputs[1])
                    message = calculate
                    return message

                except FormulaError:
                    pass
                    # print('something went wrong going plz enter again !!')
                finally:
                    print(" The finally is executed")
            # return message
            # break

            # elif():
            else:
                raise FormulaError
                # else:
                #     raise FormulaError
        else:
            raise FormulaError

    except FormulaError:
        pass
        # print("FormulaError, Invalid input, give input again please")
        # print()


userinput = [ x for x in input().split(",") if x !=""]
# print(userinput)

# print(userinput[0])

# strinput = userinput[0]

for i in range(0,3,1):
    # for i in range(0,1,1):
    strinput = userinput[i]
    # print(i)
    # print("strinput is", strinput)
    print(mathwork(strinput))
    # print(mathwork("5 * 2"))


# print(strinput)

# print(extract_values(userinput[0]))
