from distutils.core import setup

setup(name='kyle_helper',
      version='1.0.03',
      description='Helper functions to help Kyle',
      author='Kyle Mills',
      author_email='kyle.mills@uoit.net',
      packages=['latex',],
      scripts=['scripts/update_result'],
      install_requires=[
         'inflect',
         'regex',
      ]
   )

