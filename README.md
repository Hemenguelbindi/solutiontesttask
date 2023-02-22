# Solutian на Python Web Developer работа с платежной системой.

[stripe.com/docs](https://stripe.com/docs) - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки [stripe](https://stripe.com/docs) можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 
Цель данного проекта ознакомится с платежной сисемой и реализация простого сервера с одной страницей которая общается со Stripe  и создает платежные формы для товара. 
Для решения данной задачи используеются следующие технологии: 
  - Django
  - Django restframwork 
  - Библиотека stripe 
  - docker 
  - PosgrestSQL
  - python 3.11

## Неоходимые переменные окружениня:

```env
TOKEN_DJANGO_APP=Django_SECRET_KEY

DEV=[Включение выключения режима отладки] значения: True False
APP_HOST={ALLOWED_HOSTS}
DEV_DB={database}
DEV_NAME={DEV_NAME_Database}

PROD_DB={Production_database}
NAME_DB={NAME_Database}
PRODUCT_USER={ADMIN_USER}
PRODUCT_PASSWORD={PASSWORD}
PRODUCT_HOST={HOST_Database}
PRODUCT_PORT={PORT_Database}
STRIPE_PUBLIC_KEY={PUPLIK_KEY}
STRIPE_SECRET_KEY={SECTEY_KEY}
STRIP_WEBHOOK={WEBHOOK}
```

<div class="markdown prose w-full break-words dark:prose-invert light">
<p>Чтобы запустить проект, следуйте этим инструкциям:</p><ol><li>Убедитесь, что у вас установлены Docker и Docker Compose.</li><li>Склонируйте репозиторий проекта на свой локальный компьютер.</li><li>В корневой папке проекта создайте файл .env и добавьте необходимые переменные окружения (TOKEN_DJANGO_APP, DEV, APP_HOST, DEV_DB, DEV_NAME, PROD_DB, NAME_DB, PRODUCT_USER, PRODUCT_PASSWORD, PRODUCT_HOST, PRODUCT_PORT, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, STRIPE_WEBHOOK).</li><li>Откройте терминал и перейдите в корневую папку проекта.</li><li>Запустите команду <code>docker-compose up -d</code> для создания и запуска контейнеров в фоновом режиме.</li><li>Запустите команду <code>docker-compose exec web python manage.py migrate</code> для применения миграций базы данных.</li><li>Откройте браузер и перейдите на адрес <a href="http://localhost:8000" target="_new">http://localhost:8000</a>, чтобы открыть приложение.</li></ol><p>Если вы хотите остановить проект, запустите команду <code>docker-compose down</code>. Если вы хотите запустить проект снова, повторите шаги 4-7.</p></div>