# TaskTracker
### 1. Цель проекта 
<hr>
Цель проекта - разработать систему отслеживания задач (далее Система).
Пользователи могут созавать в Системе проекты, задачи в рамках этих проектов,
указывать срок выполнения, исполнителей, логировать время, отслеживать
выполнение задач. В системе должна быть предусмотрена интеграция с Telegram-ботом.

### 2. Описание системы
<hr>
Система состоит из следующих основных функциональных блоков:

1. Регистрация, аутентификация, авторизация
2. Функционал пользователя
3. Функционал интеграции с Telegram

#### 2.1 Регистрация
<hr>
Процесс регистрации должен быть реализован в интерфейсах Системы. При регистрации
должны быть запронешы следующие поля:

- email - обязательное поле
- имя и фамилия - обязательные поля
- пароль - обязательное поле
- telegram-аккаунт - опциональное поле

#### 2.2 Аутентификация пользователей
<hr>
Аутентификация осуществляется по email и паролю. Для пользователей должна быть реализована
возможность восстановления забытого пароля. При запросе пароля необходимо на email 
подписчика прислать ссылку на восстановление пароля. При переходе по этой ссылке пользователь
должен иметь возможность задать новый пароль на вход.

#### 2.3 Функционал пользователя
<hr>
Пользователь должен иметь возможность создавать проект. При создании проекта у
пользователя должны быть запрошены следующие поля:

- название проекта
- описание проекта

В рамках проекта пользователь должен иметь возможность создавать задачи.
Задача должна включать в себя следующие поля:

- имя задачи
- описание
- дедлайн

На втором этапе разработки для пользователя должна быть предусмотрена возможность
логировать время в конкретную задачу и просматривать данные о уже залогированном времени.
Для данного модуля должна быть предусмотрена интеграция в Telegram.

### 3. Предполагаемый стек технологий
Для реализации системы предлагается следующий стек технологий:

- Бэкэнд:
  + Язык: Python
  + Фрэймворк: Django
  + БД: ????????
  + Интеграция с Telegram: ????????
- Фронтенд:
  + Язык: JavaScript
  + Фрэймворк: Vue2

### 3. Требования к дизайну страниц
 - общий стиль: ???????
 - фон: ???????
 - логотип: ????????
 - footer с информацией о Системе
