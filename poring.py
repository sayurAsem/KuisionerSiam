#!/usr/bin/python
#developed by sayurAsem from FM Coder
#Developer tidak berniat untuk mengambil NIM dan Password anda, Tenang aja broh.
#Sourcecode dan aplikasi ini untuk belajar,
from BeautifulSoup import BeautifulSoup
import mechanize,cookielib


print '- - DEDICATED TO CALIPHATE FIGHTERS - -'

agree=raw_input('Boleh minta data diri (y/n)? ')
nama=''
nomor=''
if agree=='y':
    print 'Mohon Isi Nama dan Nomor Telepon/Line/Email/dll'
    nama=raw_input('Nama : ')
    nomor=raw_input('NoTelepon/Line/Email/dll : ')
    print 'Mohon Tunggu . . . '
    cookie=cookielib.CookieJar()
    driver = mechanize.Browser()
    driver.set_cookiejar(cookie)
    driver.set_handle_robots(False)
    driver.open('http://goo.gl/forms/OEJaqNovEY')
    driver.select_form(nr=0)
    driver.form['entry.1445991119']=nama
    driver.form['entry.756171490']=nomor
    driver.submit()
    print 'Syukran wa Barakallah, Sekarang silahkan gunakan aplikasi'

else :
    print 'Jika berubah pikiran, silahkan jalankan aplikasi untuk sekedar mengisi data'
    print 'Silahkan gunakan aplikasi'

print '\n\n========================================'
print 'Membuka siam.ub.ac.id, Tunggu Sebentar . . .'
cookie=cookielib.CookieJar()
driver = mechanize.Browser(factory=mechanize.RobustFactory())
driver.set_cookiejar(cookie)
driver.open('https://siam.ub.ac.id')
driver.select_form(nr=0)

cookie2=cookielib.CookieJar()
driver2 = mechanize.Browser(factory=mechanize.RobustFactory())
driver2.set_cookiejar(cookie2)
driver2.open('https://siam.ub.ac.id')
driver2.select_form(nr=0)

print 'Silahkan Login Siam '
NIM = raw_input('NIM : ')
Psswd=raw_input('Password (Usahakan anda sedang sendiri): ')
sarn=raw_input('Saran untuk semua dosen : ')

print 'proses Login . . .'
driver.form['username']=NIM
driver.form['password']=Psswd
driver.submit()
driver2.form['username']=NIM
driver2.form['password']=Psswd
driver2.submit()

print 'Menjalankan Tugas'
count=0
for link in driver.links(url_regex='kuisioner.php'):
    count+=1
    print 'Mengisi Kuisioner ke ',count
    tempLink='https://siam.ub.ac.id/'+link.url
    #print tempLink

    driver2.click_link(link)
    html_page = driver2.follow_link(link)

    #for a in driver2.forms():
    #    print a
    driver2.select_form(name="myForm")
    #driver2.form.set_all_readonly(False)
    soup = BeautifulSoup(html_page)
    #print soup
    angka = 0
    driver2['saran'] =sarn
    for row in soup.findAll('input', attrs={'value': 5 }):
        angka+=1
        print 'Checking Radio {nm}'.format(nm=angka)
        #print row
        #print driver2.form
        driver2.form['{nm}'.format(nm=angka)] =['5']
    #soup.find('textarea',attrs={'name':'saran'})

    print 'Proses Submit'
    driver2.submit()
    print 'done'






