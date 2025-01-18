# Морской бой с таблицей результатов Codeforces на Django

![Screenshot_20250118_130722](https://github.com/user-attachments/assets/7deb0e48-eb62-4a0b-920e-7cd550f33b80)

## Установка

1. Добавьте папку `battleship/` в ваш Django проект.
2. Обновите `urls.py` проекта (не приложения battleship) и `INSTALLED_APPS` в `settings.py` проекта.
3. API ключи для доступа к Codeforces нужно добавить в environment с названиями `CF_API_KEY` и `CF_API_SECRET` или записать вручную в файле `battleship/logic/cfparse.py`.
4. Конфиги каждой игры находятся в `battleship/logic/config.json`.
5. Для проверки кораблей на корректность можете использовать `CHECK_SHIPS_TABLE.py`.
6. Общий счёт команды считается по формуле в `draw_stats` в `battleship/templates/battleship/js/state.js`.
