import os
import pickle

def pdfs_category():
	ret={}
	base_path="pdfs/"
	for folder in os.listdir(base_path):
		ReadMe_path=base_path+folder+"/ReadMe"
		file=open(ReadMe_path,"r")
		text=file.read()
		info=eval(text)
		ret[folder]=info
	return ret