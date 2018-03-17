from distutils.core import setup


setup(
    name='pylint-badge',
    version='0.9',
    description="Runs pylint to generate badges",
    author="Pouncy Silverkitten",
    author_email="pouncy.sk@gmail.com",
    url="https://github.com/pouncysilverkitten/pylint-badge",
    install_requires=["pylint",]
    entry_points = {
        'console_scripts': ['pylint-badge=pylint-badge.pylint-badge:main'],
    }
}
