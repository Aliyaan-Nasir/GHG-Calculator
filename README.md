# GHG Report Summarizer

A minimal Python tool that summarizes ESG (Environmental, Social, Governance) and sustainability reports.

## What This Does

Takes a plain text ESG report and generates a structured summary with:
- Environmental highlights
- Social highlights  
- Governance highlights

That's it. Nothing fancy.

## Setup

1. Clone this repo  
2. Install dependencies:
3. Copy `.env.example` to `.env` and add your API key:
4. Edit `.env` and add your key

## Usage

Run the script:
When prompted, enter the path to your text file (try `example_report.txt` to test).

The summary will print to your terminal.

## Limitations

This is a small learning project with clear constraints:

- **Only handles plain text** — no PDF parsing or web scraping  
- **API dependent** — each run consumes API credits  
- **No validation** — summaries may miss details or be inaccurate  
- **No output saving** — results print to the terminal only  
- **Basic error handling** — not hardened for edge cases  
- **English only** — not tested on other languages  

## Future Improvements

Possible next steps:
- Add PDF parsing
- Save summaries to JSON or Markdown
- Support multiple model providers
- Compare summaries across reports
- Add basic cost or token tracking
- Improve prompt quality for consistency

## Why This Exists

This project was built to:
1. Explore text summarization in a practical context  
2. Practice building small, focused tools  
3. Keep scope minimal and understandable  
4. Share a simple, functional example  

## License

MIT — free to use, modify, or extend.
