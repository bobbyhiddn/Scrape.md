from setuptools import setup, find_packages

setup(
    name='scrape_md',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'openai',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'scrape_md = scrape.scrape:main'
        ]
    },
)