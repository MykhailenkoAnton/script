from bs4 import BeautifulSoup
import requests
import os
import os, os.path

# princip_url = 'https://princip.ua/'
# princip_url_withou_slash = 'https://princip.ua'

# url = input('Please input link to parse from princip.ua: ')
# print("  ------------------------------------------------------------- \n" )

# # Check that given url is valid for parse.
# is_url_valid = url.split(".ua/catalog/")
# if is_url_valid[0] != 'https://princip':
#     print("-- Not valid url provided: " + url)
#     exit()
# else:
#     print("-- Parse: " + url)

# # url = "https://princip.ua/catalog/khoztovary/"

# url_page = url + 'filter/clear/apply/?PAGEN_1='
# catalog = url.split(princip_url)[1] # 'catalog/igry-igrushki-detskoe-tvorchestvo/nastolnye-igry/'

def parse_page(link):
    # Make request and get html.
    print("-- Start to parce link: ", link)
    html_text = requests.get(link).text

    # Parse html to BeautifulSoup object.
    soup = BeautifulSoup(html_text, 'lxml')

    # Find all apartments list.
    apartments_section = soup.find_all("section", class_ = lambda value: value and value.startswith("ticket-clear line"))

    for apartment in apartments_section:
        price = apartment.find("div", class_ = "mb-5 mt-10 pr")
        print(price.text)
#     # Find product code.
#     product_item_detail_article = soup.find('div', class_ = 'product-item-detail-article')
#     code = ""
#     try:
#         code = product_item_detail_article.find('span').text
#     except AttributeError:
#         print("  - Can't get product code from link: " + link)
#         return

#     print("-- Try to get product with code: " + code)

#     # Find product name.
#     name = ""
#     try:
#         name = soup.find('h1', class_ = 'navigation-title').text
#     except AttributeError:
#         print("  - Can't get product name for product with code:" + code)
    
#     # Find product price.
#     price = ""
#     try:
#         pay_block = soup.find('div', class_ = 'product-item-detail-pay-block')
#         price = pay_block.find('span', class_ = 'product-item-detail-price-current').text
#     except AttributeError:
#         print("  - Can't get product price for product with code:" + code)
#     except:
#         print("  - Unknow error with product price for product with code:" + code)
    
#     # Find product description.
#     description_block = ""
#     try:
#         description_block = soup.find('div', class_ = 'col-xs-12 product-item-detail-description').text
#     except AttributeError:
#         print("  - Can't get description for product with code:" + code)

#     # Create directory
#     dirName = catalog + code
#     try:
#         # Create target Directory
#         os.makedirs(dirName)
#         print("  - Directory " , dirName ,  " Created.") 
#     except FileExistsError:
#         print("  - Directory " , dirName ,  " already exists, will replace it contents.")

#     # Write information about product in file.
#     print("  - Write information to file...")
#     file = open(dirName + "\\" + code + '.txt', 'w', encoding='utf-8')
#     file.write('Код: ' + code + '\n')
#     file.write('Имя: ' + name + '\n')
#     file.write('Цена: ' + price + '\n')
#     file.write(description_block)
#     file.close()

#     # Download all images from container with them.
#     image_block = ""
#     try:
#         image_block = soup.find('div', attrs={'class': 'product-item-detail-slider-videos-images-container'})
#     except:
#         print("  - Can't get description for product with code:" + code)

#     image_index = 1
#     for image_tag in image_block.find_all('img'):
#         image_path = princip_url_withou_slash + image_tag['data-lazyload-src'].split('.')[0] + '.jpeg' # Get image url.
#         print("  - Download image from: " + image_path)
#         image = requests.get(image_path)
#         out = open(dirName + '\\' + str(image_index) + "_img.jpg", "wb")
#         out.write(image.content)
#         out.close()
#         image_index = image_index + 1
    
#     print("  ------------------------------------------------------------- \n" )

# # ----------------------------------------------------------------------------------------------------------------------
# # Find number of last page for current product type
# # parse_product("https://princip.ua/catalog/igry-igrushki-detskoe-tvorchestvo/nastolnye-igry/igra-nastolnaya-9-toy-samiy-krokodil-danko-toys/")
parse_page("https://dom.ria.com/uk/arenda-kvartir/odessa/?page=1")

exit()

html_base_page = requests.get("https://dom.ria.com/uk/arenda-kvartir/odessa/?page=1").text
soup_base_page = BeautifulSoup(html_base_page, 'lxml')

page_count = ""
try:
    page_count = soup_base_page.find_all('span', class_ = 'page-item mhide')[-1].get_text().strip()
except:
    print("-- Can't get page_count!" )
    exit()

print("-- Will parse " + page_count + " pages with apartments...")
print("  ------------------------------------------------------------- \n" )


# for index in range(int(last_page_number)):
#     html_with_product_links = requests.get(url_page + str(index + 1) ).text
#     soup = BeautifulSoup(html_with_product_links, 'lxml')
#     for products in soup.find_all('div', attrs={'class': 'col-xs-6 col-md-3'}):
#         product_item_title = products.find('div', class_= 'product-item-title')
#         link = product_item_title.find('a', href=True)
#         parse_product(princip_url_withou_slash + link['href'])