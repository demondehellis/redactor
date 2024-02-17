# README

This is a Python script that takes in a markdown file, parses the content, and uses OpenAI's GPT-3.5-turbo model to fix the grammar and punctuation of the text content while keeping markdown and HTML tags as is.

## Requirements

- Python 3.6 or higher
- OpenAI Python package

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key.

## Usage

```bash
python main.py <input_path> [output_path]
```

- `input_path`: The path to the markdown file you want to fix.
- `output_path` (optional): The path where the fixed file will be saved. If not provided, the original file will be overwritten.

## How it works

1. The script reads the content of the input file.
2. It parses the front matter and the content.
3. It splits the content into paragraphs.
4. It fixes the grammar and punctuation of each paragraph using OpenAI's GPT-3.5-turbo model.
5. It saves the fixed content to the output file.

Please note that the script skips HTML tags, comments, and empty paragraphs.