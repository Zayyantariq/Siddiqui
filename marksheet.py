print("=============================== MARK SHEET ===============================")
print("")

sname = input ("======================Enter Student Name:  ")
print("")
mmark = int (input ("======================Enter Maths Marks:  "))
print("")
umark = int (input ("======================Enter Urdu Marks:  "))
print("")
emark = int (input ("======================Enter English Marks: "))
print("")
total = mmark + umark + emark
print("")
per = (total * 100) / 300
print("======================Total Marks Obtain:  ",total)
print("")
print("======================Percentage: ",per,"% ")
print("")
if mmark<=40 or umark<=40 or emark<=40:
    print("======================Grade: Fail")
elif per>=90:
    print("======================Grade: A+")
elif per>=80:
    print("======================Grade: A ")
elif per>=70:
    print("======================Grade: B ")
elif per>=60:
    print("======================Grade: C ")
elif per>=50:
    print("======================Grade: D ")
else:
    print("======================Grade: Fail")
print("===========================================================================")    
