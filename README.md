# web scraping com scrapy


### Inicializando env
```
conda install scrapy
conda create --name webscraping
conda activate webscraping       
```

### Projeto
```bash
scrapy startproject nome_da_pasta
```

### Na pasta spiders
``` bash
# scrapy genspider [nome] [url]
scrapy genspider bookspider books.toscrape.com
```