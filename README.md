# AI Data Analysis Agent

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

## Table of Contents

* [About The Project](#about-the-project)
* [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [License](#license)
* [Contact](#contact)

## About The Project

This repository hosts an **AI Data Analysis Agent** built using Streamlit, designed to facilitate interactive data exploration and analysis through natural language. This application empowers users to upload datasets and ask questions in plain English, with an underlying AI model processing the queries and providing insights or performing data manipulations.

The core idea is to democratize data analysis, making it accessible to users without deep programming or statistical knowledge, by leveraging the power of large language models (LLMs) to interpret requests and interact with data.

## Features

* **Interactive Chat Interface**: Engage with your data using a user-friendly chat interface powered by Streamlit.
* **AI-Powered Data Analysis**: Ask complex data-related questions in natural language and receive intelligent responses.
* **Data Upload Capability**: Easily upload your own datasets (e.g., CSV files) for analysis.
* **System Prompt Customization**: Utilizes a `SYSTEM_PROMPT.txt` to guide the AI's behavior and focus on data analysis tasks.
* **Extensible**: Designed with a modular structure, allowing for future enhancements and integration of different AI models or data sources.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Ensure you have Python 3.9 or higher installed on your system. You will also need `pip` for package management.

### Installation

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/pforpav/ai-data-analysis-agent.git](https://github.com/pforpav/ai-data-analysis-agent.git)
    cd ai-data-analysis-agent
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is assumed. If not present, you'll need to create one with `streamlit`, `pandas`, and any LLM client libraries you use, e.g., `openai`, `google-generativeai`.)*

4.  **Set up your API Key:**
    The application will likely require an API key for the underlying AI model (e.g., OpenAI, Google Gemini).
    Create a `.env` file in the root directory of the project and add your API key:
    ```
    OPENAI_API_KEY="your_openai_api_key_here"
    # Or for Google Gemini:
    # GOOGLE_API_KEY="your_google_api_key_here"
    ```
    *(Note: The exact environment variable name will depend on the LLM library used in `main.py` or the Streamlit apps.)*

## Usage

To run the Streamlit application:

```bash
streamlit run streamlit-data-analysis-chatbot.py
```

Once the application starts, it will open in your default web browser. You can then:

1. Upload your dataset (e.g., a CSV file).
2. Type your data analysis questions into the chat input.
3. Receive insights and analysis from the AI agent.

## Project Structure
```
ai-data-analysis-agent/
├── .gitignore
├── LICENSE
├── README.md                 # This file
├── SYSTEM_PROMPT.txt         # Defines the AI agent's persona and instructions
├── basic-streamlit-app.py    # A basic Streamlit app example (optional, might be for testing)
├── main.py                   # Core logic for the AI agent and data processing
├── streamlit-data-analysis-chatbot.py # The main Streamlit application for the chatbot
└── pages/                    # Directory for multi-page Streamlit apps (if used)
```

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
Pava - pava.rani96@gmail.com
Project Link: https://github.com/pforpav/ai-data-analysis-agent
