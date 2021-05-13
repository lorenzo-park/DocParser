from setuptools import setup


try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements


setup(name='docparser',
      version='0.1',
      description='DocParser',
      license='MIT',
      packages=['docparser', 'docparser.utils', 'docparser.objdetmetrics_lib'],
      data_files=[('config', ['docparser/logging.conf'])],
      install_reqs=parse_requirements('requirements.txt', session='hack'),
      zip_safe=False)
