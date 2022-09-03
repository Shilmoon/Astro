from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
import json
from data import zatmeniya
import JestcoNavalilZadach as SOLUTIONS
from selenium.webdriver.common.action_chains import ActionChains
from data import galaktiki

with open("data.json", "r") as read_file:
    data = json.load(read_file)

zvezdi_sozvezdiya = {'Дубхе': 'Большая Медведица', 'Вега': 'Лира', 'Альдебаран': 'Телец', 'Бетельгейзе': 'Орион',
                     'Мерак': 'Большая Медведица', "Кастор": "Близнецы", "Антарес": "Скорпион", "Поллукс": "Близнецы",
                     "Арктур": "Волопас", "Регул": "Лев", "Ригель": "Орион", "Капелла": "Возничий",
                     "Полярная": "Малая Медведица", "Спика": "Дева", "Денеб": "Лебедь", "Алькаид": "Большая Медведица",
                     "Альтаир": "Орёл", "Процион": "Малый Пёс"}
dati_sozvezdiya = {'5 ноября': 'Весы', '1 апреля': "Рыбы", "15 ноября": "Весы", "1 июля": "Близнецы",
                   "1 октября": "Дева", "1 августа": "Рак", "10 декабря": "Змееносец", "25 ноября": "Скорпион",
                   "1 мая": "Овен", "20 мая": "Телец", "1 сентября": "Лев", "25 июня": "Близнецы", "15 октября": "Дева",
                   "12 апреля": "Рыбы", "1 июня": "Телец", "1 января": "Стрелец", "20 марта": "Рыбы",
                   "15 августа": "Лев", "1 марта": "Водолей", "15 июля": "Близнецы", "1 декабря": "Змееносец",
                   "21 сентября": "Дева", '15 января': "Стрелец", "1 февраля": "Козерог"}
polushar_sozv = {'Стрелец': "Южное полушарие", 'Овен': "Северное полушарие", "Орион": "Экваториальное",
                 "Змееносец": "Экваториальное", "Дева": "Экваториальное", "Лев": "Северное полушарие",
                 "Козерог": "Южное полушарие", "Рыбы": "Экваториальное", "Близнецы": "Северное полушарие",
                 "Водолей": "Южное полушарие", "Скорпион": "Южное полушарие", "Телец": "Северное полушарие"}
objectc_velich = {"Вега": "0,0ᵐ", "Венера в максимуме яркости": "–4,5ᵐ", "Уран в максимуме яркости": "+5,3ᵐ",
                  "Предел для современных телескопов": "+34ᵐ", "Плутон в максимуме яркости": "+13,6ᵐ",
                  "Предел для невооружённого глаза": "+6ᵐ", "Сириус": "–1,4ᵐ", "Луна в полнолуние": "–12,8ᵐ",
                  "Полярная": "+2,0ᵐ", "Солнце": "–26,7ᵐ", "Марс в максимуме яркости": "–2,9ᵐ", }
objectc_razmer = {"Меркурий": "5 тыс. км", "Титан (спутник Сатурна)": "5 тыс. км", "Уран": "50 тыс. км",
                  "Сатурн": "116 тыс. км", "Комета Галлея": "11 км", "Земля": "12,7 тыс. км", "Венера": "12,1 тыс. км",
                  "Марс": "6,8 тыс. км", "Луна": "3,5 тыс. км", "Юпитер": "140 тыс. км",
                  "Ганимед (спутник Юпитера)": "5 тыс. км", "Солнце": "1,4 млн км", "Нептун": "50 тыс. км",
                  "Плутон": "2,4 тыс. км"}
objectc_rast = {"Нептун": "30 а.е.", "Ближайшая звезда (альфа Центавра C)": "270 тыс. а.е.", "Пояс Койпера": "50 а.е.",
                "Венера": "0,7 а.е.", "Уран": "19,2 а.е.", "Земля": "1 а.е.", "Сатурн": "9,5 а.е.",
                "Главный пояс астероидов": "3 а.е.", "Юпитер": "5,2 а.е.", "Плутон": "39 а.е.", "Марс": "1,4 а.е.",
                "Меркурий": "0,4 а.е.", "Аппарат «Вояджер-1»": "150 а.е."}
