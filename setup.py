from distutils.core import setup

setup(name='kyle_helper',
      version='1.1.01',
      description='Helper functions to help Kyle',
      author='Kyle Mills',
      author_email='kyle.mills@uoit.net',
      packages=['latex','ednn'],
      scripts=['scripts/update_result'],
      install_requires=[
         'inflect',
         'regex',
         'argparse',
      ]
   )

