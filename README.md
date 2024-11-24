# Scrape.md

![banner](Scrape.png)

## Introduction

Scrape.md is a command-line tool that allows you to scrape text content from any website and generate a comprehensive Markdown transcription using OpenAI's API. The script employs a four-stage iterative process to ensure high-quality Markdown files that closely match the original content.

## Features

- **Four-Stage Iterative Process**:
  1. **First Draft Generation**: Creates an initial Markdown version of the website's content.
  2. **Review Stage**: An AI assistant reviews the first draft for discrepancies and provides detailed feedback.
  3. **Improvement Stage**: The first draft is improved based on the AI's feedback to better match the original content.
  4. **Final Review**: A final AI review is performed to ensure the quality of the transcription, and the review is displayed in the CLI for your reference.
  
- **AI-Generated Filenames**: Automatically generates a suitable filename based on the content.
- **Customizable Save Location**: Option to save the generated Markdown file in a specified directory via the `SCRAPE_ARCHIVE_PATH` environment variable.
- **Command-Line Interface**: Easy-to-use CLI powered by Click.

## Limitations

- **Client-Side Rendered Content**: Cannot scrape text from images, React components, or other non-text elements rendered on the client side.
- **Authentication and Paywalls**: Cannot access websites that require authentication or are behind a paywall.
- **OpenAI API Costs**: Usage of the tool will consume tokens from your OpenAI API quota, which may incur costs.
- **Rate Limits**: Bound by OpenAI's API rate limits; excessive use might lead to throttling.

## Requirements

- **Python 3.6+**
- **OpenAI API Key**: Set as an environment variable `OPENAI_API_KEY`.

  ```bash
  export OPENAI_API_KEY="your-api-key-here"
  ```

- **Optional**: `SCRAPE_ARCHIVE_PATH` environment variable to specify the directory where the generated Markdown files will be saved.

  ```bash
  export SCRAPE_ARCHIVE_PATH="/path/to/your/archive"
  ```

## Installation

Clone the repository and install the package using `pip`:

```bash
git clone https://github.com/bobbyhiddn/Scrape.md.git
cd Scrape.md
pip install .
```

Alternatively, install using the `setup.py` file:

```bash
python setup.py install
```

## Usage

To scrape a website and generate a Markdown file, run:

```bash
scrape_md https://www.example.com
```

### Options and Environment Variables

- **Saving Location**: If `SCRAPE_ARCHIVE_PATH` is set, you will be prompted to choose whether to save the file in the specified path or the current working directory.
- **OpenAI API Key**: Ensure the `OPENAI_API_KEY` environment variable is set; otherwise, the script will exit with an error.
  
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

## OpenAI API Considerations

- **API Costs**: Be aware that each run consumes tokens, which may incur costs based on your OpenAI pricing plan.
- **Max Tokens**: The script uses a high `max_tokens` value to handle large content, which can increase usage.
- **Error Handling**: If OpenAI API rate limits are exceeded or if there's an authentication error, the script will output an appropriate message.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License.

