def gordon(a):
    hasil = ""
    for ch in a:
        if ch.lower() == "a":
            hasil += "@"
        elif ch.lower() in 'aiueo':
            hasil += "*"
        elif ch == " ":
            hasil += "!!!! "
        else:
            hasil += ch.upper()
    hasil += "!!!!"

    return hasil

print(gordon('What feck damn cake') + "\n" + 'WH@T!!!! F*CK!!!! D@MN!!!! C@K*!!!!')