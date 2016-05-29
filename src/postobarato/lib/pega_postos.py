import sys
import requests
import pprint
import re

if __name__ == "__main__":

	fname = sys.argv[1]
	name = sys.argv[2]
	centerlat = sys.argv[3]
	centerlng = sys.argv[4]
	swlat = sys.argv[5]
	swlng = sys.argv[6]
	nelat = sys.argv[7]
	nelng = sys.argv[8]

	data_url = 'http://www.precodoscombustiveis.com.br/mapa/atualiza?swlat='+swlat+'&swlng='+swlng+'&nelat='+nelat+'&nelng='+nelng+'&zoom=13'
	r = requests.get(data_url)
	
	text = r.text
	text = text.replace('null', '\"\"')
	text = re.sub(r'"\d+":', "\n", text)
	text = text[1:len(text)-1]

	f = open('database/postos/'+fname, 'w')
	f.write('{\n')
	f.write('\t\"cidade\":\"'+name+'\",\n')
	f.write('\t\"centro\":{\n')
	f.write('\t\t\"lat\":'+centerlat+',\n')
	f.write('\t\t\"lng\":'+centerlng+'\n')
	f.write('\t},\n')
	f.write('\t\"postos\":[')

	lines = text.split('\n')
	for line in lines:
		f.write('\t\t'+line+'\n')

	f.write('\t]\n')
	f.write('}')

	f.close()
