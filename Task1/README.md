## Выполнение ping в DVWA
- Скрипт логиниться в DVWA
- По желанию меняет защиты внутри контейнера
- Выполняет ping на адрес, указанный пользователем при запуске 

#####P.S. необходимо наличие DVWA docker:
1. docker pull citizenstig/dvwa
2. docker run -d -p 81:80 citizenstig/dvwa