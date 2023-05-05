# MODULE
import os,sys,requests,re,time,bs4,datetime,random
from tqdm import tqdm
from colorama import init, Fore
from datetime import datetime
from bs4 import BeautifulSoup as soup
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel
from rich import print as jalan
init()


# WARNA
x = '\33[m' 		# PUTIH
m = '\x1b[1;91m' 	# MERAH
s = '\33[100m'		# ABU BG
n = '\33[34m'    	# MATI
k = '\033[93m' 		# KUNING
c = '\33[46m' 		# CYAN BG
h = '\33[92m' 		# HIJAU +
hb = '\33[42m'		# HIJAU BOLD
mb = '\33[41m'		# MERAH BOLD

# REUNI ALL
ses = requests.Session()
jumlah,sm,reac = [],[],[]
tulis,commen,pasi = [],[],[]
jajan = []


# BANNER
def banner():
	if "linux" in sys.platform.lower():
		try:os.system('clear')
		except:pass
	elif "win" in sys.platform.lower():
	    try:os.system('cls')
	    except:pass
	else:
	    try:os.sytem('clear')
	    except:pass
	wel = '# FACEBOOK BOOT TOOLS'
	wel2 = mark(wel, style='green')
	sol().print(wel2,style='white')
	text = ('[white]██████╗  ██████╗ ████████╗███████╗██████╗\n██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔══██╗\n██████╔╝██║   ██║   ██║   █████╗  ██████╔╝\n██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══██╗\n██████╔╝╚██████╔╝   ██║   ██║     ██████╔╝\n╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═════╝\n[green]Welcome to script boot facebook[white]')
	nel2 = Panel(text,style="green")
	jalan(Panel(nel2,style="cyan"))

# LOGIN
def login():
	banner()
	cook = input(f'  {x}[ {h}!{x} ] Enter Cookies :{h} ')
	open('.cookie.txt','w').write(cook)
	bahasa()
	try:
	    url = 'https://mbasic.facebook.com/settings/account/?'
	    get = ses.get(url,cookies={'cookie':cook})
	    sop = soup(get.text,'html.parser')
	    sear = sop.findAll('h3')
	    for alin in sear:
	    	pas = alin.text
	    	if 'Nama' in pas:
	    		nam = pas.replace('Nama','')
	    		open('.nama.txt','w').write(nam)
	    	elif 'Alamat Email' in pas:
	    		em = pas.replace('Alamat Email','')
	    		if '@' in em:
	    			open('.email.txt','w').write(em)
	    		else:
	    			ok = 'Unknow'
	    			open('.email.txt','w').write(ok)
	    	elif 'Nomor Telepon' in pas:
	    		ph = pas.replace('Nomor Telepon','')
	    		if '0' in ph:
	    			open('.phone.txt','w').write(ph)
	    		elif '62' in ph:
	    			open('.phone.txt','w').write(ph)
	    		else:
	    			ok = 'Unknow'
	    			open('.phone.txt','w').write(ok)
	    	else:pass
	except Exception as e:
	    print(f'  {x}[ {m}•{x} ]{m}Login Failled');time.sleep(2)
	    login()

# CHECKING ACCOUNT
def check():
	bahasa()
	try:
	    cook = open('.cookie.txt','r').read()
	    url = 'https://mbasic.facebook.com/settings/account/?'
	    get = ses.get(url,cookies={'cookie':cook})
	    sop = soup(get.text,'html.parser')
	    sear = sop.findAll('h3')
	    for alin in sear:
	    	pas = alin.text
	    	if 'Nama' in pas:
	    		nam = pas.replace('Nama','')
	    		open('.nama.txt','w').write(nam)
	    	elif 'Alamat Email' in pas:
	    		em = pas.replace('Alamat Email','')
	    		if '@' in em:
	    			open('.email.txt','w').write(em)
	    		else:
	    			ok = 'Unknow'
	    			open('.email.txt','w').write(ok)
	    	elif 'Nomor Telepon' in pas:
	    		ph = pas.replace('Nomor Telepon','')
	    		if '0' in ph:
	    			open('.phone.txt','w').write(ph)
	    		elif '62' in ph:
	    			open('.phone.txt','w').write(ph)
	    		else:
	    			ok = 'Unknow'
	    			open('.phone.txt','w').write(ok)
	    	else:pass
	except:
	    print(f'  {x}[ {m}•{x} ] {m}Check Failled');time.sleep(2)
	    login()

