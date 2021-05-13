from setuptools import setup
from pip.req import parse_requirements

setup(name='docparser',
      version='0.1',
      description='DocParser',
      license='MIT',
      packages=['docparser', 'docparser.utils', 'docparser.objdetmetrics_lib'],
      install_reqs=parse_requirements('requirements.txt', session='hack'),
      zip_safe=False)
