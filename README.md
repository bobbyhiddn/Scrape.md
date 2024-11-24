# Scrape.md

## Introduction

Scrape.md is a Python package that allows you to scrape text from any website and generate a comprehensive transcription of the content using OpenAI's API. The script features a four-stage iterative process to ensure high-quality Markdown files that closely match the original content.

### Requirements

- Python 3.6+
- OpenAI API Key set as an environment variable (`OPENAI_API_KEY`)
    - This can be done with the following command:
    
    ```bash
    export OPENAI_API_KEY="your-key-here"
    ```
    - You can also add this to your `.bashrc` or `.zshrc` file to make it permanent.

- *Optional*: Set the `SCRAPE_ARCHIVE_PATH` environment variable to specify a directory where the generated Markdown files will be saved. I figure those who are wanting to use this with Obsidian or another note-taking app might want to save all their transcriptions in a specific directory. That's what I'm doing, at least.
    - Set it using the following command:

    ```bash
    export SCRAPE_ARCHIVE_PATH="/path/to/your/archive"
    ```

## Installation

First, clone the repository:

```bash
git clone https://github.com/bobbyhiddn/Scrape.md.git
```

Then you can either install the package using pip:

```bash
pip install .
```

Or install the package using the `setup.py` file:

```bash
python setup.py install
```

## Usage

To use the package, run the following command:

```bash
scrape_md https://www.example.com
```

By default, this will create a Markdown file in the current directory with a filename based on the content of the website you are scraping.

If you have the `SCRAPE_ARCHIVE_PATH` environment variable set, when you run the script, you will be prompted to choose whether to save the file in your specified scrape archive path (`$SCRAPE_ARCHIVE_PATH`) or in the current working directory.

### Four-Stage Iterative Process

The script now employs a four-stage process to enhance the quality of the transcribed content:

1. **First Draft Generation**: Creates an initial Markdown version of the website's content.
2. **Review Stage**: An AI assistant reviews the first draft for discrepancies and provides detailed feedback.
3. **Improvement Stage**: The first draft is improved based on the AI's feedback to better match the original content.
4. **Final Review**: A final AI review is performed to ensure the quality of the transcription. The review is displayed in the CLI for your reference.

This process ensures that the generated Markdown file is clean, accurate, and closely reflects the original content with all important details preserved.

### Example

```bash
scrape_md https://www.greenmatters.com/news/new-species-2024
```

Output:

```
Fetching content.
Title: New Species 2024: The Animals and Plant Species Revealed This Year
Generating the first draft.
Reviewing the first draft.
Improving the Markdown content.
Generating a suitable filename.
Content saved to new_species_discoveries_2024.md
Final AI Review:
[Detailed review output]
```

The generated file `new_species_discoveries_2024.md` will contain a high-quality transcription of the webpage content.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

