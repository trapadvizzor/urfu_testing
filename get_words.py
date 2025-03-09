import requests

# URL, к которому вы хотите получить доступ
#url = "https://wise-chefs-kneel.loca.lt/suggest"
url = ' http://172.20.10.3:5031/suggest'
# Настройка заголовков запроса
headers = {
    'User-Agent': 'MyUserAgent/1.0',
    'Authorization': 'Bearer some_token'
}

# Отправка запроса с заголовками
response = requests.get(url, headers=headers, params={'w': 'п'})

# Проверка ответа
if response.status_code == 200:
    print("Успешно обошли страницу напоминания!")
    print(response.text)
else:
    print("Возникла ошибка:", response.status_code)
