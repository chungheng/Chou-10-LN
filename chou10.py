"""
Convert local neuron data in antennal lobe of fruit fly into Pandas object.

The raw data is published in [1] by Luo's Lab at Stanford university, which can
be accessed at,

http://web.stanford.edu/group/luolab/Publications.shtml

[1] Chou YH, Spletter ML, Yaksi E, Leong JC, Wilson RI, Luo L, "Diversity and
    wiring variability of olfactory local interneurons in the Drosophila
    antennal lobe." Nature Neuroscience. 13(4):439-49. Epub 2010 Feb 7.
"""

import pandas as pd
import os.path
import urllib

filename = "Chou_Spletter_Yaksi_et_al_NN_2010_TabS2.xls"
url = "http://web.stanford.edu/group/luolab/Pdfs/" + filename


def chou10(filepath=None):
	filepath = filepath or filename
	if not os.path.isfile(filepath):
		urllib.urlretrieve (url, filename)
	xlsx = pd.ExcelFile(filename)
	df = xlsx.parse('Sheet1', skiprows=1, index_col=0)
	return df

