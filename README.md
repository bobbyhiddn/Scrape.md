
# Scrape.md

## Introduction

  Scrape.md is a Python package that allows you to scrape text from any website and generate a comprehensive summary of the text using OpenAI's API. This is then converted into a markdown file that can be used for any purpose.


### Requirements

- Python 3.6+
- OpenAI API Key set as an environment variable(OPENAI_API_KEY)
    - This can be done with the following command:
    
    ```bash
    export OPENAI_API_KEY="your-key-here"
    ```

    - You can also add this to your .bashrc or .zshrc file to make it permanent.

## Installation

You have a few choices for installation but they both start with cloning the repo: 

```bash
git clone https://github.com/bobbyhiddn/Scrape.md.git
```
Then you can either install the package using pip:

```bash
pip install .
```
Or you can install the package using the setup.py file:

```bash
python setup.py install
```

## Usage

To use the package, run the following command:

```bash
scrape_md https://www.example.com
```

This will create a markdown file in the current directory with a filename based on the website you are scraping. For example, if you were scraping https://www.example.com, the file would be named example.md or something like that.

