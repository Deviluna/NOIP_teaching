from flask import Flask,render_template
import os
from pages import pages
# -- coding: utf-8 --

app=Flask(__name__)

@app.route("/")
def index():
    index_category=pages.pdfs_category()
    return render_template('index.html',category=index_category)

@app.route("/category/<cate>")
def category(cate):
	ret=""
	for item in os.listdir("pdfs/"+cate):
		if item=="ReadMe":
			continue
		ret+=item
	return ret

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)
