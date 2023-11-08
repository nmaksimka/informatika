string = input()
string_for = ''
string_reverse = ''
l = list()
#1
print(string[::-1])
#2
for i in string:
    string_for = i + string_for
print(string_for)
#3.1
print(string_reverse.join(reversed(string))) #я подумал что здесь одинаковая логика, просто разная вариация кода поэтому записал как 3,1 и 3,2
#3.2
for k in string:
    l.append(k)
l.reverse()
print(*l, sep = '')
#неудачная, хочу спросить как написать олгически этот код так чтобы он работал
#l.clear()
#for _ in range(len(string)):
#    l.append(string[-1])
#    string.removeprefix(string[-1])
#print(*l)
#4
n = len(string)
s = ''
l.clear()
while n > 0:
    s += string[n - 1]
    n -= 1
print(s)