objectc_napravl = {"Луна вокруг Земли": "Против часовой стрелки", "Солнце вокруг своей оси": "Против часовой стрелки",
                   "Меркурий вокруг Солнца": "Против часовой стрелки",
                   "Большинство астероидов": "Против часовой стрелки", "Сатурн вокруг Солнца": "Против часовой стрелки",
                   "Венера вокруг Солнца": "Против часовой стрелки", "Земля вокруг Солнца": "Против часовой стрелки",
                   "Уран вокруг Солнца": "Против часовой стрелки"}
spectr_zv = {"бело-голубой": "B", "красный": "M", "белый": "A", "жёлтый": "G", "голубой": "O", "бело-жёлтый": "F",
             "оранжевый": "K"}
temp_zv = {"6200": 'F', "8000": 'A', "3000": 'M', "20000": 'B', "3700": 'K'}
tip_gal = {"неправильные": 'I', "спиральные с перемычкой": 'SB', "линзовидные": 'S0', "эллиптические": 'E',
           "сферические": 'E0', "спиральные без перемычки": 'S'}
rad_zv = ("красный карлик", "жёлтая звезда главной последовательности", "голубой гигант", "красный сверхгигант",
          "оранжевый гипергигант")
spectr_c = ['O', "B", 'A', 'F', 'G', 'K', 'M']
# proxy = input('Введите прокси')
# port = input('Введите порт прокси')
# proxy_login = input('Введите логин прокси')
# proxy_password = input('Введите пароль прокси')

# options = {mabinon255@ulforex.com
# mepapos680@rxcay.com
# vacicir970@otodir.com
# sageb90384@lurenwu.com
# Bhbyjxrf14@
#    'proxy': {
#        'http': f'http://{proxy_login}:{proxy_password}@{proxy}:{port}',
#        'https': f'https://{proxy_login}:{proxy_password}@{proxy}:{port}',
#        'no_proxy': 'localhost,127.0.0.1'
#    }
# }
# driver = webdriver.Chrome('/home/jhon/PycharmProjects/Astro/chromedriver',seleniumwire_options=options)
driver = webdriver.Chrome('/home/jhon/PycharmProjects/Astro/chromedriver')
driver.get('https://astroschools.ru/moodle/login/index.php')
login = 'lefid45553@seinfaq.com'
password = 'Bhbyjxrf14@'
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(login)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()


def toggle_tasks():
    driver.get('https://astroschools.ru/moodle/course/view.php?id=4')
    s = driver.find_elements(By.CLASS_NAME, 'togglecompletion')
    for i in s:
        i.click()


def autocompletion_tasks():
    driver.get('https://astroschools.ru/moodle/course/view.php?id=4')
    s = driver.find_elements(By.CLASS_NAME, 'activityinstance')
    print(len(s))
    links = []
    links.pop()
    for i in s:
        links.append((i.find_element(By.XPATH, ".//*").get_attribute('href')))
    for d in links:
        driver.get(d)


def phototasks_firstcourse(i):
    img = driver.find_element(By.XPATH, f'//*[@id="q{str(i)}"]/div[2]/div/div[1]/img').get_attribute('src')
    name = img[img.rfind('/') + 1:img.rfind('.')]
    if '-' in name:
        name = name[name.find('-') + 1:]
    driver.find_element(By.XPATH, f'//*[@id="q{str(i)}"]/div[2]/div/div[2]').find_element(By.CLASS_NAME,
                                                                                          'answer').find_element(
        By.CLASS_NAME, 'form-control').send_keys(name)


