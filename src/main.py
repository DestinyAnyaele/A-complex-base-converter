 # A full fledged base converter with all functionalities. just try it 😎
def base_converter(user_input) :
  import math
  try :
    initial_base = int(input('What base is the number : '))
    final_base = int(input('What base do you want to change it to : '))
  except ValueError as error:
    return error
  number = []
  for part in user_input.split('.') :
    number.append(part)
  try :
    if initial_base > 10 or final_base > 10 :
      raise Exception('This is not available yet please wait for upgrade by Anyaele Destiny Chinaemerem')
    else :
      if len(number) == 2 :   
        for searching in number[1] :
          if int(searching) > initial_base :
            raise Exception(f'{searching} is greater than the initial-base({initial_base})')
            break
  except Exception as message :
    return message
  try :
    def converting_10() :
      part_1 = int(number[0],initial_base)
      power = 1
      result = 0
      if len(number) == 2 :
        for digit in number[1] :
          part_2 = int(digit) / (initial_base ** power)
          power += 1
          result += part_2
      return part_1, result
    def converting_any() :
      remainders = []
      temporary = int(number[0])
      variable = True
      while variable :
        part_1 = temporary % final_base
        remainders.append(part_1)
        temporary = temporary // final_base
        if temporary < final_base :
          variable = False
      remainders.append(temporary)
      remainders.reverse()
      part_1 = ''.join(str(k) for k in remainders)
      part_1 = int(part_1)
      result = 0
      if len(number) == 2 :
        data = []
        part_2 = str(user_input).replace(str(number[0]),'0',1)
        for loop in range(4) :
          part_2 = float(part_2) * final_base
          value = math.trunc(part_2)
          data.append(value)
          part_2 = str(part_2).replace(str(value),'0',1)
        result = ''.join(str(w) for w in data)
        result = result.zfill(5)
        result = result.replace('0','0.',1)
        result = float(result)
      answer = part_1 + result
      return answer
    if final_base == 10 :
      part_1, result = converting_10()
      answer = part_1 + result
    elif initial_base == 10 :
      answer = converting_any()
    elif initial_base != 10 or final_base != 10 :
      a,b = converting_10()
      number = [a,b]
      user_input = a + b
      answer = converting_any()
  except Exception as error :
    return error
  else :
    return answer
Test = str(input('What is the number : '))
results = base_converter(Test)
print(results)
