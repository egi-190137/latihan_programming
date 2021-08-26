def convert(st): 
    st = st.lower()
    digits = {}
    hasil = ""
    count = 1
    for i in range(len(st)):
        if st[i] not in digits.keys():
            hasil += str(count)
            digits[st[i]] = str(count)
            if count == 1:
                count = 0
            elif count == 0:
                count = 2
            else:
                count += 1
        else:
            hasil += digits[st[i]]
    return int(hasil) if hasil != "" else 0
