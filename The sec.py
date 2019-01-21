def grade(grade):
    f = open('D:\Repository\mat_dv.txt', 'r')
    Class = list()
    for i in f:
        lyric = i.split()
        cl = lyric[2]
        if int(cl) == grade:
            Class.append(i)
    f.close()
    return Class

def winner(source):
    All_points = list()
    count = len(source)
    for i in range(0, count-1):
        a = source[i]
        parts = a.split()
        points = int(parts[3]) + int(parts[4])
        All_points.append(points)
    winners_point = max(All_points)
    b = All_points.index(winners_point)
    winner = source[b]
    name = winner.split()
    print(name[0] + ' ' + name[1] + ' ' + str(winners_point))

Eight = list(grade(8))
Nine = list(grade(9))
Ten = list(grade(10))
Eleven = list(grade(11))

winner(Eight)
winner(Nine)
winner(Ten)
winner(Eleven)

f = open('D:\Repository\mat_dv.txt', 'r')
Everyone = list()
Algebra = list()
Geometry = list()
for i in f:
    Everyone.append(i)
    info = i.split()
    al = info[3]
    Algebra.append(al)
    ge = info[4]
    Geometry.append(ge)
f.close()

al_max = max(Algebra)
a = Algebra.index(al_max)
win_al = Everyone[a]
s_name = win_al.split()

ge_max = max(Geometry)
g = Geometry.index(ge_max)
win_ge = Everyone[g]
surname = win_ge.split()

print(s_name[0] + ' ' + s_name[1] + ' ' + s_name[2] + ' has won in algebra section')
print(surname[0] + ' ' + surname[1] + ' ' + surname[2] + ' has won in geometry section')