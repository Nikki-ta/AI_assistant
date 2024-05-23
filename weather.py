#https://www.google.com/search?q=weather+bareilly
# user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
#  span id ="wob_tm"

#from requests_html import HTMLSession
#import requests

from bs4 import BeautifulSoup
import requests
import text_to_speech


headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def weather(city):
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    text_to_speech.text_to_speech("Searching")
    soup = BeautifulSoup(res.text, 'html.parser')
   # time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    return (info + ", " +weather+ "°C" + " in " + city.replace("+weather",""))


#s = HTMLSession()
    #res = requests.get("https://ipinfo.io/")
    #data = res.json()
    #city = data["city"]
    #url = f'https://www.google.com/search?q=weather+{city}'
    #r = s.get(url, headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})
    #temp = r.html.find('span#wob_tm', first= True).text
   # unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first= True).text
  #  desc = r.html.find('span#wob_dc', first= True).text
  #  #c = r.html.find('div.eKPi4 span.BBwThe' , first = True).text
 #   return temp+" " + unit + " " +desc+ " in " + city




