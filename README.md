<h2 align="center">TelegramBot Screenshoter</h2>

## Старт
#### Настройка

1. Необходимо переименовать файл **dev.env** в **.env**
2. Заполнить своими данными:

TELEGRAM_TOKEN - токен бота.
Переходим в бота - [@BotFather](https://t.me/BotFather). 

Командой */newbot* создаем нового бота и в конце получаем токен.

Командой */mybots* получаем ботов, выбираем нужного и жмем кнопку: *API Token*

SCREEN_PATH - путь до папки для сохранения скриншотов

```
TELEGRAM_TOKEN=5353866627:AAHXypJHZVaxidI20FNXI8YEazSASaa5h-E
SCREEN_PATH=screenshots
```

#### Запустить бота
    docker-compose up --build -d
    

