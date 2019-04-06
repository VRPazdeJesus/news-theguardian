import requests
import json
import pandas as pd

def exportar_csv(titulo, link, nome):
    df = pd.DataFrame({'Titulo': titulo, 'Link':link})
    df.to_csv("%s.csv" % nome, index=False, sep=";", encoding='utf-8-sig')
    print("Arquivo exportado com sucesso para a pasta do projeto!")

def buscar_noticias(dados):
    titulo = []
    link = []
    for posicao in dados['response']['results']:
        titulo.append(posicao['webTitle'])
        link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrado nenhum post. Tente mais tarde!")
    else:
        exportar_csv(titulo, link, "noticias")

def buscar_sports(dados):
    titulo = []
    link = []
    for posicao in dados['response']['results']:
        if posicao['pillarName'] == 'Sport':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrado nenhum post referente a esportes. Tente mais tarde!")
    else:
        exportar_csv(titulo, link, "sports")

def buscar_news(dados):
    titulo = []
    link = []
    for posicao in dados['response']['results']:
        if posicao['pillarName'] == 'News':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrada nenhuma notícia. Tente mais tarde!")
    else:
        exportar_csv(titulo, link, "news")

def buscar_arts(dados):
    titulo = []
    link = []
    for posicao in dados['response']['results']:
        if posicao['pillarName'] == 'Arts':
            titulo.append(posicao['webTitle'])
            link.append(posicao['webUrl'])
    if len(titulo) == 0:
        print("Não foi encontrado nenhum post referente a artes. Tente mais tarde!")
    else:
        exportar_csv(titulo, link, "arts")

def main():
    url = "https://content.guardianapis.com/search?api-key=11e6532a-ebc5-4b8b-a94e-e074781ea5c4"
    response = requests.get(url)
    if response.status_code == 200:
        print("Acessando a base de dados do The Guardian...")
        dados = response.json()
        
        escolha = 4
        while escolha != 0:
            print("1 - Esportes")
            print("2 - Notícias")
            print("3 - Artes")
            print("4 - Todas")
            print("0 - para sair")
            try:
                escolha = int(input("Digite o número referente a notícia que você deseja baixar!"))
            except:
                print("Por favor digite apenas números")
            if escolha > 4 or escolha < 0:
                print("Por favor digite números entre 0 e 4")
            elif escolha == 1:
                buscar_sports(dados)
            elif escolha == 2:
                buscar_news(dados)
            elif escolha == 3:
                buscar_arts(dados)
            elif escolha == 4:
                buscar_noticias(dados)
            elif escolha == 0:
                print("Obrigado por utilizar o programa!")
    else:
        print("Não foi possível acessar a base de dados.")

if __name__ == "__main__":
    main()