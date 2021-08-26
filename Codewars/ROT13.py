def rot13(message):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    hasil = ''
    for i in range(len(message)):
        if message[i].lower() in alpha:
            if message[i-1] == '\\' and message[i] == 'n':
                hasil += message[i]
            else:
                index = alpha.index(message[i].lower()) + 13
                if index >= len(alpha):
                    index = index - len(alpha)

                hasil += alpha[index].upper() if message[i].isupper() else alpha[index]
        else:
            hasil += message[i]
    
    return hasil







# print(rot13("EBG13 rknzcyr."), "ROT13 example.")
print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.") + "\n"+ "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
# print(rot13("123"), "123")
# print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"), "This is actually the first kata I ever made. Thanks for finishing it! :)")
# print(rot13("@[`{"), "@[`{")