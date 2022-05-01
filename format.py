# coding = UTF-8
import os

import pandas as pd
import fnmatch


def formatting():
    # filesource: str = rf'.\FileSource/sample.txt'
    with open(filesource, encoding='UTF-8') as file:
        name = file.name.rstrip('.txt')
        keys = name.lstrip(r'.\FileSource/')

        key = []
        text = []
        # print(name)
        # print(keys)
        keynum = 1
        for line in file.readlines():
            line = line.strip()
            key.append(rf'key_{keys}_line{keynum}')
            text.append(line)
            keynum = keynum + 1

        paragraph = {'keys(csv文件索引)': key, 'text(csv文件索引)': text}
        data = pd.DataFrame(paragraph)
        formatdata = data
        # print(data)
        formatdata.to_csv(f'{name}.csv', index=False)
        file.close()
    print('Formatting Done!')


if __name__ == "__main__":
    sourcedirs = os.listdir('.\FileSource')
    for f in sourcedirs:
        if fnmatch.fnmatch(f, '*.txt'):
            filesource = rf'.\FileSource/{f}'
            print(filesource)
            formatting()
