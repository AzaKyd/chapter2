students = int(input("Insert studetns"))
apples = int(input("Insert apples"))
apples_each = apples // students
reamain_apples = apples % students 
print("Apples for every students " + str(apples_each) + " remaining apples " + str(reamain_apples))