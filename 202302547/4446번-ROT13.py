import sys

while True:
    str = list(sys.stdin.readline())
    
    if not str:
        break
    else:
        try:

            consonant = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
            consonant_up = ['B', 'K', 'X', 'Z', 'N', 'H', 'D', 'C', 'W', 'G', 'P', 'V', 'J', 'Q', 'T', 'S', 'R', 'L', 'M', 'F']
            vowel = ['a', 'i', 'y', 'e', 'o', 'u']
            vowel_up = ['A', 'I', 'Y', 'E', 'O', 'U']

            for i in range(len(str)):
                if str[i] in consonant:
                    str[i] = consonant[(consonant.index(str[i])+10)%20]
                elif str[i] in consonant_up:
                    str[i] = consonant_up[(consonant_up.index(str[i])+10)%20]
                elif str[i] in vowel:
                    str[i] = vowel[(vowel.index(str[i])+3)%6]
                elif str[i] in vowel_up:
                    str[i] = vowel_up[(vowel_up.index(str[i])+3)%6]
                else:
                    continue
                    
            print(''.join(str), end='')
        except:
            break
        
