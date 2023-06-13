theme_dir = join_paths(get_option('prefix'), 'share/icons', 'adw-gtk3')

install_subdir('Adwaita',
    install_dir: theme_dir,
    strip_directory: true,
    exclude_files: ['index.theme'],
)

conf_data = configuration_data()
conf_data.set('ThemeName', 'adw-gtk3')
configure_file(input : 'Adwaita/@0@'.format('index.theme'),
                output : '@0@'.format('index.theme'),
                configuration : conf_data,
                install_dir: theme_dir)

meson.add_install_script('meson/post_install.py', 'adw-gtk3')
