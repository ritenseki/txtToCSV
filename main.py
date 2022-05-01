import pandas as pd

if __name__ == "__main__":
    filesource = 'FileSource/sample.txt'
    # print(filesource)
    with open(filesource, encoding='UTF-8') as file:
        name = file.name.rstrip('.txt')
        key = []
        text = []
        keys = name.lstrip('FileSource/')
        print(name)
        for line in file.readlines():
            line = line.strip()

            key.append(rf'key_{keys}')
            text.append(line)
        paragraph = {'keys(csv文件索引)': key, 'text(csv文件索引)': text}
        data = pd.DataFrame(paragraph)
        formatdata = data
        formatdata.to_csv(f'{name}.csv', index=False,)
