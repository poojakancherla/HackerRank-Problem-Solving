def caesarCipherEncryptor(string, key):
    newLetters = []
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for ele in string:
        if alpha.index(ele)+key < 26:
            new_ele = alpha[alpha.index(ele)+key]
        else:
            new_ele = alpha[(alpha.index(ele)+key)%26]
        newLetters.append(new_ele)
    return "".join(newLetters)

print(caesarCipherEncryptor('abc', 57))
