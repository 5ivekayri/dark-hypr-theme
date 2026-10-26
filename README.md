# Graphite Hyprland theme

Тёмная графитовая тема под пейзаж с холодным серым туманом.

![Обои](.wallpapers/selected-wallpaper.png)

## Состав

- Hyprland: серые градиентные рамки, приглушённое размытие, скругления 10 px.
- Waybar и Wofi: графитовые поверхности и светло-серый текст.
- GTK 3/4 и Xcursor: Bibata Modern Classic, 24 px.
- Выбранные обои и конфиг Hyprpaper для eDP-1 и HDMI-A-1.
- `apply.py`: скачивание курсора, резервное копирование и установка настроек.

## Установка

Этот пакет предназначен для существующей настроенной сессии пользователя. Это оформление, а не полный дистрибутив dotfiles. Нужны Python 3.12+, интернет, Hyprland, Hyprpaper, Waybar, Wofi, Kitty и Thunar. Для применения курсора через GSettings нужны соответствующие схемы GNOME.

Основной конфиг использует уже существующие файлы:

- `~/.config/hypr/monitors.conf`
- `~/.config/hypr/legacy-keybinds.conf` и его зависимости
- `~/.config/hypr/scripts/external-monitor-profile.sh`
- `~/.local/bin/refresh-desktop-portals`
- действующий конфиг Waybar

Обои входят в пакет: `.wallpapers/selected-wallpaper.png`. Установщик копирует их в `~/.wallpapers/` и подставляет домашнюю папку в конфиг Hyprpaper. Для других имён мониторов измените поля `monitor` в `.config/hypr/hyprpaper.conf`. Настройки мониторов и сторонние скрипты не входят в пакет.

Из каталога пакета выполните без sudo:

```bash
python3 apply.py
```

Установщик заменяет восемь файлов из `.config/`, `.icons/` и `.wallpapers/`, предварительно сохраняя существующие версии в `backup-ДАТА-ВРЕМЯ/` рядом с собой. Он также устанавливает курсор в `~/.icons/Bibata-Modern-Classic`, меняет тему и размер курсора в GSettings, перезагружает Hyprland, Waybar и Hyprpaper. Уже запущенные приложения могут потребовать перезапуска для обновления курсора.

## Восстановление

Скопируйте необходимые файлы из `backup-ДАТА-ВРЕМЯ/.config/`  , `.icons/` и `.wallpapers/` обратно в одноимённые каталоги домашней папки. Затем выполните `hyprctl reload` и `pkill -SIGUSR2 waybar`. GSettings не входит в файловую резервную копию; предыдущий курсор — Bibata Modern Ice, размер 24:

```bash
gsettings set org.gnome.desktop.interface cursor-theme Bibata-Modern-Ice
gsettings set org.gnome.desktop.interface cursor-size 24
hyprctl setcursor Bibata-Modern-Ice 24
```

## Источник курсора

[Bibata Cursor](https://github.com/ful1e5/Bibata_Cursor), вариант Modern Classic, релиз v2.0.7. Архив курсора загружается при установке и не хранится в репозитории. Права на сторонние материалы принадлежат их авторам. Обои предоставлены пользователем; их автор и лицензия не указаны.

## Git

Локальная ветка: `main`. Репозиторий: https://github.com/5ivekayri/dark-hypr-theme. Резервные копии не включаются в Git и ZIP.
