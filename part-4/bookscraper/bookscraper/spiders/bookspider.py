import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css('article.product_pod')
    
        for book in books: 
            yield{
                'name':book.css('h3 a::text').get(),
                'price':book.css('.product_price.price_color::text').get(),
                'url':book.css('h3 a').attrib['href']
            }
            
        # extrai o sufixo da próxima pagina       
        next_page = response.css('li.next a ::attr(href)').get()
        
        if next_page is not None:
            
            if 'catalogue/' in next_page:
            # se o sufixo for não nulo, então, concatena com o url
                next_page_url = 'https://books.toscrape.com/' + next_page
                
            else: 
                next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
            
            # rodar a função para a próxima página, até não haverem mais páginas
            yield response.follow(next_page_url , callback = self.parse)