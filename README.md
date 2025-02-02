# SQL Chat Assistant

## Overview
SQL Chat Assistant is a Streamlit-based web application that allows users to interact with a conversational AI to generate and debug SQL queries. The assistant is powered by the DeepSeek API via OpenRouter, enabling intelligent query generation and database-related discussions.

## Features
- **SQL Query Generation**: Generate SQL queries based on natural language input.
- **Query Debugging**: Identify and fix errors in SQL queries.
- **User-Friendly Interface**: Built using Streamlit for a seamless experience.
- **Data Analysis Support**: Supports Pandas integration for handling tabular data.

## Tech Stack
- **Backend Model**: DeepSeek API via OpenRouter
- **Frontend**: Streamlit
- **Programming Language**: Python

## Installation
To install and set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sql-chat-assistant.git
   cd sql-chat-assistant
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies
The following Python libraries are used:
```txt
openai==1.61.0
pandas==2.2.3
streamlit==1.41.1
tabulate==0.9.0
```

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Enter natural language queries to generate SQL statements.
3. Debug and refine queries with AI assistance.

## Configuration
- Ensure you have an API key for OpenRouter’s DeepSeek API.
- Set the API key in an environment variable or a configuration file.

## Contributing
Feel free to submit issues and pull requests to improve the project.

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, reach out via [your email or GitHub profile].
