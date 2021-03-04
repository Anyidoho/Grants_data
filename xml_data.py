import glob
import pathlib
import requests,zipfile
from io import BytesIO
import multiprocessing as mp

root_path = pathlib.Path().absolute() / "xml_files"



def get_xml_data(year):
	url='https://www.nsf.gov/awardsearch/download?DownloadFileName='
	new_url=url+str(year)+'&All=true'
	r=requests.get(new_url)
	z=zipfile.ZipFile(BytesIO((r.content)))
	z.extractall(root_path)

get_xml_data(2020)
#a_pool = mp.Pool()
#a_pool.map(get_xml_data, range(2010, 2022))