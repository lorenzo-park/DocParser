from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='docparser',
      version='0.1',
      description='DocParser',
      license='MIT',
      packages=['docparser', 'docparser.utils', 'docparser.objdetmetrics_lib'],
      install_requires=required,
      zip_safe=False)
