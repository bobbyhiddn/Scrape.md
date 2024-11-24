from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scrape_md',
    version='1.0.0',
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
    author="Micah Longmire",
    author_email="mlmicahlongmire@gmail.com",
    description="Scrape.md is a command line interface for scraping and converting website content to Markdown.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/bobbyhiddn/Scrape.md",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)