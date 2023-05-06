s = input()

output = []
for ch in s:
    if output == [] or int(ch) != output[-1][1]:
        output.append([1, int(ch)])
    elif int(ch) == output[-1][1]:
        output[-1][0] += 1

for item in output:         
    print(f"({item[0]}, {item[1]})", end=" ")