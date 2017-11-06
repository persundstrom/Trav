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
#print data_filer

#number = data_filer[0]


for a in data_filer:
	
	datainfile = 'data' + a #number
	y_file = 'y_' + a + '.csv'

	print datainfile
	print y_file
	data_df = pd.read_csv(data_path + datainfile,sep=',',header=None)

#	print data_df.head()


	data_df[17].to_csv(data_path + y_file, index=False,header=None)
	data_df = data_df.drop(17,axis=1)
	data_df = data_df.drop(0,axis=1)	#horsename
	data_df = data_df.drop(1,axis=1)	#kon
	data_df = data_df.drop(3,axis=1)	#ras
	data_df = data_df.drop(22,axis=1)	#kusk
	data_df = data_df.drop(23,axis=1)	# tranare
	data_df = data_df.drop(12,axis=1)	#tid
	data_df = data_df.drop(7,axis=1)	#bana
	data_df = data_df.drop(8,axis=1)	#datum
	data_df[2] = 2017 - data_df[2]
	print data_df.head()
	data_df.to_csv(data_path + 'ny_' + datainfile, index=False,header=None)
	
