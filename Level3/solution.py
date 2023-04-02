
def solve(test_case):
    
    newArr = []
    for i in range(len(test_case)):
        if(len(test_case[i]) == 2):
          for j in range(int(test_case[i][0])):
              newArr.append(test_case[i][1])
        if(len(test_case[i]) == 3):
          # print(test_case[i][:2])
          for j in range(int(test_case[i][:2])):
              # print(test_case[i][1])
              newArr.append(test_case[i][-1])
        if(len(test_case[i]) == 4):
          # print(test_case[i][:3])
          for j in range(int(test_case[i][:3])):
              newArr.append(test_case[i][-1])
    # print(newArr)

    newArr2 = []
    if(int(test_case[0][0]) > 1):
      # print("yes")
      newArr2.append("R")
      if("R" in newArr):
       newArr.remove("R")
      
      if("R" in newArr):
       newArr.remove("R")
      
    while(len(newArr) > 0):
        # print(len(newArr))
        if(newArr[0] == "R"):
          newArr2.append("R")
          newArr2.append("P")
          if("P" in newArr):
            newArr.remove("R")
            newArr.remove("P")
          elif("R" in newArr):
            newArr.remove("R")
        elif(newArr[0] == "P"):
          newArr2.append("P")
          if("P" in newArr):
            newArr.remove("P")
        elif(newArr[0] == "S"):
          newArr2.append("S")
          newArr.remove("S")
        else:
          newArr2.append(newArr[0])
          newArr.remove(newArr[0])
          
    
    # print(newArr)
    # print("".join(newArr2))
    return "".join(newArr2)

    print("====================")
    
    # for item in test_case:
    #     # print(item[0])
    #     newArr = []
    #     for i in range(int(item[0])):
    #         newArr.append(item[1])
    #     print(newArr)
    #     print("++++++++++++++++++++")

    # print("====================")
    # print(test_case)


if __name__ == '__main__':
    with open('input/level3_5.in', 'r') as input_field, open('output/level3_5.out', 'w') as output_field:
        num = int(input_field.readline().split()[0])

        for _ in range(num):
            inp = input_field.readline()
            result = solve(inp.split())
            print(result, file=output_field)