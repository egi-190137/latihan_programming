# kata = input()
def regex(kata):
    result = ""
    # Membuang baris pertama
    temp = kata.split("\n")
    for i in range(1, len(temp)):
        index = 0
        while index < len(temp[i]):
            if temp[i][index:index+4] == " && ":
                result += " and "
                index += 4
            elif temp[i][index:index+4] == " || ":
                result += " or "
                index += 4
            elif not (temp[i][index] == " " and index == len(temp[i]) - 1):
                result += temp[i][index] 
                index += 1
        result+="\n"

    return result

own = regex("""11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.""")
correct = """a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides."""
own = own.split("\n")
correct = correct.split("\n")
for i in range(len(own)):
    print(own[i]+"="+correct[i] + "|")
    print(own[i] == correct[i])
# regex("akndinsianincsbfibiafndnjNNX")