project('zarya',
        version: '44',
        meson_version: '>= 0.59',
        license : ['GPL3', 'CC BY-SA 4.0'],
        default_options: ['prefix=/usr'])
        
#Import 
fs = import('fs')
gnome = import('gnome')
i18n = import('i18n')
python = find_program('python3')
sassc = find_program('sassc')

components = ['gnome-shell', 'gtk', 'icons', 'sessions', 'backgrounds', 'plymouth']

foreach component: components
  if not get_option(component)
    message('skip component ' + component)
    continue
  endif

  message('build component ' + component)
  subdir(component)

endforeach

subdir('po')
