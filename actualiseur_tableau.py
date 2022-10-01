# coding: utf-8

import pandas as pd
import numpy as np
import os
import sys
import codecs
import jinja2

dir_path=os.path.dirname(os.path.abspath(__file__))
#os.chdir(dname)

fsloader = jinja2.FileSystemLoader(dir_path) #dossier ou se trouve les template
env = jinja2.Environment(loader=fsloader)

df = pd.read_excel("OnPeutMangerOu.xlsx")
df = df.replace(np.nan, "", regex=True)

template = env.get_template('jaifaim.html.j2') #nomdutemplate
ofh = codecs.open("jaifaim.html","w", encoding="utf-8")
rt = template.render(column_names=df.columns.values, row_data=list(df.values.tolist())  , zip=zip)
ofh.write(rt)
ofh.close()
