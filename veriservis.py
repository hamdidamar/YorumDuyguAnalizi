import  urllib.request
import re
import io
import json
import requests
import pandas as pd
from sklearn.utils import shuffle





def verigetir(kategori):
	#parametre olarak girilen kategori ıd yi atıyoruz.
	url = "https://www.hepsiburada.com/navigation/" + kategori

	#oluşan url üzerinden istek tanımlıyoruz
	istek = urllib.request.Request(url)

	#tanımlanan istek üzerinden veri isteği yapıyoruz

	try:
		cevap = urllib.request.urlopen(istek)

    except:
    	print("cevap alınırken hata oluştu")

    #normalizasyon işlemlerini yapıyoruz
    htmlBytes = cevap.read()
	htmlStr = htmlBytes.decode("utf8")

	#normalize olmuş kategorilerimizi jsona convert yapıyoruz
	json_cevap = json.loads(htmlStr)

	#kategorimizden urlleri çekme işlemlerini yapıyoruz
	kategoriler=[]
	for item in json_cevap['items']:
        kategoriler.append(item['title'])

    i = 0
	for i in range(len(kategoriler)):
    	i = i+1


    kategori_level_1=[]
	kategori_level_2=[]
	kategori_level_3=[]
	kategori_level_4=[]
	kategoriler = []

	if (kategori == '1711'):
	    for item in json_cevap['items']:
	        print(item['title'])
	        if(item['title'] == kategori2):
	            if(item['url']):
	                kategori_level_1.append(item['url'])
	                for child in item['children']:
	                    for child2 in child['children']:
	                        if(child2['url']):
	                            kategori_level_2.append(child2['url'])
	                            for child3 in child2['children']:
	                                if(child3['url']):
	                                    kategori_level_3.append(child3['url'])
	    kategoriler.append(kategori_level_1)
	    kategoriler.append(kategori_level_2)
	    kategoriler.append(kategori_level_3)
	    kategoriler.append(kategori_level_4)
	else :
	    for item in json_cevap['items']:
	            for child in item['children']:
	                print(child['title'])
	                if (child['title'] == kategori2):
	                    kategori_level_1.append(child['url'])
	                for child2 in child['children']:
	                    if (child2['url']):
	                        kategori_level_2.append(child2['url'])
	                    if (len(child2['children']) > 0):
	                        for child3 in child2['children']:
	                            kategori_level_3.append(child3['url'])
	                            for child4 in child3['children']:
	                                kategori_level_4.append(child4['url'])
	            break
	    kategoriler.append(kategori_level_2)
	    kategoriler.append(kategori_level_3)
	    kategoriler.append(kategori_level_4)

	#toplanan kategorileri bir txt dosyasına yazdırıyoruz.
	with open("data/kategoriler_liste.txt","w") as txt_file:
	    for line in kategoriler_liste:
	        txt_file.write(line + "\n")


	url = "https://www.hepsiburada.com"
	urunler = set()

	#hazırladığımız kategorileri alıyoruz
	f = open("kategoriler_liste.txt", "r")
	satirlar = f.read().split('\n')

	yeni_url = url + satirlar[sayi2]

	for sayi2 in range(1):
	    yeni_url = url + satirlar[sayi2]
	    
	    htmlStr = requests.get(yeni_url).text

	    aranan = '<a href="(.*?)-c-(.*?)sayfa=(.*?)" class="page-(.*?)">(.*?)</a>'
	    sayfalar = re.findall(aranan, htmlStr)
	    if len(sayfalar) > 0:
	        sayfa_sayisi = int(sayfalar[-1][2])
	        print('sayfa sayisi: ' + str(sayfa_sayisi))
	        sayfa = 1
	        for sayi in range(sayfa_sayisi):
	            url2 = yeni_url + '?sayfa=' + str(sayi + 1)
	            try:
	                htmlStr2 = requests.get(url2).text
	            except:
	                print("hata oluştu")

	            aranan2 = '"(.*?)" data-sku="(.*?)"'
	            sonuc2 = re.findall(aranan2, htmlStr2)

	            for urun in sonuc2:
	                if urun[0] not in urunler:
	                    urunler.add(urun[0])
	    else:
	        url3 = yeni_url
	        try:
	            htmlStr3 = requests.get(url3).text
	        except:
	            print("hata oluştu")

	        aranan3 = '"(.*?)" data-sku="(.*?)"'
	        sonuc3 = re.findall(aranan3, htmlStr3)

	        for word in sonuc3:
	            if word[0] not in urunler:
	                urunler.add(word[0])


	with open("urunler_liste.txt","w") as txt_file:
	    for line in urunler:
	        txt_file.write(line + "\n")

	def duzelt(yazi):
    	return yazi.replace("&#252;","ü").replace("&#220;","Ü").replace("&#231;","ç").replace("&#199;","Ç").replace("&#246;","ö").replace("&#214;","Ö").replace("&#39;","'")

	def parantezTemizle(yazi):
	    return yazi.replace("(","").replace(")","")

	def yorumEkle(y):
	    ysatir = y.replace('\n','').replace('\r','').replace('  ','')
	        
	    desen = '<span class="avatar">(.*?)style="width: (.*?)%">(.*?)itemprop="datePublished" content="(.*?)">(.*?)</strong>(.*?)<div class="review"><strong class="subject" itemprop="name">(.*?)</strong><p class="review-text" itemprop="description">(.*?)</p></div>(.*?)<div class="comment-provider"><span class="user-info" itemprop="author"content="(.*?)">(.*?)</span><span class="location">(.*?)</span>(.*?)data-agreed="true">Evet <b>(.*?)</b></a>(.*?)data-agreed="false">Hayır <b>(.*?)</b>(.*?)</span></div>'
	    sonuc = re.findall(desen, ysatir)

	    yorum = (int(sonuc[0][1]) / 100, parantezTemizle(duzelt(sonuc[0][7])))
	    yorumlar.add(yorum)

	url = "https://www.hepsiburada.com"
	yorumlar = set()

	f = open("urunler_liste.txt", "r")
	satirlar = f.read().split('\n')

	for satir in satirlar:
	    yeni_url = url + satir + "-yorumlari"
	    try:
	        htmlStr = requests.get(yeni_url).text
	        yorumdeseni = '<li class="review-item" itemprop="review" itemscope="itemscope" itemtype="http://schema.org/Review">(.*?)</li>'
	        yorum = re.findall(yorumdeseni, htmlStr, re.MULTILINE|re.DOTALL)

	        if len(yorum) > 0:
	            sayfadeseni = 'class="page-(.*?)">'
	            sayfalar = re.findall(sayfadeseni, htmlStr)

	            for y in yorum:
	                yorumEkle(y)

	        print(yeni_url)
	        if len(sayfalar) > 0:
	            sayfa_sayisi = int(sayfalar[-1])

	            for i in range(2, sayfa_sayisi + 1):
	                yeni_url2 = yeni_url + "?sayfa=" + str(i)
	                htmlStr2 = requests.get(yeni_url2).text
	                yorum = re.findall(yorumdeseni, htmlStr2, re.MULTILINE|re.DOTALL)
	                for y in yorum:
	                    yorumEkle(y)
	    except:
	        print("hata")

	with open("data/yorumlar_liste.csv", "w",encoding="utf-8") as txt_file:
	    txt_file.write("Puan" + "\t" + "Yorum" + "\n")
	    for line in yorumlar:
	        txt_file.write(str(line[0]) + "\t" + str(line[1]).replace("\t", " ") + "\n")

	data = pd.read_csv('data/yorumlar_liste.csv', sep = "\t")
	data.loc[data['Puan'] > 0.7, 'Puan'] = 1.0
	data.loc[data['Puan'] < 0.5, 'Puan'] = 0.0
	df_1 = data[data.Puan > 0.9]
	df_1 = df_1.head(300)#300istediğimiz kadar
	df_0 = data[data.Puan < 0.1]
	df_0 = df_0.head(300)
	df = pd.concat([df_0, df_1], ignore_index = True)
	df = shuffle(df)
	
	df.to_csv("data/yorumlar.csv", sep = "\t", encoding = "utf-8", index = False)


	              



