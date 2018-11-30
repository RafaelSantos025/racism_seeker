from threading import Thread
import requests
import time
import re
import os

pasta = os.getcwd()

arquivo_tocrawl = pasta + '/to_crawl.txt'
arquivo_crawled = pasta + '/crawled.txt'

if 'to_crawl.txt' and 'crawled.txt' not in os.listdir(pasta):
    print('[...] Criando arquivo de Backup [...]')
    c = 'https://compartilhe.info/listas/sites-inuteis-e-interessantes-para-gastar-tempo/\nhttps://falauniversidades.com.br/10-sites-bizarros-para-voce-passar-o-tempo-na-internet/\nhttps://pt.wikipedia.org/wiki/Brasil\nhttp://www.catolicoorante.com.br/oracao.php?id=6\nhttp://www.ofuxico.com.br/noticias-sobre-famosos/confira-o-clipe-oficial-da-cancao-salve-do-ex-bbb-viegas/2018/11/22-335469.html\nhttps://www.sbahq.org/curso-salve-uma-vida/\nhttps://piseagrama.org/salve-a-internet/\nhttps://www.merriam-webster.com/dictionary/salve\nhttps://poraqui.com/casa-forte/salve-o-bar-da-esquina-aposta-em-petiscos-exclusivos-e-drinks-bem-elaborados/\nhttps://tudosobreposgraduacao.wordpress.com/2017/12/12/lista-de-links-ativos-para-o-sci-hub/\nhttps://www.fabricadenoobs.com.br/deep-web/listas-de-links/\nhttps://www.criarsites.com/como-colocar-lista-de-links-personalizada-no-blogger-ou-wordpress/\nhttps://viajantesolo.com.br/companhias-aereas/programa-de-milhagem-lista-de-links-das-companhias-aereas-para-se-inscrever\nhttps://helpdesk.e-goi.com/806078-O-E-goi-diz-que-tenho-dom%C3%ADnio-recente-ou-links-em-lista-negra-Socorro?r=1\nhttps://www.techtudo.com.br/dicas-e-tutoriais/noticia/2013/11/como-incluir-links-de-sites-na-lista-de-leitura-do-windows-81.html\nhttps://portal.fiocruz.br/caixa-editorial/materias-dialogos-pensesus-duplo-vertical-lista-links\nhttps://tableless.com.br/criando-um-menu-horizontal-com-css/\nhttp://www.embarquenaviagem.com/2014/09/13/diario-professor-divulga-uma-super-lista-com-links-sobre-o-meio-ambiente/'

    tlin = open(arquivo_tocrawl, 'w')
    tlin.write(c)
    tlin.close()

    arqv = open('crawled.txt', 'w')
    arqv.close()

else:
    print('[*] Arquivo de Backup encontrado [*]')

t_arquivo = open(arquivo_tocrawl, 'r')
c_arquivo = open(arquivo_crawled, 'r')

to_crawl = list(t_arquivo.readlines())
crawled = set(c_arquivo.readlines())

t_arquivo.close()
c_arquivo.close()

def salvar():

    lista_crawled = list(crawled)

    t_lista = len(to_crawl) - 1
    c_lista = len(crawled) - 1

    try:
        S_tocrawl = open(arquivo_tocrawl, 'w')
        S_crawled = open(arquivo_crawled, 'w')

        for i in range(t_lista):
            if len(to_crawl[i]) > 2:
                S_tocrawl.write(to_crawl[i].encode('utf-8'))
                S_tocrawl.write('\n')

        for j in range(c_lista):
            if len(lista_crawled[j]) > 2:
                S_crawled.write((lista_crawled[j]).encode('utf-8'))
                S_crawled.write('\n')

        S_tocrawl.close()
        S_crawled.close()

        print('[*] Progresso salvo ' + time.asctime() + ' [*]')

    except:
        print('[!] Erro ao salvar o progresso [!]')

def reset(url):
    try:
        to_crawl.remove(url)
        crawled.add(url)
    except:
        print('[!] Erro ao resetar url [!]')
        return

def headers(dominio):

    if 'twitter.com' or 'www.twitter.com' == dominio:
        header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36','referer': 'https://twitter.com/login/error?username_or_email=deathnote.hard%40gmail.com&redirect_after_login=%2F%3Flang%3Dpt-br','cookie': ''}
    elif 'www.instagram.com' or 'instagram.com' == dominio:
        header = {'cookie': '','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36'}
    else:
        header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/70.0.3538.77 Chrome/70.0.3538.77 Safari/537.36'}

    return header

def analisar(url):

    print(url)
    dominio = re.findall('https?:\/\/([^"\'/]*)', url)

    try:
        header = headers(dominio)
        req = requests.get(url, headers=header)
        html = req.text

    except:
        print('[!] Nao foi possivel usar o Header [!]')
        try:
            req = requests.get(url)
            html = req.text
        except:
            reset(url)
            return

    links = re.findall(r'href="?\'?(https?:\/\/[^"\'>]*)', html)

    for link in links:
        if link not in crawled and link not in to_crawl:
            if re.findall('((\.br)|(\.com)|(\.net)|(\.org))$', str(dominio)[:-2]):
                to_crawl.append(link)

    reset(url)

def main():

    print 'Started at ', time.asctime()
    temporizador = 0

    while True:
        if temporizador == 20:
            salvar()
            temporizador = 0

        url1 = to_crawl[0]
        url2 = to_crawl[3]
        url3 = to_crawl[5]
        url4 = to_crawl[8]
        url5 = to_crawl[10]
        url6 = to_crawl[12]
        url7 = to_crawl[14]
        url8 = to_crawl[15]
        url9 = to_crawl[16]
        url10 = to_crawl[17]

        t_analisar1 = Thread(target=analisar(url1))
        t_analisar2 = Thread(target=analisar(url2))
        t_analisar3 = Thread(target=analisar(url3))
        t_analisar4 = Thread(target=analisar(url4))
        t_analisar5 = Thread(target=analisar(url5))
        t_analisar6 = Thread(target=analisar(url6))
        t_analisar7 = Thread(target=analisar(url7))
        t_analisar8 = Thread(target=analisar(url8))
        t_analisar9 = Thread(target=analisar(url9))
        t_analisar10 = Thread(target=analisar(url10))

        t_analisar1.start()
        t_analisar2.start()
        t_analisar3.start()
        t_analisar4.start()
        t_analisar5.start()
        t_analisar6.start()
        t_analisar7.start()
        t_analisar8.start()
        t_analisar9.start()
        t_analisar10.start()

        temporizador += 1

main()
