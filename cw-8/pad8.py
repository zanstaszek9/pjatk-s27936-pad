
#zad 1

#   Strona PAP zabrania na scrapowanie w podstronach admin, komentarzy, media, logowania i konfiguracyjnych. Strona główna i artykuła nie są objęte zakazem




#zad 2
    # Stwórz obiekt driver, który połączy się ze stroną Polskiej Agencji Prasowej. A następnie:
    # a.	Zaakceptuje pliki cookies
    # b.	Zwiększy okno przeglądarki na cały ekran
    # c.	Zmieni język strony na angielski
    # d.	Wejdzie w sekcję Business
    # e.	Z sekcji business  ściągnie wszystkie tytuły do listy titles
    # f.	Ściągnie wszystkie zdjęcia z tej sekcji na dysk lokalny
    # g.	Zjedzie na dół strony
    # h.	Przejdzie na ostatnią stronę i zwróci printem jej numer (atrybut text)

from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request



driver = webdriver.Chrome(executable_path='/chromedriver')
driver.get('https://www.pap.pl')

print('### Start Scrapping ### \n\n\n')
accept_cookies = driver.find_element(By.XPATH, '//*[@id="cookie"]/div/div/div/div/div/div[1]')
accept_cookies.click()

driver.maximize_window()

change_language = driver.find_element(By.XPATH, '//*[@id="navbar"]/ul[2]/li[3]/a')
change_language.click()

go_to_business = driver.find_element(By.XPATH, '//*[@id="block-mainnavigationen"]/ul/li[3]/a')
go_to_business.click()

titles = []
for title in driver.find_elements(By.CLASS_NAME,'title'):
    titles.append(title.text.split('\n')[0])
# print(titles)



i = 0
for image in driver.find_elements(By.TAG_NAME, "img"):
    src = image.get_attribute("src")
    urllib.request.urlretrieve(src, str(i)+'.jpg')
    i = i+1



driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
#time.sleep(1000)

go_last_page = driver.find_element(By.XPATH, '/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[6]/a/span[2]')
go_last_page.click()


last_page_number = driver.find_element(By.XPATH, '/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[6]/a')
print(last_page_number.text)



driver.close()


