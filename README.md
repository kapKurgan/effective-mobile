# Техническое задание: AQA Python

---

## Задача

Автоматизировать тестирование логина на сайте с использованием Python.
Тестовый стенд:
```bash
https://www.saucedemo.com/
```

### Написать **5 тестов**, проверяющих разные сценарии авторизации:

- Успешный логин (standard_user / secret_sauce)
- Логин с неверным паролем
- Логин заблокированного пользователя (locked_out_user)
- Логин с пустыми полями
- Логин пользователем performance_glitch_user (проверить корректный переход и что страница открывается несмотря на возможные задержки)

---

### Требования:

- Использовать Selenium или Playwright
- Использовать Page Object
- Подключить Allure
- Проверять корректность URL и отображение элементов
- Добавить Dockerfile для запуска тестов в контейнере
- Python 3.10
- Все зависимости — в requirements.txt
- Короткая инструкция по запуску — в README.md


---
## Оглавление

- [CI/CD](#cicd)
- [URL отчетов GitHub Pages](#url-отчетов-github-pages)
- [Интеграция с GitHub Actions](#интеграция-с-github-actions)

---

## CI/CD

В этом проекте включена интеграция с GitHub Actions. 

Конфигурацию можно найти в [ui-tests.yml](./.github/workflows/ui-tests.yml).

---

## URL отчетов GitHub Pages

### HTML
```bash
https://kapKurgan.github.io/effective-mobile/<run_id>/pytest-report.html
```

Например:
https://kapKurgan.github.io/effective-mobile/20753388702/pytest_report.html


### ALLURE 
```bash
https://kapKurgan.github.io/effective-mobile/<run_id>/allure-report/index.html
```

Например:
https://kapKurgan.github.io/effective-mobile/20753388702/allure-report/index.html

---

## Требования
- Python 3.10
- GitHub account (для CI/CD и GitHub Pages)

Установка зависимостей:
```bash
pip install -r requirements.txt
```

--- 

## Интеграция с GitHub Actions

Workflow автоматически:
- Устанавливает Python 3.10
- Устанавливает зависимости
- Запускает тесты к реальному UI
- Генерирует HTML-отчеты
- Публикует отчеты в GitHub Pages

---
