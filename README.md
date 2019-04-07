# News The Guardian

![The Guardian](https://media-assets-05.thedrum.com/cache/images/thedrum-prod/s3-news-tmp-90538-download--2x1--900.jpg)

> Um script modularizado para buscar, através da API do jornal The Guardian, as últimas notícias e exportar para CSV os títulos e links das notícias de algumas categorias:

  - News
  - Sports
  - Arts

### Funções 

```sh
exportar_csv(titulo, link, nome)
buscar_noticias(dados)
buscar_sports(dados)
buscar_news(dados)
buscar_arts(dados)
```

### Execução
> Pré-requisitos: Ter GIT e Python 3 instalados na máquina
```sh
$ git clone https://github.com/VRPazdeJesus/news-theguardian.git
$ cd news-theguardian
$ pip install requests
$ pip install pandas
$ python news.py
```
### Comandos do GIT
```sh
$ git status
$ git add .
$ git commit -m "texto"
$ git pull --rebase origin master
$ git push origin master
```

### Desenvolvedor
> Víctor Romário - 
> Desenvolvedor Web e Mobile - https://www.victorromario.com.br/
> Aplicação para demonstração aos alunos do curso "Programando em Python"
