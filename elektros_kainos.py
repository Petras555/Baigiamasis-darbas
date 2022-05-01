from duomenu_baze import Elektra, engine
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import ActionChains
import time
from sqlalchemy.orm import sessionmaker
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
from PIL import Image, ImageTk


def on_resize(event):
    image = bgimg.resize((event.width, event.height), Image.LANCZOS)
    l.image = ImageTk.PhotoImage(image)
    l.config(image=l.image)


def Istorija():
    boksas.delete(0, 'end')
    duomenys = session.query(Elektra).all()
    boksas.insert(END, *duomenys)


def laukimas():
    status['text'] = 'Prašome palaukti...'

def scrape_1lz():

###############Elektrum 1 laiko zona####################################################################################################
    url = 'https://www.elektrum.lt/lt/namams/elektra'

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(url)

    time.sleep(4)
    l = driver.find_element_by_id('ccc-notify-reject')
    l.click()

    driver.implicitly_wait(10)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    blokai = soup.find_all('div', {'class': "ss-price primary"})
    kainos = []
    for blokas in blokai:
        kaina = blokas.find('div', {'class': "price"}).text.strip()
        kainos.append(kaina)

    elektruml['text'] = kainos[0]


    for i in range(len(kainos)):
        imone = "Eleketrum"
        kaina = kainos[i] + " Eur/kWh "
        laiko_zonos = "1 laiko zona"
        if i == 0:
            planas = "Stabilus 36"
        if i == 1:
            planas = "Stabilus 24"
        if i == 2:
            planas = "Praktiškas"
        if i == 3:
            planas = "Stabilus +"

        pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
        session.add(pasiulymas)
        session.commit()

###############Ignitis 1 laiko zona####################################################################################################

    url = 'https://ignitis.lt/lt/nepriklausomo-tiekimo-kainos/planai'

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(url)

    time.sleep(4)
    f = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")
    f.click()

    driver.implicitly_wait(10)
    time.sleep(6)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    blokai = soup.find_all('div', {'class': "electricity-price-VK form-item js-electricity-price-VK"})
    kainos = []
    for blokas in blokai:
        kaina1 = blokas.find('em', {'class': "placeholder js-price-first"}).text.strip()
        kaina = kaina1.replace(',', '.')
        kainos.append(kaina)
    ignitisl['text'] = kainos[0]


    time.sleep(3)
    l = driver.find_element_by_xpath("//*[@id=\"edit-filters-plans-m-duration\"]/div[2]/div/label")
    ActionChains(driver).click(l).perform()

    time.sleep(2)
    soup2 = BeautifulSoup(driver.page_source, 'lxml')
    time.sleep(1)

    blokai2 = soup2.find_all('div', {'class': "electricity-price-VK form-item js-electricity-price-VK"})
    kainos2 = []
    for blokas in blokai2:
        kaina22 = blokas.find('em', {'class': "placeholder js-price-first"}).text.strip()
        kaina2 = kaina22.replace(',', '.')
        kainos2.append(kaina2)

    imone = "Ignitis"
    kaina = kainos[0] + " Eur/kWh "
    laiko_zonos = "1 laiko zona"
    planas = "18 mėn. fiksuotas planas"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()

    imone = "Ignitis"
    kaina = kainos2[0] + " Eur/kWh "
    laiko_zonos = "1 laiko zona"
    planas = "12 mėn. fiksuotas planas"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()

###############Perlas 1 laiko zona####################################################################################################

    url = 'https://perlasenergija.lt/#skaiciuokle'

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)

    driver.get(url)

    driver.implicitly_wait(10)
    time.sleep(6)

    soup3 = BeautifulSoup(driver.page_source, 'lxml')

    blokai3 = soup3.find_all('div', {'class': "col-12 col-md-4 mb-3 mb-md-0 d-flex"})
    kainos = []
    for blokas in blokai3:
        kaina3 = blokas.find('div', {'class': "price-tag"}).text.strip()
        kainos.append(kaina3)

    kaina_fixed = kainos[0].replace('Eur/kWh', '')
    perlasl['text'] = kaina_fixed

    imone = "Perlas"
    kaina = kainos[0]
    laiko_zonos ="1 laiko zona"
    planas = "Standartinis"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()



    imone = "####################################"
    kaina = "####################################"
    laiko_zonos = "####################################"
    planas = "####################################"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()



    status['text'] = 'Kainos paskaičiuotos!(Vienai laiko zononai)'


