def designerPdfViewer(h, word):
    maxHeight = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for ch in word:
        if h[alpha.index(ch)] > maxHeight:
            maxHeight = h[alpha.index(ch)]
    
    return maxHeight * len(word)

if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)