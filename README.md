# ESG Report Summarizer

A minimal Python tool that uses an LLM to summarize ESG (Environmental, Social, Governance) and sustainability reports.

## What This Does

Takes a plain text ESG report and generates a structured summary with:
- Environmental highlights
- Social highlights  
- Governance highlights

That's it. Nothing fancy.

## Built With AI

This project was created with assistance from an AI coding assistant (Kiro). The AI helped with:
- Code structure and implementation
- Documentation and comments
- Best practices for API usage

The human (me) provided the requirements, made decisions, and reviewed everything.

## Setup

1. Clone this repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your OpenAI API key:
   ```
   cp .env.example .env
   ```
4. Edit `.env` and add your key

## Usage

Run the script:
```
python summarize_esg.py
```

When prompted, enter the path to your text file (try `example_report.txt` to test).

The summary will print to your terminal.

## Limitations

This is a learning project with real constraints:

- **Only handles plain text** - No PDF parsing, no web scraping
- **Costs money** - Each summary uses OpenAI API credits
- **No validation** - The LLM might miss important details or hallucinate
- **No output saving** - Results only print to terminal
- **Basic error handling** - Will fail ungracefully in some cases
- **English only** - Not tested with other languages

## Future Improvements

If I continue this project, I might add:
- PDF parsing with PyPDF2 or similar
- Save summaries to JSON or markdown files
- Support for multiple LLM providers (Anthropic, local models)
- Comparison of multiple reports
- Cost tracking and token usage stats
- Better prompt engineering for accuracy

## Why This Exists

I wanted to:
1. Learn how to integrate LLMs into a real tool
2. Practice transparent AI development
3. Build something small and functional, not impressive
4. Share an honest example of AI-assisted coding

## License

MIT - Do whatever you want with this code.