def photooick_tasks(dictation, i):
    pht_name = driver.find_element(By.XPATH,
                                   f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[1]/p['
                                   f'3]/img').get_attribute(
        'src')
    print(pht_name)
    pht_name = pht_name[pht_name.rfind('/') + 1:]
    for d in range(1, 9):
        s = driver.find_element(By.XPATH,
                                f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/div[2]/div[{d}]/label').text
        if '.' in s:
            s = s[s.find('.') + 2:]
        if dictation.get(pht_name) == s:
            driver.find_element(By.XPATH,
                                f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/div[2]/div[{d}]/label').click()
            break


def multichoice(dictation, i):
    pht_name = driver.find_element(By.XPATH,
                                   f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[1]/p/img').get_attribute(
        'src')
    pht_name = pht_name[pht_name.rfind('/') + 1:]
    elem_len = len(driver.find_element(By.XPATH,f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/div[2]').find_elements(By.TAG_NAME,'div'))
    ass = 0
    for d in range(1, elem_len + 1):
        ass += 1
        s = driver.find_element(By.XPATH,
                                f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/div[2]/div[{d}]/label').text
        if dictation.get(pht_name) == s:
            driver.find_element(By.XPATH,
                                f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/div[2]/div[{d}]/input').click()
            break
        else:
            if ass == 4:
                print(f'Вопрос номер {i}')
                print(pht_name)
                print(s)


def draganddrop(lists, i):
    items = driver.find_element(By.XPATH,
                                f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/div/ul').find_elements(
        By.CLASS_NAME, 'sortableitem')
    for s in items:
        action = ActionChains(driver)
        source = s
        dest = driver.find_element(By.XPATH,
                                   f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/div/ul/li[{lists.index(s.text) + 1}]')
        action.drag_and_drop(source, dest).perform()


def selectask(dictation, i):
    d = driver.find_element(By.XPATH, f'//*[@id="q{i}"]/div[2]/div/div[2]/table/tbody').find_elements(By.TAG_NAME, 'tr')
    print((d))
    for s in range(1, len(d) + 1):
        f = s
        name = driver.find_element(By.XPATH,
                                   f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/table/tbody/tr[{f}]/td[1]').text

        select_object = Select(driver.find_element(By.XPATH,
                                                   f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/table/tbody/tr[{f}]/td[2]/select'))
        print(name)
        select_object.select_by_visible_text(dictation.get(name))


def gapselect(i):
    text = driver.find_element(By.XPATH,
                               f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[1]/p').text
    text = text[:text.find('\n')]
    d = driver.find_element(By.XPATH,
                            f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[1]/p').find_elements(
        By.TAG_NAME,
        'span')
    first = 1
    len_d = len(d)
    try:
        if driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div['
                                     f'1]/p/span[{1}]/select').text == '':
            first = 2
    except Exception:
        first = 2
    for num in range(first, len(d) + 1):
        select_object = Select(driver.find_element(By.XPATH,
                                                   f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[1]/p/span[{num}]/select'))
        if first == 2:
            select_object.select_by_visible_text(data.get(text)[num - 2])
        else:
            select_object.select_by_visible_text(data.get(text)[num - 1])


def finish_test(q_answ):
    id = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/section/div/form').find_element(By.XPATH,
                                                                                                      './/*').get_attribute(
        'id')
    driver.find_element(By.XPATH, f'//*[@id="{id}"]/div[{str(len(q_answ) + 1)}]').find_element(By.XPATH, './/*').click()
    driver.find_element(By.XPATH, '//*[@id="region-main"]/div/div[3]/div/div/form').find_element(By.XPATH,
                                                                                                 './/*').find_element(
        By.XPATH, './/*').click()
    time.sleep(1)
    button_id = driver.find_element(By.XPATH, '//*[@id="page-mod-quiz-summary"]').find_element(By.XPATH,
                                                                                               r'//div[@class="moodle-dialogue-base moodle-dialogue-confirm"]').find_element(
        By.XPATH,
        r'//div[@class="yui3-widget yui3-panel moodle-dialogue yui3-widget-positioned yui3-widget-modal yui3-widget-stacked moodle-has-zindex moodle-dialogue-focused"]').find_element(
        By.XPATH, './/*').get_attribute('id')
    button_id = button_id[button_id.find('_') + 1:]
    driver.find_element(By.XPATH, f'//*[@id="id_yuiconfirmyes-yui_{button_id}"]').click()


def calculated_tasks(i, answ):
    driver.find_element(By.XPATH,
                        f'/html/body/div[3]/div/div/div/section/div/form/div/div[{i}]/div[2]/div/div[2]/span/input').send_keys(
        answ)


def solutions(url):
    driver.get(url)
    lens = driver.find_elements(By.CLASS_NAME, 'thispageholder')
    for q in range(1, len(lens) + 1):
        clas = driver.find_element(By.XPATH, f'//*[@id="q{str(q)}"]').get_attribute(
            'class')
        s = driver.find_element(By.XPATH, f'//*[@id="q{str(q)}"]/div[2]/div/div[1]')
        if 'Определите созвездие на звёздном небе' in s.text or 'Определите созвездие по его контурной карте' in s.text:
            phototasks_firstcourse(q)
        elif 'Сопоставьте звёзды и созвездия, в которых они находятся' in s.text:
            selectask(zvezdi_sozvezdiya, q)
        elif 'Сопоставьте даты и созвездия, по которым в эти даты проходит Солнце' in s.text or 'Сопоставьте даты и ' \
                                                                                                'созвездия, ' \
                                                                                                'в которых в этот ' \
                                                                                                'день находится ' \
                                                                                                'Солнце' in s.text:
            selectask(dati_sozvezdiya, q)
        elif 'Укажите, в каких полушариях небесной сферы расположены созвездия' in s.text:
            selectask(polushar_sozv, q)
        elif 'Определите тип затмения' in s.text:
            photooick_tasks(zatmeniya, q)
        elif 'Сопоставьте объекты (или понятия) и соответствующие им звёздные величины.' in s.text:
            selectask(objectc_velich, q)
        elif clas == 'que calculatedsimple adaptivenopenalty notyetanswered' or clas == 'que calculated ' \
                                                                                        'adaptivenopenalty ' \
                                                                                        'notyetanswered' or clas == 'que calculatedsimple deferredfeedback notyetanswered' or clas == 'que calculated deferredfeedback notanswered' or clas == 'que calculated deferredfeedback notyetanswered':
            try:
                text = ""
                for d in driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div/section/div/form/div/div[{q}]/div[2]/div/div[1]').find_elements(By.TAG_NAME, 'p'):
                    text += driver.find_element(By.XPATH, f'/html/body/div[3]/div/div/div/section/div/form/div/div['
                                                          f'3]/div[2]/div/div[1]/p[{d}]').text
            except Exception as e:
                text = s.text
            text = text.replace('\n', '')
            print(text)
            for i in SOLUTIONS.AYE.keys():
                if i in text:
                    print(text.replace('\n', ''))
                    calculated_tasks(q, SOLUTIONS.main(SOLUTIONS.AYE.get(i), text.replace('\n', '')))
                    break
        elif 'Сопоставьте объекты и характерные расстояния до них от Солнца' in s.text:
            selectask(objectc_rast, q)
        elif 'Мы смотрим на Солнечную систему с северного полюса Солнца.' in s.text:
            selectask(objectc_napravl, q)
        elif 'Соотнесите объекты Солнечной системы и их примерные размеры (диаметры)' in s.text:
            selectask(objectc_razmer, q)
        elif 'Расставьте спектральные классы звёзд по уменьшению температуры -- от горячих звёзд к холодным' in s.text:
            draganddrop(spectr_c, q)
        elif 'Сопоставьте спектральный класс и наблюдаемый цвет звезды' in s.text:
            selectask(spectr_zv, q)
        elif 'В левой колонке даны температуры поверхности звёзд. Сопоставьте им нужные спектральные классы.' in s.text:
            selectask(temp_zv, q)
        elif 'Расставьте звёзды в порядке увеличения их радиуса' in s.text:
            draganddrop(rad_zv, q)
        elif 'Сопоставьте тип галактики и её обозначение по классификации Хаббла' in s.text:
            selectask(tip_gal, q)
        elif clas == 'que gapselect adaptivenopenalty notyetanswered' or clas == 'que gapselect ' \
                                                                                        'deferredfeedback ' \
                                                                                        'notyetanswered' :
            gapselect(q)
        elif '' in s.text:
            multichoice(galaktiki, q)
    finish_test(lens)


def lsson_resh(url):
    driver.get(url)
    try:
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/section/div/div[2]/div/form/div/input[1]').click()
    except Exception:
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/section/div/div[3]/div/form/div/input[1]').click()
    try:
        driver.find_element(By.XPATH,
                            '/html/body/div[4]/div[2]/div/div[2]/form/fieldset[2]/div/div/div/input[1]').click()
    except Exception:
        pass
    solutions(driver.current_url)


lsson_resh('https://astroschools.ru/moodle/mod/quiz/view.php?id=84')
lsson_resh('https://astroschools.ru/moodle/mod/quiz/view.php?id=155')
lsson_resh('https://astroschools.ru/moodle/mod/quiz/view.php?id=164')
lsson_resh('https://astroschools.ru/moodle/mod/quiz/view.php?id=170')
lsson_resh('https://astroschools.ru/moodle/mod/quiz/view.php?id=172')
lsson_resh('https://astroschools.ru/moodle/mod/quiz/view.php?id=185')