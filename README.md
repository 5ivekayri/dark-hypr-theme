# Graphite Hyprland theme

Тёмная графитовая тема под пейзаж с холодным серым туманом.

## Состав

- Hyprland: серые градиентные рамки, приглушённое размытие, скругления 10 px.
- Waybar и Wofi: графитовые поверхности и светло-серый текст.
- GTK 3/4 и Xcursor: Bibata Modern Classic, 24 px.
- `apply.py`: скачивание курсора, резервное копирование и установка настроек.

## Установка

Этот пакет предназначен для существующей настроенной сессии пользователя. Это оформление, а не полный дистрибутив dotfiles. Нужны Python 3.12+, интернет, Hyprland, Hyprpaper, Waybar, Wofi, Kitty и Thunar. Для применения курсора через GSettings нужны соответствующие схемы GNOME.

Основной конфиг использует уже существующие файлы:

- `~/.config/hypr/monitors.conf`
- `~/.config/hypr/legacy-keybinds.conf` и его зависимости
- `~/.config/hypr/scripts/external-monitor-profile.sh`
- `~/.local/bin/refresh-desktop-portals`
- действующие конфиги Hyprpaper и Waybar

Обои, настройки мониторов и сторонние скрипты не входят в этот пакет. Выбранные обои остаются установленными отдельно.

Из каталога пакета выполните без sudo:

```bash
python3 apply.py
```

Установщик заменяет шесть файлов из `.config/` и `.icons/`, предварительно сохраняя существующие версии в `backup-ДАТА-ВРЕМЯ/` рядом с собой. Он также устанавливает курсор в `~/.icons/Bibata-Modern-Classic`, меняет тему и размер курсора в GSettings, перезагружает Hyprland и Waybar. Уже запущенные приложения могут потребовать перезапуска для обновления курсора.

## Восстановление

Скопируйте необходимые файлы из `backup-ДАТА-ВРЕМЯ/.config/` и `.icons/` обратно в одноимённые каталоги домашней папки. Затем выполните `hyprctl reload` и `pkill -SIGUSR2 waybar`. GSettings не входит в файловую резервную копию; предыдущий курсор — Bibata Modern Ice, размер 24:

```bash
gsettings set org.gnome.desktop.interface cursor-theme Bibata-Modern-Ice
gsettings set org.gnome.desktop.interface cursor-size 24
hyprctl setcursor Bibata-Modern-Ice 24
```

## Источник курсора

[Bibata Cursor](https://github.com/ful1e5/Bibata_Cursor), вариант Modern Classic, релиз v2.0.7. Архив курсора загружается при установке и не хранится в репозитории. Права на сторонние материалы принадлежат их авторам.

## Git

Локальная ветка: `main`. Удалённый репозиторий будет подключён после получения URL. Резервные копии не включаются в Git и ZIP.
