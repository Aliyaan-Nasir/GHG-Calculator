"""
ESG Report Summarizer
A minimal tool that uses an LLM to summarize sustainability reports.
Built with AI assistance - see README for details.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv


def load_report(file_path):
    """
    Load a plain text report from a file.
    
    Args:
        file_path: Path to the text file
        
    Returns:
        String containing the report text
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


def summarize_esg_report(report_text, api_key):
    """
    Use an LLM to generate a structured ESG summary.
    
    Args:
        report_text: The full text of the ESG report
        api_key: OpenAI API key
        
    Returns:
        Structured summary as a string
    """
    client = OpenAI(api_key=api_key)
    
    # Simple, direct prompt - no fancy engineering
    prompt = f"""Please analyze this ESG/sustainability report and provide a structured summary with these three sections:

1. Environmental Highlights
2. Social Highlights  
3. Governance Highlights

Keep each section brief (2-4 bullet points). Focus on concrete facts and commitments.

Report text:
{report_text}
"""
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using cheaper model - good enough for summaries
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes ESG reports clearly and concisely."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3  # Lower temperature for more consistent summaries
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error calling LLM: {e}")
        return None


def main():
    """
    Main function - loads environment, reads report, generates summary.
    """
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        print("Please copy .env.example to .env and add your API key")
        return
    
    # Get report file path from user
    file_path = input("Enter the path to your ESG report (text file): ").strip()
    
    # Load the report
    print("\nLoading report...")
    report_text = load_report(file_path)
    
    if not report_text:
        return
    
    # Generate summary
    print("Generating summary with LLM...\n")
    summary = summarize_esg_report(report_text, api_key)
    
    if summary:
        print("=" * 60)
        print("ESG REPORT SUMMARY")
        print("=" * 60)
        print(summary)
        print("=" * 60)
    else:
        print("Failed to generate summary.")


if __name__ == "__main__":
    main()
