import setuptools

setuptools.setup(
    name='requests-retry-on-exceptions',
    version='2020.10.30',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
