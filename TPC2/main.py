import re
import json
import matplotlib.pyplot as plt
from tabulate import tabulate
from musicalWork import MusicalWork

def read_csv(path):
    data = list()
    dataD = dict()
    file = open(path, 'r', encoding='utf-8')
    content = file.read()
    adjusted = re.sub(r'\n\s+', ' ', content)
    file.close()
    data = adjusted.splitlines()
    data.pop(0)
    for line in data:
        pattern = r'(?:^|;)("(?:[^"]|"")*"|[^;]*)'
        match = re.findall(pattern, line)
        id = match[6]
        work = MusicalWork(match[0], match[1], match[2], match[3], match[4], match[5], id)
        dataD[id] = work
    return dataD

def composers(data):
    composers = list()
    for work in data.values():
        name = work.composer
        patternName = r'(\w+),\s+(.+)'
        nameS = re.search(patternName, name)
        if nameS:
            name = re.sub(patternName, r'\2 \1', name)
        composers.append(name)
    composers = sorted(set(composers))
    return composers

def distribution_per_period(data):
    periods = dict()
    for work in data.values():
        period = work.period
        title = work.title
        if period not in periods:
            periods[period] = set()
        periods[period].add(title)

    periods_with_count = {
        period: {'titles': sorted(titles), 'count': len(titles)} 
        for period, titles in sorted(periods.items())
    }
    return periods_with_count

def save_to_json(data, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Dados salvos no arquivo {file_name}.")

def main():  
    csv_path = input("Path do ficheiro CSV:\n")
    data = read_csv(csv_path)
    question1 = None
    question23 = None
    print(len(data), "dados carregados e processados!")

    option = 0

    while option != 4:
        print("------------------------------------------")
        print("O que pretende visualizar?")
        print("1 - Lista dos compositores musicais (ordenados alfabeticamente)")
        print("2 - Distribuição das obras por período (quantas obras catalogadas)")
        print("3 - Dicionário com a lista alfabética dos títulos das obras por período")
        print("4 - Sair")
        print("------------------------------------------")

        option = int(input())

        match option:
            case 1:
                if question1 is None:
                    question1 = composers(data)
                print("------------------------------------------")
                print("1 - No terminal")
                print("2 - Num ficheiro xxx.json")
                print("------------------------------------------")
                show = int(input())

                match show:
                    case 1:
                        print("Exibindo no terminal...")
                        for i, nome in enumerate(question1, start=1):
                            print(f"{i}. {nome}")
                        print("Nota: Os compositores são apresentados de forma única, ou seja, mesmo que um compositor tenha várias obras, ele aparecerá apenas uma vez na lista.")
                    case 2:
                        print("Indique o nome que deseja dar ao ficheiro:")
                        file_name = input()
                        save_to_json(question1, file_name)
                    case _:
                        print("Opção inválida!")
            case 2:
                print("------------------------------------------")
                print("1 - Formato tabular")
                print("2 - Formato gráfico")
                print("------------------------------------------")
                format = int(input())
                if question23 is None:
                    question23 = distribution_per_period(data)

                match format:
                    case 1:
                        table_data = []
                        for period, titles in question23.items():
                            table_data.append([period, titles['count']])
                        headers = ['Período', 'Quantidade de Obras']
                        print(tabulate(table_data, headers=headers, tablefmt='pretty'))
                    case 2:
                        print("Formato gráfico selecionado.")
                        periods = list(question23.keys())
                        quantities = [titles['count'] for titles in question23.values()]
                        bars = plt.bar(periods, quantities, color='#ffd1dc')
                        for bar in bars:
                            yval = bar.get_height()
                            plt.text(bar.get_x() + bar.get_width() / 2, yval, str(yval), ha='center', va='bottom', fontsize=10)
                        plt.xticks(rotation=45, ha='right')
                        plt.title('Distribuição de Obras por Período')
                        plt.xlabel('Período')
                        plt.ylabel('Quantidade de Obras')
                        plt.tight_layout()
                        plt.show()
                    case _:
                        print("Opção inválida!")
            case 3:
                print("------------------------------------------")
                print("1 - No terminal")
                print("2 - Num ficheiro xxx.json")
                print("------------------------------------------")
                show = int(input())
                if question23 is None:
                    question23 = distribution_per_period(data)
                match show:
                    case 1:
                        for period, titles in question23.items():
                            print(f"{period}:", end=' ')
                            print(titles['count'])
                            for title in titles['titles']:
                                print(f"  - {title}")
                    case 2:
                        print("Indique o nome que deseja dar ao ficheiro:")
                        file_name = input()
                        save_to_json(question23, file_name)
                    case _:
                        print("Opção inválida!")
            case 4:
                print("Bye!")
            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()