# UBAH BAHASA
def bahasa():
	try:
		cook = open('.cookie.txt','r').read()
		req = ses.get('https://mbasic.facebook.com/language/',cookies={'cookie':cook})
		pra = soup(req.content,'html.parser')
		for x in pra.find_all('form',{'method':'post'}):
		    if 'Bahasa Indonesia' in str(x):
		        bahasa = {
		            "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
		            "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
		            "submit"  : "Bahasa Indonesia"}
		        url = 'https://mbasic.facebook.com' + x['action']
		        exec = ses.post(url,data=bahasa,cookies={'cookie':cook})
	except:pass

# MENU
def menu():
	check()
	banner()
	ip = requests.get("https://api.ipify.org").text
	nam,ema,pho = open('.nama.txt','r').read(),open('.email.txt','r').read(),open('.phone.txt','r').read()
	print(f'{x} ╔ {x}[ {h}•{x} ] Your Name  : {h}'+nam)
	print(f'{x} ╠ {x}[ {h}•{x} ] Your Email : {h}'+ema)
	print(f'{x} ╠ {x}[ {h}•{x} ] Your Phone : {h}'+pho)
	print(f'{x} ╠ {x}[ {h}•{x} ] Your Ip    : {h}{ip}{x}')
	print(f'{x} ║')
	print(f'{x} ╠══ [ {h}•{x} ] MENU UTAMA TOOLS')
	print(f'{x} ║')
	print(f'{x} ╠══ [ {h}1{x} ] Bot auto confirmations		[{k} ON {x}]')
	print(f'{x} ╠══ [ {h}2{x} ] Bot komen target			[{m} OF {x}]')
	print(f'{x} ╠══ [ {h}3{x} ] Bot komen & Reaction beranda		[{h} ON {x}]')
	print(f'{x} ╠══ [ {h}4{x} ] Bot pesan masal			[{h} ON {x}]')
	print(f'{x} ╠══ [ {h}5{x} ] Lihat log aktifitas			[{h} ON {x}]')
	print(f'{x} ╠══ [ {h}0{x} ] Log out')
	print(f'{x} ║')
	pilih = input(f'{x} ╚══ [ {h}!{x} ] Pilih : ')
	if pilih in ['1','2','3','4','5']:
		setting(pilih)
	elif '0' in pilih:
		os.system('rm -rf .cookie.txt')
		exit()
	else:
		print(f'{x} ═══ [ {m}!{x} ] EROR MENU SELEC')
		time.sleep(3)
		menu()

# SETTING
def setting(pilih):
	banner()
	if '1' in pilih:
		konfirmasi('/friends/center/requests/?')
		print(f'\r{x} ╚══ [ {h}•{x} ] Berhasil mengonfirmasi{h} {len(jumlah)}{x} Requests')
	elif '2' in pilih:
		pass
	elif '3' in pilih:
		print(f'{x} ╠ {x}[ {h}•{x} ] Menu ')
		print(f'{x} ╠ {x}[ {h}1{x} ] Dengan Reaction		[ {h}2{x} ] Hanya Komentar')
		print(f'{x} ║')
		pas = input(f'{x} ╠══ [ {h}!{x} ] Pilih : ')
		pasi.append(pas)
		if '1' in pas:
			print(f'{x} ║')
			print(f'{x} ╠ {x}[ {h}•{x} ] Menu Reaction')
			print(f'{x} ╠ {x}[ {h}1{x} ] Suka		[ {h}5{x} ] Wow')
			print(f'{x} ╠ {x}[ {h}2{x} ] Super		[ {h}6{x} ] Sedih')
			print(f'{x} ╠ {x}[ {h}3{x} ] Peduli		[ {h}7{x} ] Marah')
			print(f'{x} ╠ {x}[ {h}4{x} ] Haha		[ {h}8{x} ] Kembali')
			print(f'{x} ║')
			pil = input(f'{x} ╠══ [ {h}!{x} ] Pilih : ')
			reac.append(pil)
		else:
			pass
		print(f'{x} ║')
		print(f'{x} ╠ {x}[ {h}•{x} ] Menu Komentar')
		print(f'{x} ╠ {x}[ {h}1{x} ] Dengan foto	[{m} OF {x}]	[ {h}2{x} ] Hanya text	[{h} ON {x}]')
		print(f'{x} ║')
		pilih = input(f'{x} ╠══ [ {h}!{x} ] Pilih : ')
		commen.append(pilih)
		if '1' in pilih:
			pass
		elif '2' in pilih:
			print(f'{x} ║')
			print(f'{x} ╠══ [ {k}!{x} ] Gunakan [{h} , {x}] jika ingin komentar random ')
			text = input(f'{x} ╠══ [ {h}!{x} ] Masukan text : ')
			if ',' in text:
				co = text.split(',')
				for ok in co:
					tulis.append(ok)
			else:
				tulis.append(text)
			banner()
			komen('https://mbasic.facebook.com/home.php')
	elif '4' in pilih:
		print(f'{x} ╠══ [ {h}!{x} ] Gunakan [{h} , {x}] jika ingin komentar random ')
		text = input(f'\r{x} ╚══ [ {h}•{x} ] Masukan Pesan :{h} ')
		if ',' in text:
			co = text.split(',')
			for ok in co:
				tulis.append(ok)
		else:
			tulis.append(text)
		banner()
		pessan('https://mbasic.facebook.com/messages/?')
	elif '5' in pilih:
		logger('/allactivity')

