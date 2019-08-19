#webscraper
from bs4 import BeautifulSoup
import requests
import regex as re
contador = 1
modelo = input("insira o nome: \n")
marca = input ("insira a marca: \n")
planilha = input("insira o nome do dataset: \n")
pagina = ("https://carros.mercadolivre.com.br/"+str(marca)+"/"+str(modelo)+"/_Desde_"+str(contador))
pagina = requests.get(pagina)
soup = BeautifulSoup(pagina.content,'html.parser')
busca = soup.find(class_="section search-results list-view grid search-results-mot list--has-row-logos")
carros = busca.find_all(class_="results-item highlighted article grid product item-with-attributes")
while busca != None:
 pagina = ("https://carros.mercadolivre.com.br/"+str(marca)+"/"+str(modelo)+"/_Desde_"+str(contador))
 pagina = requests.get(pagina)
 soup = BeautifulSoup(pagina.content,'html.parser')
 busca = soup.find(class_="section search-results list-view grid search-results-mot list--has-row-logos")
 carros = busca.find_all(class_="results-item highlighted article grid product item-with-attributes")
 for item in carros:
  preco = item.find(class_="price__fraction").get_text()
  linke = item.find('a', href = re.compile(r'[/]([a-z]|[A-Z])\w+')).attrs['href']
  atributos = item.find(class_="item__attrs").get_text()
  atributos = atributos.split('|')
  ano = str(int(atributos[0]))
  kms = str(int(atributos[1][:-2]))
  f = open(str(planilha+".csv"), 'a+')
  f.write (preco+","+ano+","+kms+","+linke+"\n") 
 contador += 50
f.close()