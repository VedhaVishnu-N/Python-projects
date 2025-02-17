print("-------------------Welcome-------------------")

qn_format=int(input("enter the format your temperature is in\n1.Farenheit 2.kelvin 3.celsius\noption:"))
qn_temp=float(input("Enter the temperature you want to convert:"))
ans_format=int(input("enter the format you want to change your temperature into \n1.Farenheit 2.kelvin 3.celsius\noption:"))
ans_temp=0

if qn_format==ans_format:
    print("both question format and answer format is same")
    ans_temp=qn_temp
elif qn_format==1:
    if ans_format==2:
        ans_temp=(qn_temp-32)*(5/9)+273.15
    if ans_format==3:
        ans_temp=(qn_temp-32)*(5/9)
elif qn_format==2:
     if ans_format==1:
        ans_temp=qn_format*(9/5)+32
     if ans_format==3:
        ans_temp=qn_temp+273.15
elif qn_format==3:
    if ans_format==1:
        ans_temp=qn_temp-273.15
    if ans_format==2:
      ans_temp=(qn_temp-273.15)*(9/5)+32

print(f"the answer for the conversion is {ans_temp :.4f}")  
      
