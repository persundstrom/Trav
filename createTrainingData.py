import pandas as pd
import gc
from os import listdir
from os.path import isfile, join

cnt = 0
data_filer = []

data_path = 'pandasdata/data/'


data_files = [d for d in listdir(data_path) if isfile(join(data_path, d))]

for i in data_files:
	if 'data' in i:
		data_filer.append(i[-2:])

data_filer.sort()


for a in data_filer:
	
	datainfile = 'ny_data' + a #number
	sexinfile = 'sex' + a #number
	datuminfile = 'datum' + a #number
	distansinfile = 'distans' + a #number
	kuskinfile = 'kusk' + a #number
	horsesinfile = 'horses' + a #number
	rasinfile = 'ras' + a #number
	trainerinfile = 'trainer' + a #number
	banainfile = 'bana' + a #number
#	yfile = 'y_' + a + '.csv'#number

	#print datainfile
	
	data_df = pd.read_csv(data_path + datainfile,sep=',',header=None,prefix='data')
	sex_df = pd.read_csv(data_path + sexinfile,sep=',',header=None,prefix='sex')
#	datum_df = pd.read_csv(data_path + datuminfile,sep=',',header=None,prefix='datum')
	distans_df = pd.read_csv(data_path + distansinfile,sep=',',header=None,prefix='distans')
#	kusk_df = pd.read_csv(data_path + kuskinfile,sep=',',header=None,prefix='kusk')
#	horses_df = pd.read_csv(data_path + horsesinfile,sep=',',header=None,prefix='horses')
	ras_df = pd.read_csv(data_path + rasinfile,sep=',',header=None,prefix='ras')
#	trainer_df = pd.read_csv(data_path + trainerinfile,sep=',',header=None,prefix='trainer')
	bana_df = pd.read_csv(data_path + banainfile,sep=',',header=None,prefix='bana')
#	y_df = pd.read_csv(data_path + yfile,sep=',',header=None,prefix='y')

#	print data_df.head()
	data_df = data_df.join(sex_df)
#	data_df = data_df.join(datum_df)
	data_df = data_df.join(distans_df)
#	data_df = data_df.join(kusk_df)
#	data_df = data_df.join(horses_df)
	data_df = data_df.join(ras_df)
#	data_df = data_df.join(trainer_df)
	data_df = data_df.join(bana_df)
#	data_df = data_df.join(y_df)

	#print data_df.head()
#	print data_df.num_columns
	data_df.to_csv(data_path + 'keras_' + datainfile, index=False,header=None)

