import pandas as pd
import os
import shutil




#def formatfile(filename):
    #paragraph = file.readlines()

    #return 0


if __name__ = "__main__" :
    with open(r'Inputs/(*).txt') as file:
        name = file.name
        #formatfile(name)
        formatdata = pd.DataFrame([file.readlines()])
        formatdata.to_csv(f'Outputs/{name}', index= False, columns= None )




