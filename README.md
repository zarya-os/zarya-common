## zarya-common

`zarya-common` provides custom GNOME session with the following as overrides:
- **gtk**: Fork of [`adw-gtk3-theme`](https://github.com/lassekongo83/adw-gtk3) that adds gtk-2 + gtk-4 themes. (_uses yaru's build structure_)
- **gnome-shell**: Fork of [`adwaita-gnome-shell-theme`](https://gitlab.gnome.org/GNOME/gnome-shell) that adds `prefer-light` stylesheet. (_uses yaru's build structure_)
- **icons**: Fork of [`adwaita-icon-theme`](https://gitlab.gnome.org/GNOME/adwaita-icon-theme) that aims to add further mimetypes. (_uses yaru's build structure_)
- **plymouth**: Fork of [`plymouth-theme-vanilla`](https://github.com/Vanilla-OS/plymouth-theme-vanilla) renamed with `zarya-prefix` (_uses plymouth-theme-vanilla build structure_)
- **backgrounds**: Fork of [`vanilla-backgrounds`](https://github.com/Vanilla-OS/vanilla-backgrounds) to act as placeholder-wallpapers until new ones are picked (_uses vanilla-backgrounds build structure_)
- **sessions**: adds custom `GNOME` session with the above overrides (_uses yaru's build structure_).

### dependencies
```bash
sudo apt install libgtk-3-dev git meson sassc
```

#### clone and build

```bash
git clone https://github.com/zarya-os/zarya-common.git
cd yaru
# Initialize build system (only required once per repo)
meson build
cd build
# Build and install
sudo ninja install
```