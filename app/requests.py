import urllib.request,json
from .models import Sources,Articles
from datetime import datetime

#getting the api key
api_key = None

#getting the news base url
base_url = None

#getting the articlces url
articles_url = None

def configure_request(app):
	global api_key,base_url,articles_url
	api_key = app.config['NEWS_API_KEY']
	base_url = app.config['NEWS_SOURCES_BASE_URL']
	articles_url = app.config['ARTICLES_BASE_URL']
