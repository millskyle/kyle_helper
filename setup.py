from setuptools import setup,find_packages

setup(name='kyle_helper',
      version='1.3.0',
      description='Helper functions to help Kyle',
      author='Kyle Mills',
      author_email='kyle.mills@uoit.net',
      packages=find_packages(),#,['kyle_helper','latex','dnn', 'data', 'render'],
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