# CONFIRMATIONS
def konfirmasi(urll):
	try:
		cook = open('.cookie.txt','r').read()
		url = 'https://mbasic.facebook.com'
		get = ses.get(url+urll,cookies={'cookie':cook}).text
		ambil = re.findall('a\ class\=\"..\"\ href\=\".*\"\>(.*?)\<\/a\>\<div(.*?)\<\/div\>\<div\ class\=\"..\"\>\<a\ href\=\"(.*?)\"\>',get)
		for co in ambil:
			sm.append(co[0])
			print(f'\r{x} ╚══ [ {h}•{x} ] Sedang mengonfirmasi{h} {len(sm)}{x} Requests',end='')
			ok = soup(ses.get(url+co[2],cookies={'cookie':cook}).content,'html.parser')
			fom = ok.find('form',{'method':'post'})
			dat = {
			'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
			'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
			'submit' : 'Konfirmasi'
			}
			uri = url+co[2]
			post = ses.post(uri,data=dat,cookies={'cookie':cook})
			if '<Response [200]>' in str(post):
				print(f'\r{x} ╚══ [ {h}•{x} ] Berhasil mengonfirmasi,{h} '+co[0])
				jumlah.append(co[0])
			else:
				print(f'\r{x} ╚══ [ {m}•{x} ] Gagal mengonfirmasi, '+co[0])

		if 'Lihat selengkapnya' in get:
			konfirmasi(soup(get, "html.parser").find("a", string="Lihat selengkapnya").get("href"))
		elif 'Tidak ada permintaan' in get:
			print(f'\r{x} ╚══ [ {m}•{x} ] Tidak Ada permintaan Pertemanan')
		else:
			pass
	except:pass

