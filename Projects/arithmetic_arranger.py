problems = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems, bool_value=None):
    line_one = ""
    line_two = ""
    line_three = ""
    line_four = ""
    if(len(problems)<=5):
        for line_1 in problems:
            if(line_1.islower() or line_1.isupper()):
                return "Error: Numbers must contains only digits."
                break
            else:
                segments = line_1.split()
                first_number = segments[0]
                operator = segments[1]
                second_number = segments[2]
                max_seg = first_number if len(first_number) > len(second_number) else second_number
                if(operator=='+' or operator=='-'):
                    if((len(first_number) <= 4) or (len(second_number) <= 4)):
                        result_line_one = "  " + " "*(len(max_seg) - len(first_number)) + first_number + "\t"
                        line_one = line_one + result_line_one
                    else:
                        return "Error: Numbers cannot be more than four digits."
                        break
                else:
                    return "Error: Operator must be '+' or '-'."
                    break
        
        for line_2 in problems:
            if(line_2.islower() or line_2.isupper()):
                return "Error: Numbers must contains only digits."
                break
            else:
                segments = line_2.split()
                first_number = segments[0]
                operator = segments[1]
                second_number = segments[2]
                max_seg = first_number if len(first_number) > len(second_number) else second_number
                if(operator=='+' or operator=='-'):
                    if((len(first_number) <= 4) or (len(second_number) <= 4)):
                        result_line_two = operator + " " + " "*(len(max_seg) - len(second_number)) + second_number + "\t"
                        line_two = line_two + result_line_two
                    else:
                        return "Error: Numbers cannot be more than four digits."
                        break
                else:
                    return "Error: Operator must be '+' or '-'."
                    break
        
        for line_3 in problems:
            if(line_3.islower() or line_3.isupper()):
                return "Error: Numbers must contains only digits."
                break
            else:
                segments = line_3.split()
                first_number = segments[0]
                operator = segments[1]
                second_number = segments[2]
                max_seg = first_number if len(first_number) > len(second_number) else second_number
                if(operator=='+' or operator=='-'):
                    if((len(first_number) <= 4) or (len(second_number) <= 4)):
                        result_line_three = "-"*(2 + len(max_seg)) + "\t"
                        line_three = line_three + result_line_three
                    else:
                        return "Error: Numbers cannot be more than four digits."
                        break
                else:
                    return "Error: Operator must be '+' or '-'."
                    break
        
        for problem in problems:
            segments = problem.split()
            first_number = segments[0]
            operator = segments[1]
            second_number = segments[2]
            max_seg = first_number if len(first_number) > len(second_number) else second_number
            if(operator=='+'):
                result = int(first_number) + int(second_number)
                result_line_four = "  " + " "*(len(max_seg) - len(str(result))) + str(result) + "\t"
                line_four = line_four + result_line_four
            else:
                result = int(first_number) - int(second_number)
                result_line_four = "  " + " "*(len(max_seg) - len(str(result))) + str(result) + "\t"
                line_four = line_four + result_line_four

    else:
        return "Error: Too many problems."
    
    if(bool_value==True):
        arranged_problems = line_one + "\n" + line_two + "\n" + line_three + "\n" + line_four
        return arranged_problems
    elif(bool_value==None):
        arranged_problems = line_one + "\n" + line_two + "\n" + line_three
        return arranged_problems
    else:
        arranged_problems = line_one + "\n" + line_two + "\n" + line_three
        return arranged_problems

print(arithmetic_arranger(problems, True))