def scrape_2lz():

###############Elektrum 2 laiko zonos####################################################################################################

    url = 'https://www.elektrum.lt/lt/namams/elektra'
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(url)

    time.sleep(4)
    l = driver.find_element_by_id('ccc-notify-reject')
    l.click()

    time.sleep(2)
    l = driver.find_element_by_id('timezone2')
    l.click()

    driver.implicitly_wait(10)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    blokai = soup.find_all('div', {'class': "ss-price primary"})
    kainos = []
    for blokas in blokai:
        kaina = blokas.find('div', {'class': "price"}).text.strip()
        kainos.append(kaina)

    elektruml_2lz_diena['text'] = kainos[0]
    elektruml_2lz_naktis['text'] = kainos[1]

    for i in range(len(kainos)):

        if i == 0:
            imone = "Eleketrum"
            kaina = kainos[i] + " Eur/kWh:Dieninis; " + kainos[i+1] + " Eur/kWh:Naktinis, "
            laiko_zonos = "2 laiko zonos"
            planas = "Stabilus 36"

            pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
            session.add(pasiulymas)
            session.commit()
        if i == 2:
            imone = "Eleketrum"
            kaina = kainos[i] + " Eur/kWh:Dieninis; " + kainos[i + 1] + " Eur/kWh:Naktinis, "
            laiko_zonos = "2 laiko zonos"
            planas = "Stabilus 24"

            pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
            session.add(pasiulymas)
            session.commit()
        if i == 4:
            imone = "Eleketrum"
            kaina = kainos[i] + " Eur/kWh:Dieninis; " + kainos[i + 1] + " Eur/kWh:Naktinis, "
            laiko_zonos = "2 laiko zonos"
            planas = "Praktiskas"

            pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
            session.add(pasiulymas)
            session.commit()
        if i == 6:
            imone = "Eleketrum"
            kaina = kainos[i] + " Eur/kWh:Dieninis; " + kainos[i + 1] + " Eur/kWh:Naktinis, "
            laiko_zonos = "2 laiko zonos"
            planas = "Stabilus +"

            pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
            session.add(pasiulymas)
            session.commit()

###############Ignitis 2 laiko zonos####################################################################################################

    url = 'https://ignitis.lt/lt/nepriklausomo-tiekimo-kainos'

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get(url)

    time.sleep(3)
    f = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection")
    f.click()

    time.sleep(1)
    f = driver.find_element_by_xpath("//*[@id=\"edit-time-zone\"]/div[2]/div/label[1]/div")
    f.click()

    time.sleep(1)
    f = driver.find_element_by_xpath("//*[@id=\"edit-submit\"]")
    f.click()

    driver.implicitly_wait(5)
    time.sleep(3)

    diena_18 = driver.find_element_by_xpath("//*[@id=\"edit-m\"]/div[2]/div[5]/div[1]/div[2]/div[1]/label[2]/em").text
    naktis_18 = driver.find_element_by_xpath("//*[@id=\"edit-m\"]/div[2]/div[5]/div[1]/div[2]/div[2]/label[2]/em").text

    diena_18_fixed = diena_18.replace(',', '.')
    naktis_18_fixed = naktis_18.replace(',', '.')

    ignitisl_2lz_diena['text'] = diena_18_fixed
    ignitisl_2lz_naktis['text'] = naktis_18_fixed

    imone = "Ignitis"
    kaina = diena_18 + " Eur/kWh:Dieninis; " + naktis_18 + " Eur/kWh:Naktinis, "
    laiko_zonos = "2 laiko zonos"
    planas = "18 mėn. fiksuotas planas"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()

    time.sleep(2)
    p = driver.find_element_by_xpath("//*[@id=\"edit-filters-plans-m-duration\"]/div[2]/div/label")
    ActionChains(driver).click(p).perform()
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    blokas = soup.find('div', {'class': "price-types"}).text.strip()
    kainos = []
    blokas1 = blokas.replace('Eur/kWh', '')
    blokas2 = blokas1.replace('0,000', '')
    blokas3 = blokas2.replace('\n', '')

    kainos.append(blokas3[0:5])
    kainos.append(blokas3[5:10])

    imone = "Ignitis"
    kaina = kainos[0] + " Eur/kWh:Dieninis; " + kainos[1] + " Eur/kWh:Naktinis, "
    laiko_zonos = "2 laiko zonos"
    planas = "12 mėn. fiksuotas planas"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()

