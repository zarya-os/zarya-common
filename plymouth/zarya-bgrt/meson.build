zarya_bgrt_plymouth = i18n.merge_file(
  input: configure_file(
    input: 'zarya-bgrt.plymouth.desktop',
    output: 'zarya-bgrt.plymouth.desktop',
    configuration: {
      'PLYMOUTH_THEME_PATH': plymouth_theme_path,
    },
  ),
  output: 'zarya-bgrt.plymouth',
  type: 'desktop',
  po_dir: '../../po',
  install: true,
  install_dir: plymouth_theme_path / 'zarya-bgrt',
)

install_subdir('bgrt_assets',
  install_dir:plymouth_theme_path / 'zarya-bgrt',
  strip_directory: true,)
