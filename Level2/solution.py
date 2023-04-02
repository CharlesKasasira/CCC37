
def fight(fighters):
  if(fighters == "RR"):
    return "R"
  if(fighters == "SS"):
    return "S"
  if(fighters == "PP"):
    return "P"
  if(fighters == "PR" or fighters == "RP"):
    return "P"
  if(fighters == "SR" or fighters == "RS"):
    return "R"
  if(fighters == "PS" or fighters == "SP"):
    return "S"
  return fighters
    


def solve(test_case):
    newStr = ""
    afterRound = ""

    round = 0
    while(int(len(test_case)) > 2):
       round += 1
       for i in range(int(len(test_case))):
        if(i%2 == 0):
          newStr += fight("".join(list(test_case[i: i+2])))
       test_case = newStr
       if(round == 2):
             afterRound += newStr
             return afterRound
       newStr = ""

if __name__ == '__main__':
    with open('input/level2_5.in', 'r') as input_field, open('output/level2_5.out', 'w') as output_field:
        num = int(input_field.readline().split()[0])

        for _ in range(num):
            inp = input_field.readline()
            result = solve(inp.split()[0])
            print(result, file=output_field)