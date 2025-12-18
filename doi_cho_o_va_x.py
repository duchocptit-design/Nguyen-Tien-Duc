def func_a(number1, number2):
    if number1 <= number2:
        return number1
    return number2

def func_b(patterns):
    count = patterns.count('O')
    answer = 0
    for i in range(count, len(patterns)):
        if patterns[i] == 'O':
            answer += 1
    return answer

def func_c(patterns):
    count = patterns.count('X')
    answer = 0
    for i in range(count, len(patterns)):
        if patterns[i] == 'X':
            answer += 1
    return answer

def solution(patterns):
    pattern1_first = func_b(patterns)
    patterns2_first = func_c(patterns)
    return func_a(pattern1_first-patterns2_first)

patterns=input("Hãy nhập 1 chuỗi(chỉ có X và O và không có dấu cách):")
number1=func_b(patterns)
number2=func_c(patterns)
result=func_a(number1,number2)
print(result)