__author__ = 'will'

from flask import Flask
import searcher

app = Flask(__name__)

working = False

searcher1 = None

@app.route("/")
def hello():
    if not searcher1 or searcher1.done:
        return "nothin running<br> Use url as 'http://galvanicloop.com:5001/load/<FILENAME>/<URL>'"
    else:
        return searcher1.log

@app.route('/load/<name>/<path:path>')
def load_images(name,path):
    global searcher1
    if name == "default_name":
        return "bugou"
    # show the user profile for that user
    if not searcher1 or searcher1.name != name:
        searcher1 = searcher.Downloader(name, path)
        searcher1.start()
        return "starting downloading with name:" + name + " from path " + path + "<br>" + searcher1.log
    elif searcher1.name == name:
        return searcher1.log

if __name__ == "__main__":
    app.run(debug=True)


