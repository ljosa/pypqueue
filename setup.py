from setuptools import setup

setup(
    name="pqueue",
    version="1.0.0",
    url="http://github.com/ljosa/pypqueue",
    download_url = 'https://github.com/ljosa/pypqueue/tarball/1.0.0',
    description="Python interface to submit jobs to http://github.com/ljosa/go-pqueue",
    long_description=open('README.rst', 'rt').read(),
    author="Vebjorn Ljosa",
    author_email="vebjorn@ljosa.com",
    license="BSD",
    packages=['pqueue'],
    test_suite="pqueue.tests"
)
