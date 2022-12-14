<h1>Работа с приложением из терминала</h1>

При запуске приложения из терминала можно использовать следующую команду:

```shell
python app.exe /s [количество сообщений] /i [интервал] /t [топик] /b [брокеры] /n [флаг пустых полей] /l [логгирование]
```

Доступные параметры:
- `/s` - количество сообщений (по умолчанию, бесконечно)
- `/i` - временной интервал между сообщениями в секундах (по умолчанию, 5 сек)
- `/t` - название топика, в который буду отправляться сообщения (по умолчанию, `default_topic`)
- `/b` - брокеры, которым будут отправляться сообщения (по умолчанию, localhost:29092)
- `/n` - флаг включения пустых полей в сообщения (по умолчанию, выключено)
- `/l` - флаг включения логирования (по умолчанию, выключено) 


<i>*брокеров необходимо записывать через запятую, но без пробелов</i>

Пример запуска приложения:

```shell
python app.py /s 100 /i 5 /t topicname /b localhost:1111,localhost:2222 /n Y /l Y
```