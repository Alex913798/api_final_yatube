# Проект социальной сети "Yatube" с api
## Описание
Незарегистрированные пользователи могут просматривать посты, комментарии, группы проекта. Для зарегистрированных пользователей доступны подписка на авторов, добавление постов, комментариев, а также удаление и редактирование собственных публикаций и комментариев.
## В API проекта доступны следующие эндпоинты:
- api/v1/posts/ При GET-запросе на этот эндпоинт будет получен список публикаций (при указании параметров limit и offset выдача будет осуществляться с пагинацией). При POST-запросе буден создана новая публикация. Анонимные POST-запросы запрещены.
- api/v1/posts/{id}/ GET-запрос позволяет поучить публикацию по id. PUT- и PATCH-запросы позволяют редактировать публикацию. DELETE-запрос удаляет публикацию. Анонимные PUT-, PATCH- и DELETE-запросы запрещены. Обновить и удалить публикацию может только автор публикации.
- api/v1/posts/{post_id}/comments/ При GET-запросе будут получены все комментарии к публикации. При POST-запросе будет создан новый комментарий.
- api/v1/posts/{post_id}/comments/{id}/ При GET-запросе будет получен комментарий по id. При PATCH- и PUT-запросах комментарий будет отредактирован. DELETE-запрос удалит комментарий. Анонимные PUT-, PATCH- и DELETE-запросы запрещены.
- api/v1/groups/ При GET-запросе будет получен список сообществ.
- api/v1/groups/{id}/ При GET-запросе будет получена информация о сообществе по id.
-api/v1/follow/ При GET-запросе будет получен список всех подписок пользователя, сделавшего запрос. При POST-запросе будет создана новая подписка пользователя, сделавшего запрос, на пользователя, переданного в теле запроса. Анонимные POST-запросы запрещены.
- api/v1/jwt/create/ Получение JWT-токена.
- api/v1/jwt/refresh/ Обновление JWT-токена.
- api/v1/jwt/verify/ Проверка JWT-токена.

## Запуск проекта локально:


- Клонировать репозиторий и перейти в него в командной строке:
  git clone https://github.com/Alex913798/api_final_yatube.git 
  cd api_final_yatube 
- Cоздать и активировать виртуальное окружение: 
  python3 -m venv env 
  source env/bin/activate 
- Установить зависимости из файла requirements.txt: 
  python3 -m pip install --upgrade pip 
  pip install -r requirements.txt 
- Выполнить миграции: 
  python3 manage.py migrate
- Запустить проект: 
  python3 manage.py runserver

## Автор
Александр Ермаков