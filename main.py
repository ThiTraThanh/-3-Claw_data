from TikiClawer import TikiClawer
from data import *
import time 

<<<<<<< HEAD
tiki_url = "https://tiki.vn"
=======
# Const
tiki_url = "https://tiki.vn/search?q="

>>>>>>> 47db73e36ce1730ee1a5f69ce5b0b0c8ffb770b3
keywords = "balo"

tiki = TikiClawer()

<<<<<<< HEAD
tiki.getUrl(tiki_url)
tiki.sendSearchInput(keywords)
=======
tiki.getUrl(tiki_url + keywords)
links = tiki.getProductLinks(productLinksXpath)
print(links)

total_products = []

time.sleep(3)

for link in links:
    # Vào chi tiết sản phẩm
    tiki.getUrl(link)
    
    # Lấy brand
    tiki.getBrand(brand_xpath)
    
    # Lấy name
    
    # lấy price
    
>>>>>>> 47db73e36ce1730ee1a5f69ce5b0b0c8ffb770b3
