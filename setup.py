from setuptools import setup

setup(name='kyle_helper',
      version='1.2.07',
      description='Helper functions to help Kyle',
      author='Kyle Mills',
      author_email='kyle.mills@uoit.net',
      packages=['latex','dnn', 'data', 'render'],
      scripts=['scripts/update_result'],
      install_requires=[
         'inflect',
         'regex',
         'argparse',
         'matplotlib',
         'opencv-python',
         'numpy'
      ]
   )

