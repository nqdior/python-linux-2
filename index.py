from gevent import monkey
monkey.patch_all()

import bottle
from bottle import route, run, template
import json
import image
import gevent

def call_service():
    directoryName = 'photos'
    image.process(directoryName)

def async_call_service():
     gevent.spawn(call_service)

@route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    async_call_service()  # 非同期で呼び出し
    return template('index.tpl', data="Request submitted!", title=title)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000, debug=True, reloader=True, server='gevent')
    
app = bottle.default_app()