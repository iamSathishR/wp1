import flask

from wp1.wp10_db import connect as wp10_connect
from wp1.wiki_db import connect as wiki_connect

DB_CONNECT = {
    'wp10db': wp10_connect,
    'wikidb': wiki_connect,
}


def has_db(name):
  return hasattr(flask.g, name)


def get_db(name):
  if not has_db(name):
    setattr(flask.g, name, DB_CONNECT[name]())
  return getattr(flask.g, name)
