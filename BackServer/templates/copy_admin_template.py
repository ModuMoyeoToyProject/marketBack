import site
from distutils.dir_util import copy_tree
from os.path import join

djangoadmin_template_dir = join(site.getsitepackages()[0], 'django/contrib/admin/templates')
copy_tree(djangoadmin_template_dir, 'BackServer/templates')

# /usr/local/lib/python3.8/site-packages/django/contrib/admin/templates