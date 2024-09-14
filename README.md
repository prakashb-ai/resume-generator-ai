# LinkedIn Resume to HTML

## Overview

This project provides a web application for converting LinkedIn PDF resumes into HTML format using FastAPI and OpenAI's API and Google Gemini AI

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/resume-generator-ai.git
   cd resume-generator-ai
   ```

2. Create virtual env and install requirements
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt 
    ```

3. Duplicate the file .env_example and rename it to .env and add API keys of AI Providers
    - OpenAI: https://platform.openai.com/api-keys
    - Google Gemini: https://ai.google.dev/gemini-api/docs/api-key

3. Run the application
    ```bash
    uvicorn main:app --reload
    ```

Note: My limits with OPENAI_API_KEY is exhausted, so added the support of google gemini along with open ai. So, tested the entire code with Google gemini, but open ai should also work
