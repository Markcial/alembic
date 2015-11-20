from os.path import dirname, abspath, sep

app_root = abspath(dirname(__file__))
template_folder = app_root + sep + 'templates'
asset_folder = app_root + sep + 'static'
storage_folder = app_root + sep + 'storage'
