# AI Email Automation System

A working Python prototype that demonstrates how an email automation workflow can:

- read email data
- summarize messages
- classify emails
- extract tasks
- generate draft replies

## Overview

This project is a simplified proof-of-concept for an AI-powered email assistant.

The script reads sample email data from a JSON file, processes each email, and prints:

- sender
- subject
- summary
- classification
- extracted tasks
- draft reply

This demonstrates the core logic behind a larger system that could later connect to:

- Microsoft Outlook via Microsoft Graph API
- OpenAI for LLM-based classification and summarization
- Google Sheets for task tracking

## Files

- `main.py` → runs the email workflow
- `sample_data/emails.json` → sample emails used as input
- `requirements.txt` → project dependencies

## How to Run

Clone the repository and run:

```bash
python main.py
