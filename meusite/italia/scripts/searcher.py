from StringIO import StringIO
import threading
import os, errno
import zipfile
import sys
import urllib2
import json
from Queue import Queue
import time
from lxml import etree
## url style =
"""https://familysearch.org/pal:/MM9.3.1/TH-266-12657-9427-10"""
"""https://familysearch.org/pal:/MM9.3.1/TH-267-11845-83978-98"""
"""https://familysearch.org/pal:/MM9.3.1/TH-1942-27455-5120-90"""


#download urls
"""https://familysearch.org/pal:/MM9.3.1/TH-1942-27455-5120-90.jpg?ctx=CrxCtxPublicAccess&header=Content-Disposition&headerValue=attachment%3B%20filename%3Drecord-image.jpg"""


download_ender = ".jpg?ctx=CrxCtxPublicAccess&header=Content-Disposition&headerValue=attachment%3B%20filename%3Drecord-image.jpg"

class DownloadThread(threading.Thread):

    def __init__(self, name, parent,id, stop):
        super(DownloadThread, self).__init__()
        self.running = True
        self.name = name
        self.parent = parent
        self.id = id
        self.stop = stop

    def log(self, string):
        self.parent.log("Thread" + str(self.id)+":" + string)

    def run(self):

        self.log("started download thread {0} <br>".format(self.name))
        while not self.stop.is_set() or not self.parent.download_links.empty():
            print "running"
            url,counter = self.parent.download_links.get()
            # print self.name
            self.log("downloading file nr. " + str(counter)+" of " + str(self.parent.count) + " from " + url + "<br>")
            try:
                with open('downloaded/{0}/{0}{1}.jpg'.format(self.name, counter), 'wb') as file:
                    file.write(urllib2.urlopen(url).read())
            except:
                self.log("Errordownload file," + str(counter))
            self.log("file nr. " + str(counter) + " done.<br>")
            time.sleep(1)

        self.log("leaving thread<br>")
        print "thread done!"

class Downloader(threading.Thread):

    download_links = Queue()
    name = "default_name"
    count = None
    running = True
    done = True

    def __init__(self, search_object):
        super(Downloader, self).__init__()
        self.name = search_object.filename
        self.url = search_object.url
        self.search_object = search_object

    def log(self, string):
        self.search_object.log += str(string) + "\n"
        print string
        self.search_object.save()

    def mkdir_p(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    def compressfile(self, name):
        simonsZip = zipfile.ZipFile("downloaded/{0}.zip".format(name), "w")
        dir = os.path.join(os.path.curdir, "downloaded", name)
        # print dir
        for dirname, subdirs, files in os.walk(dir):
            simonsZip.write(dirname)
            for filename in files:
                simonsZip.write(os.path.join(dirname,filename))
        simonsZip.close()

    def run(self):
        curdir = os.path.curdir

        if os.path.isdir(os.path.join(curdir,"downloaded", self.name)):
            self.log("doing nothing, already downloaded, get file <a href='/file/{0}.zip'> here</a><br>".format(self.name))
            time.sleep(5)
            exit()
        else:
            self.mkdir_p(os.path.join(curdir, "downloaded", self.name))
            self.log("Starting job with name " + self.name + " from path " + self.url + "<br>")
        threads = []
        self.done = False
        self.stops = []
        for i in range(1):
            stop = threading.Event()
            self.stops.append(stop)
            t = DownloadThread(self.name, self,i,stop)
            t.start()
            threads.append(t)
        site = self.url
        if "?" in site:
            site = site.split("?")[0]

        url = site
        counter = 0
        while self.running:
            counter += 1
            self.download_links.put((url+download_ender, counter))
            data = self.load_data(url)
            next = self.extract_next_image_url(data)
            if next:
                # print next
                self.log("new url: " + next + "<br>")
                url = next
            else:
                self.log("finished fetching urls <br>")
                self.run = False
                break

        self.log("waiting for threads to end <br>")
        for stop in self.stops:
            stop.set()
        for thread in threads:
            thread.join()

        time.sleep(1)
        self.log("threads finished<br>")
        self.done = True
        self.compressfile(self.name)
        self.log("compression done <br>")
        self.log("get file <a href='/file/{0}.zip'> here</a><br>".format(self.name))
        self.log("execution finished.")
        self.search_object.done = True
        self.search_object.save()

        # for thread in threads:
        #     thread.join()
        #     # thread.join()


    def load_data(self, url):
        response = urllib2.urlopen(url)
        html = response.read()
        with open("debug.html", "w") as file:
            file.write(html)
        return html

    def extract_next_image_url(self, data):
        parser = etree.HTMLParser()
        scripts = etree.parse(StringIO(data), parser).findall('.//script')

        for script in scripts:
            if "var imageMeta" in unicode(script.text):
                jsondata = script.text.split("eval(")[1].split("var collectionStats")[0][:-5]

                data = json.loads(jsondata)
                properties = data["properties"]
                next = None
                for entry in properties:
                    if "next" in entry["type"]:
                        next = entry["value"]
                    elif "count" in entry["type"]:
                        self.count = entry["value"]
                if next:
                    return next.split("?")[0]

        print "end of files?"
        return None

if __name__ == "__main__":
    a =Downloader(sys.argv[1], sys.argv[2])
    a.start()