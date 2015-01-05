import logging
from flask import Flask
from pyelasticsearch import ElasticSearch

from noodles import default_settings

logging.basicConfig(level=logging.DEBUG)

# specific loggers
logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('pyelasticsearch').setLevel(logging.WARNING)


app = Flask(__name__)
app.config.from_object(default_settings)
app.config.from_envvar('NOODLES_SETTINGS', silent=True)

es = ElasticSearch(app.config.get('ELASTICSEARCH_URL'))
es_index = app.config.get('ELASTICSEARCH_INDEX')