###############Perlas 2 laiko zonos####################################################################################################

    url = 'https://perlasenergija.lt/#skaiciuokle'

    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)

    driver.get(url)

    driver.implicitly_wait(10)
    time.sleep(4)

    p = driver.find_element_by_xpath("//*[@id=\"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowallSelection\"]")
    p.click()
    time.sleep(1)

    l = driver.find_element_by_xpath("//*[@id=\"plans-block\"]/div/div[1]/div/div[2]")

    ActionChains(driver).click(l).perform()
    time.sleep(3)

    soup3 = BeautifulSoup(driver.page_source, 'lxml')

    blokai3 = soup3.find_all('div', {'class': "row flex-grow-1 d-none d-md-flex"})
    kainos = []

    for blokas in blokai3:
        kaina3 = blokas.find_all('div', {'class': "price-tag"})
        for i in kaina3:
            kainos.append(i.text.strip())
        # print(blokas.text)


    kaina_fixed1 = kainos[0].replace('Eur/kWh', '')
    kaina_fixed2 = kainos[1].replace('Eur/kWh', '')
    perlasl_2lz_diena['text'] = kaina_fixed1
    perlasl_2lz_naktis['text'] = kaina_fixed2

    imone = "Perlas"
    kaina = kainos[0] + " Eur/kWh:Dieninis; " + kainos[1] + " Eur/kWh:Naktinis, "
    laiko_zonos = "2 laiko zonos"
    planas = "Standartinis"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()


    imone = "####################################"
    kaina = "####################################"
    laiko_zonos = "####################################"
    planas = "####################################"

    pasiulymas = Elektra(imone, kaina, laiko_zonos, planas)
    session.add(pasiulymas)
    session.commit()


    status['text'] = 'Kainos paskaičiuotos!(Dviems laiko zonoms)'


def skaiciuoti_1lz():
    try:
        suvartojimas = float(suvartojimas_1lz.get())
    except:
        skaiciuokle_status['text'] = "Klaida:(Blogai įvestas suvartojimas)"
        return

    try:


        ign_1lz = float(ignitisl['text'])
        skaiciuokle_ignitisl['text'] = round((ign_1lz * suvartojimas), 2)

        elek_1lz = float(elektruml['text'])
        skaiciuokle_elektruml ['text'] = round((elek_1lz * suvartojimas), 2)

        perl_1lz = float(perlasl['text'])
        skaiciuokle_perlasl['text'] = round((perl_1lz * suvartojimas), 2)

        skaiciuokle_status['text'] = "Paskaičiuota 1 laiko zonos galutinė suma"
    except:
        skaiciuokle_status['text'] = "Klaida:(Tikriausiai neatlikote kainų paieškos)"
        return

def skaiciuoti_2lz_diena():
    try:
        suvartojimas = float(suvartojimas_2lz_diena.get())
    except:
        skaiciuokle_status['text'] = "Klaida:(Blogai įvestas suvartojimas)"
        return

    try:
        ign = float(ignitisl_2lz_diena['text'])
        skaiciuokle_ignitisl_2lz_diena['text'] = round((ign * suvartojimas), 2)

        elek = float(elektruml_2lz_diena['text'])
        skaiciuokle_elektruml_2lz_diena['text'] = round((elek * suvartojimas), 2)

        perl = float(perlasl_2lz_diena['text'])
        skaiciuokle_perlasl_2lz_diena['text'] = round((perl * suvartojimas), 2)
        skaiciuokle_status['text'] = "Paskaičiuota 2 laiko zonų dienos galutinė suma"
    except:
        skaiciuokle_status['text'] = "Klaida:(Tikriausiai neatlikote kainų paieškos)"
        return

