import time
from parallelFetcher import ParallelFetcher

__author__ = 'will'
import urllib2

import sys
from bs4 import BeautifulSoup


baseurl = "http://museudaimigracao.org.br/acervodigital/pesquisageral.php?id=nomes&busca="

class Pessoa():
    nome = None
    sobrenome = None
    chegada = None
    nacionalidade = None
    precedencia = None
    destino = None
    profissao = None
    idade = None
    sexo = None
    pdf = None
    more_info = None

    def getNascimento(self):
        try:
            nascimentoEstimado = int(self.chegada.split("/")[-1])- int(self.idade)
            return nascimentoEstimado
        except:
            return -1

    def matches(self,args):
        for arg in args:
            if arg not in self.nome.lower() and arg not in self.sobrenome.lower():
                return False
        return True

    def __repr__(self):
        return "nome: {0}, sobrenome: {1}, idade: {2}, chegado em:{3} no porto de {4} ".format(self.nome.encode('utf-8'),
                                                                self.sobrenome.encode('utf-8'),
                                                                self.idade.encode('utf-8'),
                                                                self.chegada.encode('utf-8'),
                                                                self.destino.encode('utf-8'),)



class EntryFinder():
    found = []

    def load_data(self, url):
        print "loading url", url
        response = urllib2.urlopen(url)
        html = response.read()
        return html


    def extract_people_data(self,entries):
        people = zip(*(iter(entries),) * 5)
        for person in people:

            firstRow = person[0].find_all('td')
            nome = firstRow[0].text.split(":")[1]
            sobrenome = firstRow[1].text.split(":")[1]
            chegada = firstRow[2].text.split(":")[1]
            pdf = firstRow[3].find('a')['href']#[0].get('href')

            secondRow = person[1].find_all('td')
            nacionalidade = secondRow[0].text.split(":")[1]
            precedencia = secondRow[1].text.split(":")[1]
            destino = secondRow[2].text.split(":")[1]
            more_info = secondRow[3].find('a')['href']

            thirdRow = person[2].find_all('td')
            profissao = thirdRow[0].text.split(":")[1]
            idade = thirdRow[1].text.split(":")[1]
            sexo = thirdRow[2].text.split(":")[1]

            newperson = Pessoa()
            newperson.nome = nome
            newperson.sobrenome = sobrenome
            newperson.chegada = chegada
            newperson.nacionalidade = nacionalidade
            newperson.precedencia = precedencia
            newperson.destino = destino
            newperson.profissao = profissao
            newperson.idade = idade
            newperson.sexo = sexo
            newperson.pdf = "http://museudaimigracao.org.br/acervodigital/" + pdf
            newperson.more_info = "http://museudaimigracao.org.br/acervodigital/" + more_info

            self.found.append(newperson)



    def get_processed_data(self,data):
        soup = BeautifulSoup(data)
        ammount = soup.find_all('a', {'href' : "?id=nomes&busca={0}".format(self.entries[0])})[0].text.split(" ")[0]
        ammount = int(ammount)
        contentTable = soup.find('table', {'width':'100%',
                                           'height':'300'})
        entries = contentTable.find_all('tr')
        self.extract_people_data(entries)
        return int(ammount)

    def load_urls(self,urls):
        fetcher = ParallelFetcher(urls,7)
        fetcher.start()
        while not fetcher.done:
            time.sleep(0.1)
        return fetcher.data

    def __init__(self, args):
        self.entries = [arg.upper() for arg in args]
        ammount = self.get_processed_data(self.load_data(baseurl+args[0]))
        print ammount
        urls = []
        time.sleep(5)
        for i in xrange(10,ammount,10):
            newurl = baseurl+args[0]+"&paginanome={0}".format(i)
            urls.append(newurl)

        datas = self.load_urls(urls)
        for url in urls:
            self.get_processed_data(datas[url])

        matches = []
        for pessoa in self.found:
            if pessoa.matches(args):
                matches.append(pessoa)

        for pessoa in matches:
            #if  1872 < pessoa.getNascimento()  < 1874:
                print pessoa
                print "nascido aprox em ", pessoa.getNascimento()
                print pessoa.more_info
                print pessoa.pdf


if __name__ == "__main__":
    EntryFinder(sys.argv[1:])
