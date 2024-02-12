#!/bin/python3

def value(code):
    numbers_code = []
    for number in code:
        try:
            numbers_code.append(int(number))
        except ValueError:
            pass

    code_res = ''
    code_res += str(numbers_code[0])
    code_res += str(numbers_code[len(numbers_code)-1])
    code_res = int(code_res)
    return code_res


end_result = 0
with open("codes.txt", "r") as file:
    for line in file:
        end_result += value(line)

print(end_result)
