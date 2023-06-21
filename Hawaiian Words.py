def validWord(word):
    x = True
    val_chr1 = ['a', 'e', 'i', 'o', 'u', 'p', 'k', 'h', 'l', 'm', 'n', 'w', ' ', '\'', ',', '.']
    val_chr2 = ['a', 'e', 'i', 'o', 'u', 'p', 'k', 'h', 'l', 'm', 'n', 'w', ' ', '\'', ',']
    if word[0] == '.' or word[-1] == '.':
        for char in word.lower():
            if char not in val_chr1:
                x = False
    else:
        for char in word.lower():
            if char not in val_chr2:
                x = False
    return x


def pronunciate(phrase):
    pronounce = ''
    i = 0
    while i < len(phrase):
        if phrase.lower()[i] == 'p':
            pronounce += 'p'
            i += 1
        elif phrase.lower()[i] == 'k':
            pronounce += 'k'
            i += 1
        elif phrase.lower()[i] == 'h':
            pronounce += 'h'
            i += 1
        elif phrase.lower()[i] == 'l':
            pronounce += 'l'
            i += 1
        elif phrase.lower()[i] == 'm':
            pronounce += 'm'
            i += 1
        elif phrase.lower()[i] == 'n':
            pronounce += 'n'
            i += 1
        elif phrase.lower()[i] == 'w':
            if phrase.lower()[i] == 'ww':
                pronounce += 'w'
                i += 1
            elif phrase.lower()[i - 1] == 'i' or phrase.lower()[i - 1] == 'e':
                pronounce += 'v'
                i += 1
            else:
                pronounce += 'w'
                i += 1
        elif phrase[i] == ' ':
            pronounce += ' '
            i += 1
        elif phrase[i] == '\'':
            pronounce += '\''
            i += 1
        elif phrase[i] == '.':
            pronounce += '.'
            i += 1
        elif phrase[i] == ',':
            pronounce += ','
            i += 1
        elif phrase.lower()[i] == 'a':
            if i == len(phrase) - 1:
                pronounce += 'ah'
                i += 1
            elif i + 1 == len(phrase) - 1 or phrase[i + 2] == ' ' or phrase.lower()[i + 1] == ' ' or phrase[i + 1] == '\'':
                if phrase.lower()[i + 1] == 'e' or phrase.lower()[i + 1] == 'i':
                    pronounce += 'eye'
                    i += 2
                elif phrase.lower()[i + 1] == 'o' or phrase.lower()[i + 1] == 'u':
                    pronounce += 'ow'
                    i += 2
                else:
                    pronounce += 'ah'
                    i += 1
            else:
                if phrase.lower()[i + 1] == 'e' or phrase.lower()[i + 1] == 'i':
                    if phrase[i + 2] == '\'' or phrase[i + 2] == ' ':
                        pronounce += 'eye'
                        i += 2
                    else:
                        pronounce += 'eye-'
                        i += 2
                elif phrase.lower()[i + 1] == 'o' or phrase.lower()[i + 1] == 'u':
                    if phrase[i + 2] == '\'' or phrase[i + 2] == ' ':
                        pronounce += 'ow'
                        i += 2
                    else:
                        pronounce += 'ow-'
                        i += 2
                else:
                    pronounce += 'ah-'
                    i += 1
        elif phrase.lower()[i] == 'e':
            if i == len(phrase) - 1:
                pronounce += 'eh'
                i += 1
            elif i + 1 == len(phrase) - 1 or phrase[i + 2] == ' ' or phrase[i + 1] == ' ' or phrase[i + 1] == '\'':
                if phrase.lower()[i + 1] == 'i':
                    pronounce += 'ay'
                    i += 2
                elif phrase.lower()[i + 1] == 'u':
                    pronounce += 'eh-oo'
                    i += 2
                else:
                    if phrase[i + 1] == ' ' or phrase[i + 1] == '\'':
                        pronounce += 'eh'
                        i += 1
                    else:
                        pronounce += 'eh-'
                        i += 1
            else:
                if phrase.lower()[i + 1] == 'i':
                    pronounce += 'eye-'
                    i += 2
                elif phrase.lower()[i + 1] == 'u':
                    pronounce += 'eh-oo-'
                    i += 2
                else:
                    pronounce += 'eh-'
                    i += 1
        elif phrase.lower()[i] == 'i':
            if i == len(phrase) - 1:
                pronounce += 'ee'
                i += 1
            elif i + 1 == len(phrase) - 1 or phrase[i + 2] == ' ' or phrase[i + 1] == ' ' or phrase[i + 1] == '\'':
                if phrase.lower()[i + 1] == 'u':
                    pronounce += 'ew'
                    i += 2
                else:
                    pronounce += 'ee'
                    i += 1
            else:
                if phrase.lower()[i + 1] == 'u':
                    pronounce += 'ew-'
                    i += 2
                else:
                    pronounce += 'ee-'
                    i += 1
        elif phrase.lower()[i] == 'o':
            if i == len(phrase) - 1:
                pronounce += 'oh'
                i += 1
            elif i + 1 == len(phrase) - 1 or phrase[i + 2] == ' ' or phrase[i + 1] == ' ' or phrase[i + 1] == '\'':
                if phrase.lower()[i + 1] == 'i':
                    pronounce += 'oy'
                    i += 2
                elif phrase.lower()[i + 1] == 'u':
                    pronounce += 'ow'
                    i += 2
                elif phrase.lower()[i + 1] == 'a':
                    pronounce += 'oh-'
                    i += 1
                else:
                    pronounce += 'oh'
                    i += 1
            else:
                if phrase.lower()[i + 1] == 'i':
                    if phrase[i + 2] == '\'' or phrase[i + 2] == ' ':
                        pronounce += 'oy'
                        i += 2
                    else:
                        pronounce += 'oy-'
                        i += 2
                elif phrase.lower()[i + 1] == 'u':
                    if phrase[i + 2] == '\'' or phrase[i + 2] == ' ':
                        pronounce += 'ow'
                        i += 2
                    else:
                        pronounce += 'ow-'
                        i += 2
                else:
                    pronounce += 'oh-'
                    i += 1
        elif phrase.lower()[i] == 'u':
            if i == len(phrase) - 1:
                pronounce += 'oo'
                i += 1
            elif i + 1 == len(phrase) - 1 or phrase[i + 2] == ' ' or phrase[i + 1] == ' ' or phrase[i + 1] == '\'':
                if phrase.lower()[i + 1] == 'i':
                    pronounce += 'ooey'
                    i += 2
                else:
                    pronounce += 'oo'
                    i += 1
            else:
                if phrase.lower()[i + 1] == 'i':
                    pronounce += 'ooey-'
                    i += 2
                else:
                    pronounce += 'oo-'
                    i += 1
    y = pronounce.split()
    for i in range(len(y)):
        y[i] = y[i].capitalize()
    y = ' '.join(y)
    if pronounce[-1] == ' ':
        y += ' '
    if pronounce[0] == ' ':
        y = ' ' + y
    return y


def createGuide(inputFile, outputFile):
    try:
        file = open(inputFile, 'r')
        data = file.readlines()
        z = ''
        for line in data:
            x = line.split()
            for word in x[:-1]:
                word = word.strip()
                if validWord(word):
                    z += (pronunciate(word))
                else:
                    z += '\"' + word + '\"'
                z += ' '

            if validWord(x[-1]):
                z += (pronunciate(x[-1]))
            else:
                z += '\"' + x[-1] + '\"'
            if line != data[-1]:
                z += '\n'
        file.close()

        with open(outputFile, 'w') as f:
            f.write(z)
    except:
        print('inputFile does not exist.')
