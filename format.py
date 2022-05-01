# coding = UTF-8
import pandas as pd

if __name__ == "__main__":
    filesource = r'.\FileSource/sample.txt'
    # print(filesource)
    with open(filesource, encoding='UTF-8') as file:
        name = file.name.rstrip('.txt')
        key = []
        text = []
        keys = name.lstrip(r'.\FileSource/')
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
