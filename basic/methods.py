from str import TXT_INVALID_OPERATION, TXT_KEEP, TXT_OPERATION, TXT_VALUE1,TXT_VALUE2,SOMAR,MULTIPLICAR,DIVIDIR,SUBTRAIR
from str import TXT_INVALID_OPERATION


def sum(val1,val2):
    if(val1.isnumeric):
        return"digite um valor numerico"
    result = float(val1) + float(val2)
    return str(result)

def multiply(val1,val2):
    result = float(val1) * float(val2)
    return str(result)

def subtract (val1,val2):
    result = float(val1) - float(val2)
    return str(result)

def divide (val1,val2):
    if (val1 == "0" or val2 == "0"):
        return TXT_INVALID_OPERATION
    
    result = float(val1) / float(val2)
    return str(result)

def identify_operation(operation,val1,val2):
  if (operation  == SOMAR):
        return sum(val1,val2)
  if (operation  == SUBTRAIR):
        return subtract(val1,val2)
  if (operation  == MULTIPLICAR):
        return multiply(val1,val2)
  if (operation  == DIVIDIR):
    return divide(val1,val2)
  return TXT_INVALID_OPERATION

def calc():
  operation= input(TXT_OPERATION)
  value1= input(TXT_VALUE1)
  value2= input(TXT_VALUE2)
  result=identify_operation(operation,value1,value2)
  print(result)
  keep=input(TXT_KEEP)
  if (keep=="S"):
    calc()
