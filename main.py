import pandas as pd

if __name__ == "__main__":
    with open(r'Inputs/sample.txt') as file:
        name = file.name
        countline = 0
        for line in file.readlines():
            print(line)
            line = line.strip()
            paragraph = []
            paragraph.append(line)
            paragraph[countline] = line

            countline = countline + 1

        data = pd.DataFrame(paragraph)
        formatdata = data
        # print(formatdata)
        formatdata.to_csv(f'{name}.csv', index=False,)
