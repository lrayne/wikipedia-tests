# Запуск

Для того, чтобы запустить тест-кейсы, необходимо:

1. Склонировать репозиторий
```bash
git clone https://github.com/lrayne/wikipedia-tests
```

2. Установить зависимости

```bash
poetry install
```

3. Положить `.apk` в корень проекта

4. Создать `.env`, внутри него указать username и login от Browserstack

```dotenv
bstack_username='username'
bstack_accesskey='accesskey'
```

5. Создать отдельные `.env` для необходимых контекстов запуска:

<details><summary>Для запуска на Browserstack</summary>

Наименование файла —`.env.bstack`, внутри него:
```dotenv
projectName='Your project'
buildName=Your build name
sessionName='Your session name'
app=bs://0ff93e27c635bc80292dc1158547a219944fb184
deviceName='Your device'
appWaitActivity='org.wikipedia.*'
timeout=4
```
</details>

<details><summary>Для запуска локально на реальном девайсе</summary>

Наименование файла —`.env.local_emulator`, внутри него:
```dotenv
app=apk.apk
remote_url=http://127.0.0.1:4723
deviceName=DeviceName
udid=3221234
timeout=5
```
</details>

<details><summary>Для запуска локально на эмуляторе</summary>

Наименование файла —`.env.local_real_device`, внутри него:
```dotenv
app=apk.apk
remote_url=http://127.0.0.1:4723
deviceName=DeviceName
timeout=1
udid=1233311
```
</details>


6. Запустить тест-кейсы, указав необходимый контекст:

```bash
context='bstack' pytest tests/android  
```

```bash
context='real_device' pytest tests/android
```

```bash
context='local_real_device' pytest tests/android
```