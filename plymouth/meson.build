# Path variables
plymouth_theme_path = get_option('prefix') / get_option('datadir') / 'plymouth' / 'themes'

# config
conf = configuration_data()
conf.set_quoted('PLYMOUTH_THEME_PATH', plymouth_theme_path)

plymouth_themes = [
  'zarya-bgrt',
  'zarya-text',
]

foreach plymouth_theme: plymouth_themes
  if not get_option(plymouth_theme)
    message('skip plymouth_theme ' + plymouth_theme)
    continue
  endif

  message('build plymouth_theme ' + plymouth_theme)
  subdir(plymouth_theme)

endforeach
