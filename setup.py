from distutils.core import setup

setup(
    name='Page Generator',
    version='0.0.1',
    author='Anton Onikiychuk',
    author_email='anton@onikiychuk.com',
    packages=['page_gen'],
    scripts=[],
    url='https://github.com/holyslon/page_gen',
    license='LICENSE.txt',
    description='Simple page generator.',
    long_description='Simple page generator.',
    install_requires=[
        "Mako >= 0.7.2",
        "markdown2 >= 2.0.1",
    ],
)