from threading import Thread
import platform
import requests
import time
import re
import os

pasta = os.getcwd()

arquivo_tocrawl = pasta + '/to_crawl.txt'
arquivo_crawled = pasta + '/crawled.txt'

if 'to_crawl.txt' and 'crawled.txt' not in os.listdir(pasta):
    c = 'https://compartilhe.info/listas/sites-inuteis-e-interessantes-para-gastar-tempo/\nhttps://falauniversidades.com.br/10-sites-bizarros-para-voce-passar-o-tempo-na-internet/\nhttps://pt.wikipedia.org/wiki/Brasil\nhttp://www.catolicoorante.com.br/oracao.php?id=6\nhttp://www.ofuxico.com.br/noticias-sobre-famosos/confira-o-clipe-oficial-da-cancao-salve-do-ex-bbb-viegas/2018/11/22-335469.html\nhttps://www.sbahq.org/curso-salve-uma-vida/\nhttps://piseagrama.org/salve-a-internet/\nhttps://www.merriam-webster.com/dictionary/salve\nhttps://poraqui.com/casa-forte/salve-o-bar-da-esquina-aposta-em-petiscos-exclusivos-e-drinks-bem-elaborados/'

    if platform.system() == 'Windows':
        os.system('copy NUL to_crawl.txt')

        tlin = open(arquivo_tocrawl, 'w')
        tlin.write(c)
        tlin.close()

        os.system('copy NUL crawled.txt')

    elif platform.system() == 'Linux':
        tlin = open(arquivo_tocrawl, 'w')
        tlin.write(c)
        tlin.close()

        arqv = open('crawled.txt', 'w')
        arqv.close()

else:
    print('Arquivo salvo encontrado')

t_arquivo = open(arquivo_tocrawl, 'r')
c_arquivo = open(arquivo_crawled, 'r')

to_crawl = list(t_arquivo.readlines())
crawled = set(c_arquivo.readlines())

t_arquivo.close()
c_arquivo.close()

def salvar():

    lista_crawl = to_crawl
    lista_crawled = list(crawled)

    t_lista = len(lista_crawl) - 1
    c_lista = len(lista_crawled) - 1

    try:
        S_tocrawl = open(arquivo_tocrawl, 'w')
        S_crawled = open(arquivo_crawled, 'w')

        for i in range(t_lista):
            if len(lista_crawl[i]) > 2:
                S_tocrawl.write(lista_crawl[i].encode('utf-8'))
                S_tocrawl.write('\n')

        for j in range(c_lista):
            if len(lista_crawl[i]) > 2:
                S_crawled.write((lista_crawled[j]).encode('utf-8'))
                S_crawled.write('\n')

        S_tocrawl.close()
        S_crawled.close()

    except:
        print('erro ao salvar o arquivo')

def reset(url):
    try:
        to_crawl.remove(url)
        crawled.add(url)
    except:
        return

def headers(url):
    url2 = re.findall('https?:\/\/([^"\'/]*)', url)

    if 'twitter.com' or 'www.twitter.com' == url2:
        header = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36',
            'referer': 'https://twitter.com/login/error?username_or_email=deathnote.hard%40gmail.com&redirect_after_login=%2F%3Flang%3Dpt-br',
            'cookie': ''}
    elif 'www.instagram.com' or 'instagram.com' == url2:
        header = {
            'cookie': '',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36'}
    else:
        header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36'}

    return header

def analisar(url):

    print(url)

    try:
        header = headers(url)
        req = requests.get(url, headers=header)
        html = req.text

    except:
        try:
            req = requests.get(url)
            html = req.text
        except:
            reset(url)
            return

    links = re.findall(r'href="?\'?(https?:\/\/[^"\'>]*)', html)
    url2 = re.findall('https?:\/\/([^"\'/]*)', url)

    for link in links:
        if link not in crawled and link not in to_crawl:
            if re.findall('((\.br)|(\.com)|(\.net)|(\.org))$', str(url2)[:-2]):
                to_crawl.append(link)
                salvar()
    reset(url)


def main():
    print 'started at ', time.asctime()
    while True:
        url1 = to_crawl[0]
        url2 = to_crawl[3]
        url3 = to_crawl[5]
        url4 = to_crawl[8]

        t_analisar1 = Thread(target=analisar(url1))
        t_analisar2 = Thread(target=analisar(url2))
        t_analisar3 = Thread(target=analisar(url3))
        t_analisar4 = Thread(target=analisar(url4))

        t_analisar1.start()
        t_analisar2.start()
        t_analisar3.start()
        t_analisar4.start()


main()