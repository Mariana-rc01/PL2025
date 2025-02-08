def main():
    sum = 0
    state = True
    numberS = ""

    line = input("> ")

    while (line != ""):
        line = line.lower() + '\n'
        for index, char in enumerate(line):
            if state:
                if char.isdigit():
                    numberS += char
                else:
                    if char == 'o' and line[index: index + 3] == "off":
                        state = False
                    
                    if len(numberS) > 0:
                        sum += int(numberS)
                        numberS = ""
            else:
                if char == 'o' and line[index: index + 2] == "on":
                    state = True

            if char == '=':
                print("Soma = ", sum, '\n')

        line = input("> ")

if __name__ == '__main__':
    main()
