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

## Неоходимые переменные окружеиня:

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
```

