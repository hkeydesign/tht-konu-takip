import requests
from lxml import html
import time
from win10toast import ToastNotifier

link = input('Konu Linki: ')

temp = None
temp_like = None
while True:
    
    r = requests.get(link)

    tekil = html.fromstring(r.content)
    tekil = tekil.xpath('body/div[@id="posts"]/div/div/div[2]/div[@style="padding:0px 0px 0px 0px"][1]/div[@class="postbit-content d-flex"]/div[2]/div/div[1]/div/div[6]/a/@href')
    tekil = tekil[0]
    tekill = requests.get(tekil)
    tekill = html.fromstring(tekill.content)

    thankseds = tekill.xpath('//*[@class="dbtech-ent-count"]/div[@class="thankseds"]/a/span/text()')
    print(thankseds)
    r = html.fromstring(r.content)
    r = r.xpath('/html/body/div[5]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/text()')
    r = r[0].strip('\n')
    if r !=temp and temp != None:
        print('naber')
        bildirim = ToastNotifier()
        bildirim.show_toast("THT","Konuna yeni bir yorum eklendi. Bakmaya ne dersin ?")
    
    print(r)
    temp = r
    if thankseds !=temp_like and temp_like != None and len(temp_like)<len(thankseds):
        bildirim = ToastNotifier()
        bildirim.show_toast("THT","Birisi konuna teşekkür etti ! Bakmaya ne dersin ?")
    temp_like = thankseds
    time.sleep(10)
