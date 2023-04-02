
def solve(test_case):
    if(test_case == "RR"):
      return "R"
    if(test_case == "SS"):
      return "S"
    if(test_case == "PP"):
      return "P"
    if(test_case == "PR" or test_case == "RP"):
      return "P"
    if(test_case == "SR" or test_case == "RS"):
      return "R"
    if(test_case == "PS" or test_case == "SP"):
      return "S"
    return test_case

if __name__ == '__main__':
    with open('input/level1_5.in', 'r') as input_field, open('output/level1_5.out', 'w') as output_field:
        num = int(input_field.readline())

        for _ in range(num):
            inp = input_field.readline()
            result = solve(inp.split()[0])
            print(result, file=output_field)