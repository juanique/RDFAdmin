import settings
from rdf import TripleStore, SparqlProxy

def get_triple_store():
   host = settings.VIRTUOSO_HOST
   if host[:4] != 'http':
       host = "http://%s" % host
   return TripleStore(host, settings.VIRTUOSO_USER, settings.VIRTUOSO_PASS, settings.VIRTUOSO_WORK_DIR)

def get_sparql_proxy():
    return SparqlProxy(settings.VIRTUOSO_ENDPOINT)
