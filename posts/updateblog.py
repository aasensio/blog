import glob
import os
import datetime

notebooks = glob.glob("/scratch/Dropbox/ipyNotebook/*.ipynb")

for notebook in notebooks:
	name = notebook.split("/")[-1].split('.')[0]
	date = datetime.datetime.fromtimestamp(os.path.getmtime(notebook))
	f = open("/scratch/Dropbox/myblog/posts/{0}.meta".format(name), "w")
	f.write(".. title: {0}\n".format(name))
	f.write(".. slug: {0}\n".format(name))
	f.write(".. date: {0}\n".format(date))
	f.write(".. tags: work, python\n")
	f.write(".. link: \n")
	f.write(".. description: {0}\n".format(name))
	f.write(".. type: text\n")
	f.close()