def skaiciuoti_2lz_nakti():
    try:
        suvartojimas = float(suvartojimas_2lz_naktis.get())
    except:
        skaiciuokle_status['text'] = "Klaida:(Blogai įvestas suvartojimas)"
        return

    try:
        ign = float(ignitisl_2lz_naktis['text'])
        skaiciuokle_ignitisl_2lz_naktis['text'] = round((ign * suvartojimas), 2)

        elek = float(elektruml_2lz_naktis['text'])
        skaiciuokle_elektruml_2lz_naktis['text'] = round((elek * suvartojimas), 2)

        perl = float(perlasl_2lz_naktis['text'])
        skaiciuokle_perlasl_2lz_naktis['text'] = round((perl * suvartojimas), 2)
        skaiciuokle_status['text'] = "Paskaičiuota 2 laiko zonų nakties galutinė suma"
    except:
        skaiciuokle_status['text'] = "Klaida:(Tikriausiai neatlikote kainų paieškos)"
        return


def uzdaryti():
    langas.destroy()


options = ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")

options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--headless")

Session = sessionmaker(bind=engine)
session = Session()
langas = Tk()

langas.configure(background='orange')
bgimg = Image.open('img.png') # load the background image
l = Label(langas)
l.place(x=0, y=0, relwidth=1, relheight=1) # make label l to fit the parent window always
l.bind('<Configure>', on_resize) # on_resize will be executed whenever label l is resized


langas.title("Kainu skaiciuokle")
langas.geometry('750x500')
langas.iconbitmap(r'flash.ico')

notebook = ttk.Notebook(langas)
dabartines_kainos = Frame(notebook)
kainu_istorija = Frame(notebook)
skaiciuokle = Frame(notebook)



notebook.add(dabartines_kainos, text="Dabartinės kainos")
notebook.add(kainu_istorija, text="Kainų istorija")
notebook.add(skaiciuokle, text="Skaičiuoklė")



notebook.pack()








titline = Label(dabartines_kainos, text="Raskite Optimaliausias elektros tiekėjų kainos")
ignitis = Label(dabartines_kainos, text="Ignitis: ")
ignitisl = Label(dabartines_kainos)
ignitisl_2lz_diena = Label(dabartines_kainos)
ignitisl_2lz_naktis = Label(dabartines_kainos)
ign_eu_kwh1 = Label(dabartines_kainos, text="Eur/kWh")
ign_eu_kwh2diena = Label(dabartines_kainos, text="Eur/kWh")
ign_eu_kwh2naktis = Label(dabartines_kainos, text="Eur/kWh")
elektrum = Label(dabartines_kainos, text="Elektrum: ")
elektruml = Label(dabartines_kainos)
elektruml_2lz_diena = Label(dabartines_kainos)
elektruml_2lz_naktis = Label(dabartines_kainos)
elek_eu_kwh1 = Label(dabartines_kainos, text="Eur/kWh")
elek_eu_kwh2diena = Label(dabartines_kainos, text="Eur/kWh")
elek_eu_kwh2naktis = Label(dabartines_kainos, text="Eur/kWh")
perlas = Label(dabartines_kainos, text="Perlas: ")
perlasl = Label(dabartines_kainos)
perlasl_2lz_diena = Label(dabartines_kainos)
perlasl_2lz_naktis = Label(dabartines_kainos)
perl_eu_kwh1 = Label(dabartines_kainos, text="Eur/kWh")
perl_eu_kwh2diena = Label(dabartines_kainos, text="Eur/kWh")
perl_eu_kwh2naktis = Label(dabartines_kainos, text="Eur/kWh")
mygtukas2 = Button(dabartines_kainos, text="2 laiko zonų", command=scrape_2lz)
mygtukas1 = Button(dabartines_kainos, text="1 laiko zonos", command=scrape_1lz)
tarifai_l =Label(dabartines_kainos, text="Laiko zonos: ")
viena_lz= Label(dabartines_kainos, text="Viena laiko zona")
dvi_lz_diena= Label(dabartines_kainos, text="Dvi laiko zonos\nDieninis tarifas")
dvi_lz_naktis= Label(dabartines_kainos, text="Dvi laiko zonos\nNaktinis tarifas")
status = Label(dabartines_kainos, text="Pasirinkite kelių laiko zonų kainas norite skaičiuoti", bd=1, relief=SUNKEN, anchor=W)