# KOMEN BERANDA
def komen(tar):
	try:
		sasi = ["oyo","Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
		now = datetime.now();hari = now.day;blx = now.month;bulan = sasi[blx];tahun = now.year;tanggal = str(hari)+' - '+str(bulan)+' - '+str(tahun);jam = now.hour;menit = now.minute;detik = now.second;hari1 = now.strftime("%A")
		date = '\n\n [ '+str(hari1)+', '+str(tanggal)+' ] [ Pukul, '+str(jam)+' : '+str(menit)+', '+str(detik)+' ]'
		url = tar
		cook = open('.cookie.txt','r').read()
		get = ses.get(url,cookies={'cookie':cook}).text
		al = re.findall('Suka\<\/a\>\<span\>\ · \<\/span\>\<a\ href\=\"(.*?)\"\>Tanggapi\<\/a\>\<\/span\>\<span\>\ ·\ <\/span\>\<a\ href\=\"(.*?)\"\>',get)
		for pisah in al:
			try:
				jajan.append(pisah[1])
				print(f'\r{x} ═══[ {h}•{x} ] Postingan ke,{h} {len(jajan)} {x}      ')
				if '1' in pasi:
					try:
						urll = 'https://mbasic.facebook.com'+pisah[0]
						post = ses.get(urll,cookies={'cookie':cook}).text
						dic = {'1':'tanggapan\<\/h1\>','2':'Suka','3':'Super','4':'Peduli','5':'Haha','6':'Wow','7':'Sedih'}
						au = (dic[random.choice(reac)])
						if 'Wow' in post:
							target = re.findall(f'{au}\<\/span\>\<\/td\>(.*?)\<a\ href\=\"(.*?)\"\ style\=',post)
							for ok in target:
								uri = 'https://mbasic.facebook.com'+ok[1].replace('amp;','')
								gas = ses.get(uri,cookies={'cookie':cook})
								if '<Response [200]>' in str(gas):
									dic = {'1':'Suka','2':'Super','3':'Peduli','4':'Haha','5':'Wow','6':'Sedih','7':'Marah'}
									ae = (dic[random.choice(reac)])
									print(f'\r{x} ╚══[ {h}•{x} ] Berhasil menanggapi, [{h} {ae} {x}] postingan')
									sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 10 detik');sys.stdout.flush()
								time.sleep(10)
								
						else:
							pass
					except:pass

				else:
					pass
				if '1' in commen:
					pass
				else:
					try:
						if 'https://mbasic.facebook.com' in pisah[1]:
							tes = pisah[1].replace('amp;','')
							urlk = tes.split('"')[0]
						else:
							urlk = 'https://mbasic.facebook.com'+pisah[1].replace('amp;','')
						req = ses.get(urlk,cookies={'cookie':cook}).text
						par = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"\>\<input',req)
						ok = soup(req,'html.parser')
						fom = ok.find('form',{'method':'post'})
						text = random.choice(tulis)
						if 'Komentar di buat pada' in str(req):
							print(f'\r{x} ╚══[ {m}•{x} ] postingan ini sudah di komentari')
							print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
						elif 'Anda Diblokir Sementara' in str(req):
							print(f'\r{x} ╚══[ {m}•{x} ] Anda di larang berkomentar untuk sementara')
							print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
						else:
							dat = {
							'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
							'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
							'comment_text': f'{text}{date}',
							'submit' : 'Komentari'
							}
							header = {
							'initiator': 'https://mbasic.facebook.com',
							'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
							'accept-encoding': 'gzip, deflate, br',
							'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
							'content-type': 'application/x-www-form-urlencoded',
							'origin': 'https://mbasic.facebook.com',
							'referer': urlk,
							'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
							'sec-ch-ua-mobile': '?1',
							'sec-ch-ua-platform': '"Android"',
							'sec-fetch-dest': 'document',
							'sec-fetch-mode': 'navigate',
							'sec-fetch-site': 'same-origin',
							'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36'
							}
							ukr = 'https://mbasic.facebook.com'+par[0].replace('amp;','')
							post = ses.post(ukr,headers=header,data=dat,cookies={'cookie':cook})
							if '<Response [200]>' in str(post):
								print(f'\r{x} ╚══[ {h}•{x} ] Berhasil mengomentari postingan')
								print(f'\r{x} ╚══[ {h}•{x} ] Isi text :{h} {text}')
								print(f'\r{x} ╚══[ {h}•{x} ] Url post :{h} {urlk}')
								print(f'\r{x} ╚══[ {k}!{x} ] Lihat log aktifitas untuk info\n')
								sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 60 detik');sys.stdout.flush()
								time.sleep(60)
					except:
						print(f'\r{x} ╚══[ {m}!{x} ] Tidak ada akses untuk komentar\n')
			except:
				print(f'\r{x} ╚══[ {k}!{x} ] Getting Url Error\n')
		if 'Lihat Berita Lain' in get:
			target = soup(get, "html.parser").find("a", string='Lihat Berita Lain').get('href')
			komen('https://mbasic.facebook.com'+target)
		else:
			komen('https://mbasic.facebook.com/home.php')
	except:pass

# LOG AKTIFITAS
def logger(urll):
	try:
		banner()
		cook = open('.cookie.txt','r').read()
		url = 'https://mbasic.facebook.com'+urll
		post = ses.get(url,cookies={'cookie':cook}).text
		get = soup(post,'html.parser')
		sop = get.findAll('h3')
		open('wri.txt','w').write(post)
		for ok in sop:
			if 'Log Aktivitas' in ok.text:
				pass
			elif 'Filter' in ok.text:
				pass
			elif 'Arsip' in ok.text:
				pass
			elif 'Sampah' in ok.text:
				pass
			else:
				print(f'\r{x} ╚══[ {h}•{x} ] {ok.text}')
		pilih = input(f'\r{x} ╚══[ {k}!{x} ] Pilih [ y/t ] : ')
		if 'y' in pilih:
			sasi = ["oyo", "Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
			now = datetime.now();blx = now.month;bulan = sasi[blx]
			urll = get.find("a", string=f"Muat lebih banyak dari {str(bulan)}").get("href")
			logger(urll)
			print(f'\r{x} ╚══[ {k}!{x} ] Tidak ada lagi aktifitas\n')
			
		else:
			menu()
	except Exception as e:
		print(e)

# BOT PESAN
def pessan(urll):
	try:
		url = urll
		cook = open('.cookie.txt','r').read()
		get = ses.get(url,cookies={'cookie':cook}).text
		sasi = ["oyo","Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
		now = datetime.now();hari = now.day;blx = now.month;bulan = sasi[blx];tahun = now.year;tanggal = str(hari)+' - '+str(bulan)+' - '+str(tahun);jam = now.hour;menit = now.minute;detik = now.second;hari1 = now.strftime("%A")
		date = '\n\n[ by brutalID ]\n[ '+str(hari1)+', '+str(tanggal)+'/ '+str(jam)+' : '+str(menit)+', '+str(detik)+' ]'
		te = re.findall('table\>\<table\ class\=\".*?\"\>\<tr\>\<td\ class\=\".*?\"\>\<div\>\<h3\ class\=\".*?\"\>\<a\ href\=\"(.*?)\"\>(.*?)\<',get)
		for de in te:
			text = random.choice(tulis)
			pesan = text+date
			jajan.append(de[1])
			print(f'\r{x} ═══[ {h}•{x} ] Pesan ke,{h} {len(jajan)} {x}       ')
			try:
				ukl = 'https://mbasic.facebook.com'+de[0].replace('amp;','')
				uo = ses.get(ukl,cookies={'cookie':cook}).text
				par = re.findall('form\ method\=\"post\"\ action\=\"(.*?)\"',uo)
				ok = soup(uo,'html.parser')
				fom = ok.find('form',{'method':'post'})
				dat = {
				'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(fom)).group(1),
				'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(fom)).group(1),
				'body': f'{pesan}',
				'send' : 'Kirim',
				'tids' : re.search('name="tids" type="hidden" value="(.*?)"',str(fom)).group(1),
				'wwwupp' : re.search('name="wwwupp" type="hidden" value="(.*?)"',str(fom)).group(1),
				'platform_xmd': '',
				'referrer': '',
				'ctype': '',
				'cver' : re.search('name="cver" type="hidden" value="(.*?)"',str(fom)).group(1)
				}
				ukr = 'https://mbasic.facebook.com'+par[0].replace('amp;','')
				post = ses.post(ukr,data=dat,cookies={'cookie':cook})
				if '<Response [200]>' in str(post):
					text = '[green]Penerima[white] :[cyan] '+ de[1] + '\n[green]Pesan[white] :[cyan] ' + pesan + '[white]'
					pan = Panel(text,title='>[green] Succes[cyan] <',style="cyan")
					jalan(pan)
					sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 30 detik');sys.stdout.flush()
					time.sleep(30)
				else:
					print(f'\r{x} ╚══[ {m}!{x} ] Gagal Mengirim pesan \n')
			except:
				print(f'\r{x} ╚══[ {m}!{x} ] Tidak ada akses untuk mengirim pesan\n')
				sys.stdout.write(f'\r{x}  ══[ {k}!{x} ] Wait 30 detik');sys.stdout.flush()
				time.sleep(60)
		if 'Lihat Pesan Sebelumnya' in get:
			target = soup(get, "html.parser").find("a", string='Lihat Pesan Sebelumnya').get('href')
			pessan('https://mbasic.facebook.com'+target)
		else:
			print(f'\r{x} ╚══[ {k}!{x} ] Hei anda sudah mengirimi semua pesan yang ada di table\n')
	except Exception as e:
		print(e)


'''
try:
	get = ses.get('https://script.brutalid.repl.co').text
	if 'SCRIPT ON' in get:
		for i in tqdm(range(100), desc=Fore.GREEN + 'Loading...', ascii=False, ncols=65):
			time.sleep(0.03)
		menu()
	elif 'SCRIPT OF' in get:
		banner()
		print('script ini sudah di tutup oleh owner')
	else:
		print('Error')
except:pass'''

menu()
