# coding = UTF-8
import os
import sys

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
            key.append(rf'{keys}_line{keynum}')
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
    print('txt 转 csv工具 for Paratranz, Copyright 2022 Ritenseki.')
    print('Ritenseki on Github: https://github.com/Ritenseki')
    # print('本工具免费提供。')
    print('开始转换？')
    inputting = input('[Y/n]')
    if inputting == 'Y':
        try:
            sourcedirs = os.listdir('.\FileSource')
        except FileNotFoundError as error:
            print('找不到FileSource目录，是否新建？')
            inp = input('[Y/n]')
            if inp == 'Y':
                os.makedirs('FileSource')
            else:
                sys.exit()

        else:
            for f in sourcedirs:
                if fnmatch.fnmatch(f, '*.txt'):
                    filesource = rf'.\FileSource/{f}'
                    print(filesource)
                    formatting()
        finally:
            sys.exit()
    else:
        sys.exit()
