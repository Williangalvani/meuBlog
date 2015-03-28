import time

__author__ = 'will'
import threading
from Queue import Queue
import urllib2

class Worker(threading.Thread):
    def __init__(self, parent):
        super(Worker, self).__init__()
        self.parent = parent
        self.running = True

    def run(self):
        while self.running:
            if self.parent.links.empty():
                self.running = False
                break
            else:
                url = self.parent.links.get()
                response = urllib2.urlopen(url)
                html = response.read()
                self.parent.add_result(url,html)
        print "done"

    def stop(self):
        self.running = False


class ParallelFetcher(threading.Thread):
    def __init__(self, links,N_THREADS=5):
        super(ParallelFetcher, self).__init__()
        self.links = Queue()
        for link in links:
            self.links.put(link)
        self.data = {}
        self.done = False
        self.N_THREADS = N_THREADS

    def run(self):
        threads =[]
        for i in range(self.N_THREADS):
            thread = Worker(self)
            thread.start()
            threads.append(thread)

        for thread in threads:
            # thread.stop()
            thread.join()
        self.done = True

    def add_result(self, url, data):
        self.data[url] = data
        print "downloaded pages:", len(self.data.keys())


asd = ["http://museudaimigracao.org.br/acervodigital/pesquisageral.php?id=nomes&busca=hermenegildo&paginanome=10",
       "http://museudaimigracao.org.br/acervodigital/pesquisageral.php?id=nomes&busca=hermenegildo&paginanome=20"]


if __name__ == "__main__":

    fetcher = ParallelFetcher(asd)
    fetcher.start()
    while not fetcher.done:
        time.sleep(0.1)
    print fetcher.data