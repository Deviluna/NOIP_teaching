import pickle

def read_pkl_data(path):
	file=open(path,'rb'):
	data=pickle.read(file)
	file.close()
	return data

def write_pkl_data(data,path):
	file=open(path,'wb')
	pickle.dump(data,file)
	file.close()