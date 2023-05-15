#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set ft=python :

import sys
from os import environ, path
from shutil import move

PREFIX = environ.get('MESON_INSTALL_DESTDIR_PREFIX', '/usr')
data_dir = sys.argv[1]
project_name = sys.argv[2]
styles = sys.argv[3:]

themes_dir = path.join(PREFIX, data_dir, 'themes')

for s in styles:
    if s == 'default':
        style_name = project_name
    else:
        style_name = "{project}-{style}".format(project=project_name, style=s)

    style_dir = path.join(themes_dir, style_name)

    # rename index.theme
    theme_index_name = style_name + "-index.theme"
    theme_index_src = path.join(style_dir, theme_index_name)
    if path.exists(theme_index_src):
        theme_index_dst = path.join(style_dir, 'index.theme')
        move(theme_index_src, theme_index_dst)

    for gtkver in ['3.0', '4.0']:
        gtk_dir = path.join(style_dir, 'gtk-' + gtkver)

        # rename gresource
        theme_gresource = "{style}-gtk-{ver}.gresource".format(style=style_name, ver=gtkver)
        theme_gresource_src = path.join(gtk_dir, theme_gresource)
        if path.exists(theme_gresource_src):
            theme_gresource_dst = path.join(gtk_dir, 'gtk.gresource')
            move(theme_gresource_src, theme_gresource_dst)

        # rename css
        for variant in ['', '-dark']:
            theme_gtk_css = "{style}-gtk{variant}-{ver}.css".format(style=style_name, ver=gtkver, variant=variant)
            theme_gtk_css_src = path.join(gtk_dir, theme_gtk_css)
            if path.exists(theme_gtk_css_src):
                theme_gtk_css_dst = path.join(gtk_dir, 'gtk{variant}.css'.format(variant=variant))
                move(theme_gtk_css_src, theme_gtk_css_dst)
