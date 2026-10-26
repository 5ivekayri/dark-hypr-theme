#!/usr/bin/env python3
from pathlib import Path
import datetime, shutil, subprocess, tarfile, tempfile, urllib.request
root=Path(__file__).resolve().parent
home=Path.home()
files=['.config/hypr/hyprland.conf','.config/waybar/style.css','.config/wofi/style.css','.config/gtk-3.0/settings.ini','.config/gtk-4.0/settings.ini','.icons/default/index.theme']
backup=root/('backup-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
with tempfile.TemporaryDirectory() as tmp:
    archive=Path(tmp)/'cursor.tar.xz'
    urllib.request.urlretrieve('https://github.com/ful1e5/Bibata_Cursor/releases/download/v2.0.7/Bibata-Modern-Classic.tar.xz',archive)
    with tarfile.open(archive) as tar:
        tar.extractall(tmp,filter='data')
    theme=Path(tmp)/'Bibata-Modern-Classic'
    assert (theme/'cursors/left_ptr').exists(), 'Missing cursor files'
    for rel in files:
        dest=home/rel
        if dest.exists():
            saved=backup/rel
            saved.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(dest,saved)
    shutil.copytree(theme,home/'.icons/Bibata-Modern-Classic',dirs_exist_ok=True)
    for rel in files:
        dest=home/rel
        dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(root/rel,dest)
for cmd in [ ['gsettings','set','org.gnome.desktop.interface','cursor-theme','Bibata-Modern-Classic'], ['gsettings','set','org.gnome.desktop.interface','cursor-size','24'], ['hyprctl','reload'], ['hyprctl','setcursor','Bibata-Modern-Classic','24'], ['pkill','-SIGUSR2','waybar'] ]:
    subprocess.run(cmd,check=False)
print('Theme installed. Backup:',backup)
subprocess.run(['Hyprland','--verify-config','-c',str(home/'.config/hypr/hyprland.conf')],check=True)