titline_2 = Label(kainu_istorija, text="Kainų istorija")
boksas = Listbox(kainu_istorija, selectmode=SINGLE, width=100)
istorijos_button = Button(kainu_istorija, text="Rodyti istorija", command=Istorija)

skaiciuokle_titline = Label(skaiciuokle, text="Elektros tiekėjų kainos")
skaiciuokle_ignitis = Label(skaiciuokle, text="Ignitis: ")
skaiciuokle_ignitisl = Label(skaiciuokle)
skaiciuokle_ignitisl_2lz_diena = Label(skaiciuokle)
skaiciuokle_ignitisl_2lz_naktis = Label(skaiciuokle)
skaiciuokle_ign_eu_kwh1 = Label(skaiciuokle, text="Eur")
skaiciuokle_ign_eu_kwh2diena = Label(skaiciuokle, text="Eur")
skaiciuokle_ign_eu_kwh2naktis = Label(skaiciuokle, text="Eur")
skaiciuokle_elektrum = Label(skaiciuokle, text="Elektrum: ")
skaiciuokle_elektruml = Label(skaiciuokle)
skaiciuokle_elektruml_2lz_diena = Label(skaiciuokle)
skaiciuokle_elektruml_2lz_naktis = Label(skaiciuokle)
skaiciuokle_elek_eu_kwh1 = Label(skaiciuokle, text="Eur")
skaiciuokle_elek_eu_kwh2diena = Label(skaiciuokle, text="Eur")
skaiciuokle_elek_eu_kwh2naktis = Label(skaiciuokle, text="Eur")
skaiciuokle_perlas = Label(skaiciuokle, text="Perlas: ")
skaiciuokle_perlasl = Label(skaiciuokle)
skaiciuokle_perlasl_2lz_diena = Label(skaiciuokle)
skaiciuokle_perlasl_2lz_naktis = Label(skaiciuokle)
skaiciuokle_perl_eu_kwh1 = Label(skaiciuokle, text="Eur")
skaiciuokle_perl_eu_kwh2diena = Label(skaiciuokle, text="Eur")
skaiciuokle_perl_eu_kwh2naktis = Label(skaiciuokle, text="Eur")
skaiciuokle_mygtukas2 = Button(skaiciuokle, text="2 laiko zonų", command=scrape_2lz)
skaiciuokle_mygtukas1 = Button(skaiciuokle, text="1 laiko zonos", command=scrape_1lz)
skaiciuokle_tarifai_l =Label(skaiciuokle, text="Laiko zonos: ")
skaiciuokle_viena_lz= Label(skaiciuokle, text="Viena laiko zona")
skaiciuokle_dvi_lz_diena= Label(skaiciuokle, text="Dvi laiko zonos\nDieninis tarifas")
skaiciuokle_dvi_lz_naktis= Label(skaiciuokle, text="Dvi laiko zonos\nNaktinis tarifas")
skaiciuokle_status = Label(skaiciuokle, text="Paskaičiuokite galutinę sumą pagal jūsų suvartojimą", bd=1, relief=SUNKEN, anchor=W)
suvartojimas_1lz = Entry(skaiciuokle)
suvartojimas_2lz_diena = Entry(skaiciuokle)
suvartojimas_2lz_naktis = Entry(skaiciuokle)
label_suvartojimas_1lz = Label(skaiciuokle, text="1-os laiko zonos suvartojimas")
label_suvartojimas_2lz_diena = Label(skaiciuokle, text="2-jų laiko zonų dienos suvartojimas" )
label_suvartojimas_2lz_naktis = Label(skaiciuokle, text="2-jų laiko zonų nakties suvartojimas")
mygtukas_skaiciavimui_1 = Button(skaiciuokle, text='Skaičiuoti', command=skaiciuoti_1lz)
mygtukas_skaiciavimui_2 = Button(skaiciuokle, text='Skaičiuoti', command=skaiciuoti_2lz_diena)
mygtukas_skaiciavimui_3 = Button(skaiciuokle, text='Skaičiuoti', command=skaiciuoti_2lz_nakti)




