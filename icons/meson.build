theme_dir = join_paths(get_option('prefix'), 'share/icons', 'adw-gtk3')

install_subdir('Adwaita',
    install_dir: theme_dir,
    strip_directory: true,
    exclude_files: ['index.theme'],
)

themes_f = [
  'index.theme',
]
conf_data = configuration_data()
conf_data.set('ThemeName', 'adw-gtk3')
foreach theme: themes_f
  configure_file(input : 'Adwaita/@0@'.format(theme),
                 output : '@0@'.format(theme),
                 configuration : conf_data,
                 install_dir: theme_dir)
endforeach

meson.add_install_script('meson/post_install.py', 'adw-gtk3')
