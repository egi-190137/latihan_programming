def gabungKata(kata1, kata2, length):
    idx = 0
    while idx < len(kata1) - length + 1:
        if kata1[idx:length+idx] in kata2:
            break
        else:
            idx += 1
        
        if idx == len(kata1) - length + 1:
            length -= 1
            idx = 0
    
    idx2 = 0
    while idx < len(kata2) - length + 1:
        if kata1[idx:length+idx] == kata2[idx2:length+idx2]:
            break
        else:
            idx2 += 1
    
    return f'{kata1[:idx]}{kata1[idx:length+idx]}{kata2[length+idx2:]}'

kata1 = input()
kata2 = input()

if len(kata1) < len(kata2):
    print(len(gabungKata(kata1, kata2, len(kata1))))
else:
    print(len(gabungKata(kata1, kata2, len(kata2))))

    # idx = 0
    # while idx < len(kata1) - length + 1:
    #     if kata1[idx:length+idx] in kata2:
    #         break
    #     else:
    #         idx += 1
    
    # idx2 = 0
    # while idx < len(kata2) - length + 1:
    #     if kata1[idx:length+iidx] == kata2[idx2:length+idx2]:
    #         break
    #     else:
    #         idx2 += 1
    
    # print(f'{kata1[:idx]}{kata1[idx:length+idx]}{kata2[length+idx2-1:]}')