import re
import sys

def conversor(file, output):
    with open(file, 'r') as f:
        lines = f.readlines()

    countL = False

    headers = re.compile(r'^(#+)\s*(.*)')
    bold = re.compile(r'(\*\*|__)(.*?)\1')
    italic = re.compile(r'(\*|_)(.*?)\1')
    numerate = re.compile(r'^(\d+\.)\s(.*)')
    urlOrImage = re.compile(r'( |!)\[(.*?)\]\((.*?)\)')

    with open(output, 'w+') as f:
        f.write("<html>\n")
        f.write("<body>\n")

        for i, line in enumerate(lines):
            hM = headers.search(line)
            bM = bold.findall(line)
            iM = italic.findall(line)
            uIM = urlOrImage.search(line)
            nM = numerate.search(line)

            if hM:
                header_symbols = hM.group(1)
                title = hM.group(2)
                quantity = len(header_symbols)
                new_title = f'<h{quantity}>{title}</h{quantity}>'
                line = headers.sub(new_title, line)

            for bold_text in bM:
                line = line.replace(bold_text[0] + bold_text[1] + bold_text[0], f'<b>{bold_text[1]}</b>')

            for italic_text in iM:
                line = line.replace(italic_text[0] + italic_text[1] + italic_text[0], f'<i>{italic_text[1]}</i>')

            if uIM:
                option = uIM.group(1)
                text = uIM.group(2)
                link = uIM.group(3)

                if option == ' ':
                    new_link = f' <a href="{link}">{text}</a>'
                else:
                    new_link = f'<img src="{link}" alt="{text}"/>'
                line = urlOrImage.sub(new_link, line)

            if nM:
                text = nM.group(2)
                if not countL:
                    countL = True
                    new_numerate = f'<ol>\n<li>{text}</li>'
                else:
                    new_numerate = f'<li>{text}</li>'

                next_line = lines[i + 1] if i + 1 < len(lines) else ""
                if not numerate.match(next_line):
                    new_numerate = f'<li>{text}</li>\n</ol>'
                    countL = False
                line = numerate.sub(new_numerate, line)

            f.writelines(line)

        f.write("</body>\n")
        f.write("</html>")
    return 'output.html'

def main(args):
    if len(args) != 3:
        print('Usage: python conversor.py <input_file> <output_file>')
        return 1
    
    input_file = args[1]
    output_file = args[2]
    conversor(input_file, output_file)

    print(f'Done!')

if __name__ == '__main__':
    main(sys.argv)
