fr=open("number","r")
fw=open("numberOut","w")
data=fr.read().split("\n")

for i in (data):
    fw.write("\""+i+"\",")

count=0

#fw.write(data.replace(".",""))
'''for i in data:
    if(i.find("One hundred ") !=-1 or i.find("ten ") !=-1):
        #print count
        count+=1
    else:
        d=i.find("one ")
        i=i.replace(i[0:d+4],"")
        fw.write(i+"\n")'''




fr=open("a","r")
data=fr.read().split("\n")
'''
for i in data:
    i = i.replace("-On", "-on")
    i = i.replace("-Tw", "-tw")
    i = i.replace("-Th", "-th")
    i = i.replace("-Fo", "-fo")
    i = i.replace("-Fi", "-fi")
    i = i.replace("-Si", "-si")
    i = i.replace("-Se", "-se")
    i = i.replace("-Ei", "-ei")
    i = i.replace("-Ni", "-ni")

    fw.write(i[0:2]+" "+i[2:] + "\n")'''

for j in range(0,99):
        print "0"+`(j + 1)` + data[j][2:]

for i in range(0,9):
    for j in range(0,99):
        if j<9:
            print "" + `(i+1)` +"0" +`(j + 1)` + " " + data[i][2:] + " Hundred " + data[j][2:]
        else:
            print "" + `(i + 1)` + `(j + 1)` + " " + data[i][2:] + " Hundred " + data[j][2:]

