backgrounddir = join_paths(get_option('prefix'), get_option('datadir'), 'backgrounds', 'zarya')
metadatadir = join_paths(get_option('datadir'), 'gnome-background-properties')

backgrounds = ['vanilla-default.webp',  'vanilla-dark.webp']

conf_data = configuration_data()
  conf_data.set('BACKGROUNDDIR', backgrounddir)
  configure_file(input: 'zarya.xml.in',
    output: 'zarya.xml',
    configuration: conf_data,
    install: true,
    install_dir: metadatadir
  )

install_data(backgrounds, install_dir: backgrounddir)


