# coding = UTF-8
import os
import sys
import datetime

if __name__ == "__main__":
    print('txt 聚合工具 for Paratranz, Copyright 2022 ritenseki.')
    print('ritenseki on Github: https://github.com/ritenseki')
    # print('本工具免费提供。')
    print('开始转换？')
    inputting = input('[Y/n]')
    if inputting == 'Y':
        try:
            sourcedirs = os.listdir('.\OriginalFile')
        except FileNotFoundError as error:
            print('找不到OriginalFile目录，是否新建？')
            inp = input('[Y/n]')
            if inp == 'Y':
                os.makedirs('OriginalFile')
            else:
                sys.exit()

        else:
            date = datetime.date.today()
            with open(rf".\FileSource\{date}.txt", encoding="UTF-8", mode="w") as final:
                for each in sourcedirs:
                    with open(rf".\OriginalFile\{each}", encoding="UTF-8") as f:
                        # print(f.readlines())
                        for fline in f.readlines():
                            finalline= fline.rstrip("\n")
                            final.write(finalline)
                            final.write(" ")
                        final.write("\n")
                print('Done!')
        finally:
            i = input("按任意键继续")
            sys.exit()
    else:
        i = input("按任意键继续")
        sys.exit()
