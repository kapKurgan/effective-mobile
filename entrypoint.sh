#!/bin/bash
set -e

# Ловим Ctrl+C и завершаем все фоновые процессы
trap 'echo "⏹ Остановлено пользователем (Ctrl+C)"; kill $HTTP_PID $ALLURE_PID 2>/dev/null; exit 0' INT

# 1. Запуск тестов
pytest -s -v \
  --alluredir=reports/allure-results \
  --html=reports/pytest_report.html \
  --self-contained-html \
  --capture=tee-sys

# 2. Генерация Allure-отчёта
allure generate reports/allure-results --clean --output reports/allure-report

# 3. Веб-сервер для HTML (порт 8080) – тихо
cd reports
python3 -m http.server 8080 > /dev/null 2>&1 &
HTTP_PID=$!

# 4. Allure-serve (порт 5252) – тихо
allure open --host 0.0.0.0 --port 5252 allure-report > /dev/null 2>&1 &
ALLURE_PID=$!

# 5. Эхо ссылок
echo ""
echo "========================================================"
echo "|   Отчёты доступны по адресам:                        |"
echo "|   HTML  : http://localhost:8080/pytest_report.html   |"
echo "|   Allure: http://localhost:5252/index.html           |"
echo "|------------------------------------------------------|"
echo "|   Нажмите Ctrl+C для остановки контейнера.           |"
echo "========================================================"
echo ""

# 6. Бесконечный цикл – держим процесс на переднем плане
tail -f /dev/null