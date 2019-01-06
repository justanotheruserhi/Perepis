f = open('D:\Repository\Perepis.txt', 'r')

year = int(input('From'))
sec_year = int(input('To'))
count = 0

for i in f:
    gr = i.split()
    x = str(gr[3])
    y = int(x[-4:])
    if y<1978:
        print(gr[0])
        count = count + 1

print(count)

f.close()

f = open('D:\Repository\Perepis.txt', 'r')

for i in f:
    gr = i.split()
    x = str(gr[3])
    y = int(x[-4:])
    if year<y<sec_year:
        print(i)

f.close()