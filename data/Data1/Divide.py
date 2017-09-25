name = input("Enter file.\n")
fp = open(name,'r');
res1 = name[0:-4] + "train.txt"
res2 = name[0:-4] + "test.txt"
fout1 = open(res1,'w')
fout2 = open(res2,'w')
i = 0
x= []
y = []
for line in fp:
	m,n = line.split()
	x.append(m)
	y.append(n)
r = (int)(3*(len(x))/4)
print(r)
j = 0
for j in range (r):
	fout1.write(x[j])
	fout1.write(" ")
	fout1.write(y[j])
	fout1.write("\n")
j += 1
print(j)
for k in range (j,len(x)):
	fout2.write(x[k])
	fout2.write(" ")
	fout2.write(y[k])
	fout2.write("\n")
fp.close()
fout1.close()
fout2.close()
# for i in range 
# print(len(x))
