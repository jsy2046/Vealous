#-*- coding: utf-8 -*-

from google.appengine.ext.webapp import template
from google.appengine.api import memcache

from config import gvars
from dbs import Vigo

template.register_template_library('filters')

def render(path, value):
    vigo = memcache.get('vigo')
    if vigo is None:
        vigo = {}
        vigo['sitename'] = Vigo.get('sitename')
        vigo['sitetag'] = Vigo.get('sitetag')
        vigo['twitter'] = Vigo.get('twitter')
        vigo['alterfeed'] = Vigo.get('alterfeed')
        vigo['meta'] = Vigo.get('meta')
        vigo['widget'] = Vigo.get('widget')
        memcache.set('vigo', vigo, 604800)
    conf = value.pop('conf',{})
    value['vigo'] = vigo
    if not conf:
        value['conf'] = gvars
    return template.render(path, value)
