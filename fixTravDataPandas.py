# -*- coding: utf-8  -*-

import pandas as pd
import sys
from sklearn.utils import shuffle

df = pd.read_csv('out_file4',sep='\t',header=0)
#df = pd.read_csv('data.csv',sep=',',header=0)
#df = pd.read_csv('dummies/data.csv',sep=',')

#df = shuffle(df)


#print len(list(df.columns.values))

#sex_horse = pd.get_dummies(df['sex'])
#df = df.append(sex_horse)
#print len(list(df.columns.values))

#distansbonus = pd.get_dummies(df['distansbonus'])
#df = df.append(distansbonus)
#print len(list(df.columns.values))

#ras_horse = pd.get_dummies(df['ras'])
#df = df.append(ras_horse)
#print len(list(df.columns.values))

#bana = pd.get_dummies(df['bana'])
#df = df.append(bana)
#print len(list(df.columns.values))

dum_horse = pd.get_dummies(df['horsename'])
#df = df.append(dum_horse)
#print len(list(df.columns.values))


kusk = pd.get_dummies(df['kusk'])
#df = df.append(kusk)
#print len(list(df.columns.values))

trainer = pd.get_dummies(df['trainer'])
#df = df.append(trainer)
#print len(list(df.columns.values))

datum = pd.get_dummies(df['datum'])
#df = df.append(datum)
#print len(list(df.columns.values))

#sex_horse = sex_horse.drop('sex',1).head()
#distansbonus = distansbonus.drop('distansbonus',1).head()
#ras_horse = ras_horse.drop('ras',1).head()
#bana = bana.drop('bana',1).head()
dum_horse = dum_horse.drop('horsename',1).head()
kusk = kusk.drop('kusk',1).head()
trainer = trainer.drop('trainer',1).head()
datum = datum.drop('datum',1).head()


#print df.head()
#print trainer
#df.to_csv('data.csv', index=False)#,header=None)
#sex_horse.to_csv('dummies/sex_horse.csv', index=False)
#distansbonus.to_csv('dummies/distansbonus.csv', index=False)
#ras_horse.to_csv('dummies/ras_horse.csv', index=False)
#bana.to_csv('dummies/bana.csv', index=False)
dum_horse.to_csv('dummies/dum_horse.csv', index=False)
trainer.to_csv('dummies/trainer.csv', index=False)
kusk.to_csv('dummies/kusk.csv', index=False)
datum.to_csv('dummies/datum.csv', index=False)
