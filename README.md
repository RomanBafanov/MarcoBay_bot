# MarcoBay_bot

Бот для отправки подарочного видео, так же с возможностью подписаться на ТГ канал и группу ВК
 
## Как установить

Python3 должен быть уже установлен. Затем используйте pip 
(или pip3, если есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
``` 

### Будет установлен:

pyTelegramBotAPI==4.14.0
python-dotenv==1.0.0

## Переменные окружения

Необходимо создать файл **.env**, в нём должены находится:

- бот токен полученный от **BotFather** в Телеграм.
Переменная должна иметь имя **BOT_TOKEN**

```bash
BOT_TOKEN='ваш токен бота'
```

- ссылка на Телеграм канал.
Переменная должна иметь имя **TG**

```bash
TG='ссылка на Телеграм канал'
```

- ссылка на подарочное видео.
Переменная должна иметь имя **URL**

```bash
URL='ссылка на подарочное видео'
```

- задержка в секундах между отправкой стартовых сообщений.
Переменная должна иметь имя **TIME_START**

```bash
TIME_START='задержка между стартовых сообщений'
```

- задержка в секундах перед напоминанием о подписке.
Переменная должна иметь имя **TIME_REMINBER**

```bash
TIME_REMINBER='задержка перед напоминанием'
```

## Запуск

Запустите программу командой 
```bash
python main.py
```

## Цели проекта

Код написан для **MarcoBay** в целях коммуникации с клиентами.