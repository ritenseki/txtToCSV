import os
import sys
import pandas as pd
import fnmatch

if __name__ == "__main__":
    print('csv 导出为 txt工具 for Paratranz, Copyright 2022 ritenseki.')
    print('ritenseki on Github: https://github.com/ritenseki')
    # print('本工具免费提供。')
    print('开始转换？')
    inputting = input('[Y/n]')
    if inputting == 'Y':
        try:
            sourcedirs = os.listdir('.\Translated')
        except FileNotFoundError as error:
            print('找不到Translated目录，是否新建？')
            inp = input('[Y/n]')
            if inp == 'Y':
                os.makedirs('Translated')
            else:
                i = input("按任意键继续")
                sys.exit()

        else:
            for f in sourcedirs:
                if fnmatch.fnmatch(f, '*.csv'):
                    filesource = rf'.\Translated/{f}'
                    # print(filesource)
                    filen = filesource.rstrip('.csv')
                    filenam = filen.lstrip(f'{filesource}')
                    filename = f'{filen}.txt'
                    file = open(filename, encoding='UTF-8', mode='w')
                    dataframe = pd.DataFrame.dropna(pd.read_csv(f'{filesource}', usecols=[1], engine='python'))
                    # print(dataframe.values)
                    for line in (dataframe.values):
                        for text in line:
                            text = str(text)
                            # print(text)
                            file.write(text)
                            file.write('\n')
                    print('Done!')
                    file.close()
        finally:
            inppput = input("按任意键继续")
            sys.exit()
