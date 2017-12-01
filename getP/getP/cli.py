import click
import requests
from PIL import Image
from StringIO import StringIO
from bs4 import BeautifulSoup

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='pompham_sb', required=False)
def main(name, as_cowboy):
    	"""Get Photo Instagram"""
    	#greet = 'Howdy' if as_cowboy else 'Hello'
    	#click.echo('{0}, {1}.'.format(greet, name))
	url="http://picbear.com/{}".format(name)
	html=requests.get(url)
	beau=BeautifulSoup(html.content,'html.parser')
	photo = beau.find_all('img',{'class':'p-avatar'})[0]['src']
	req=requests.get(photo)
	img=Image.open(StringIO(req.content))
	img.show()
