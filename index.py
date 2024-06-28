import cProfile
import pstats
import io
import bottle
from bottle import route, run, template
import image
from memory_profiler import profile

@profile
def call_service():
    directoryName = 'photos'
    image.process(directoryName)

def profile_service():
    pr = cProfile.Profile()
    pr.enable()
    call_service()
    pr.disable()

    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())

@route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    profile_service()
    return template('index.tpl', data="Request completed!", title=title)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8000, debug=True, reloader=True)

app = bottle.default_app()