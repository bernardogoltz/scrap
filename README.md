# web scraping com scrapy

## First Scrapy Spider
    $git clone https://github.com/bernardogoltz/scrap

### Inicializando env
```
conda install scrapy
conda create --name webscraping
conda activate webscraping       
```

#
### Inicializando Projeto
```bash
scrapy startproject [nome_da_pasta]
```
```bash
scrapy shell [url]
```
```bash
fetch [url]
```
#
### Na pasta spiders
``` bash
# scrapy genspider [nome] [url]
scrapy genspider bookspider books.toscrape.com
```

#
### Rodando o crawler:
url "books.toscrape.com" <br> path = bookscraper\spiders

```python
# Pegando os livros na página 
def parse(self, response):
    
    books = response.css('article.product_pod')
    for book in books: 
        yield{
            'name':book.css('h3 a::text').get(),
            'price':book.css('.product_price.   price_color::text').get(),
            'url':book.css('h3 a').attrib['href']
        }
```

```bash
# @ terminal: scrapy crawl [spider_name]
scrapy crawl bookspider
```



    