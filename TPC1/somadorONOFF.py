import sys

def main():
    sum = 0
    state = True
    numberS = ""

    for line in sys.stdin:
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
                print(">> ", sum)
    print (">> ", sum)

if __name__ == '__main__':
    main()
