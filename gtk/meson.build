styles = []
foreach style: ['default', 'dark']
  if not get_option(style)
    message('skip style ' + style)
    continue
  endif
  styles += style
endforeach

subdir('src')