titline.grid(row=0, column=0, columnspan=2)
tarifai_l.grid(row=1, column=0)
viena_lz.grid(row=1, column=1)
dvi_lz_diena.grid(row=1, column=3)
dvi_lz_naktis.grid(row=1, column=5)
ignitis.grid(row=2, column=0)
ignitisl.grid(row=2, column=1)
ignitisl_2lz_diena.grid(row=2, column=3)
ignitisl_2lz_naktis.grid(row=2, column=5)
ign_eu_kwh1.grid(row=2, column=2)
ign_eu_kwh2diena.grid(row=2, column=4)
ign_eu_kwh2naktis.grid(row=2, column=6)
elektrum.grid(row=3, column=0)
elektruml.grid(row=3, column=1)
elektruml_2lz_diena.grid(row=3, column=3)
elektruml_2lz_naktis.grid(row=3, column=5)
elek_eu_kwh1.grid(row=3, column=2)
elek_eu_kwh2diena.grid(row=3, column=4)
elek_eu_kwh2naktis.grid(row=3, column=6)
perlas.grid(row=4, column=0)
perlasl.grid(row=4, column=1)
perlasl_2lz_diena.grid(row=4, column=3)
perlasl_2lz_naktis.grid(row=4, column=5)
perl_eu_kwh1.grid(row=4, column=2)
perl_eu_kwh2diena.grid(row=4, column=4)
perl_eu_kwh2naktis.grid(row=4, column=6)
mygtukas2.grid(row=7, column=1)
mygtukas1.grid(row=7, column=0)
status.grid(row=8, columnspan=2, sticky=W+E)


titline_2.grid(row=0, columnspan=2)
boksas.grid(row=1, columnspan=1)
istorijos_button.grid(row=2, columnspan=2)
istorijos_button.bind('<Button>', )


skaiciuokle_titline.grid(row=0, column=0)
skaiciuokle_tarifai_l.grid(row=1, column=0)
skaiciuokle_viena_lz.grid(row=1, column=1)
skaiciuokle_dvi_lz_diena.grid(row=1, column=3)
skaiciuokle_dvi_lz_naktis.grid(row=1, column=5)
skaiciuokle_ignitis.grid(row=2, column=0)
skaiciuokle_ignitisl.grid(row=2, column=1)
skaiciuokle_ignitisl_2lz_diena.grid(row=2, column=3)
skaiciuokle_ignitisl_2lz_naktis.grid(row=2, column=5)
skaiciuokle_ign_eu_kwh1.grid(row=2, column=2)
skaiciuokle_ign_eu_kwh2diena.grid(row=2, column=4)
skaiciuokle_ign_eu_kwh2naktis.grid(row=2, column=6)
skaiciuokle_elektrum.grid(row=3, column=0)
skaiciuokle_elektruml.grid(row=3, column=1)
skaiciuokle_elektruml_2lz_diena.grid(row=3, column=3)
skaiciuokle_elektruml_2lz_naktis.grid(row=3, column=5)
skaiciuokle_elek_eu_kwh1.grid(row=3, column=2)
skaiciuokle_elek_eu_kwh2diena.grid(row=3, column=4)
skaiciuokle_elek_eu_kwh2naktis.grid(row=3, column=6)
skaiciuokle_perlas.grid(row=4, column=0)
skaiciuokle_perlasl.grid(row=4, column=1)
skaiciuokle_perlasl_2lz_diena.grid(row=4, column=3)
skaiciuokle_perlasl_2lz_naktis.grid(row=4, column=5)
skaiciuokle_perl_eu_kwh1.grid(row=4, column=2)
skaiciuokle_perl_eu_kwh2diena.grid(row=4, column=4)
skaiciuokle_perl_eu_kwh2naktis.grid(row=4, column=6)
suvartojimas_1lz.grid(row=8, column=1)
label_suvartojimas_1lz.grid(row=8, column=0)
mygtukas_skaiciavimui_1.grid(row=8, column=2)
suvartojimas_2lz_diena.grid(row=9, column=1)
label_suvartojimas_2lz_diena.grid(row=9, column=0)
mygtukas_skaiciavimui_2.grid(row=9, column=2)
suvartojimas_2lz_naktis.grid(row=10, column=1)
label_suvartojimas_2lz_naktis.grid(row=10, column=0)
mygtukas_skaiciavimui_3.grid(row=10, column=2)
skaiciuokle_status.grid(row=15, columnspan=2, sticky=W+E)



langas.bind("<Escape>", lambda event: uzdaryti())
langas.mainloop()