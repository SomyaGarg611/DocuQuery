# DocuQuery

- A robust intelligent query processing system that can handle ambiguous user queries and fetch accurate responses from a variety of data sources.
- The system is able to decide the best data source/tool to answer the query, which could range from the company's internal documents, LLM's own knowledge, or a relational database. 
- The system is also able to handle different formats of files for document analysis. Additionally, the system implements session management and context retention for a conversational user experience. 
- The system is scalable to handle a large volume of data and is efficient in providing accurate responses. The system is also user-friendly yet professional, allowing users to easily interact with it and get the information they need. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Environment Configuration](#environment-configuration)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://your-repo-url.git
   cd DocuQuery
   ```
   

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   

2. **Install Dependencies:**

   Make sure you have Python 3.7 or above, then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Set Up Environment Variables:**

   Ensure you have a `.env` file with the required variables; 


## Environment Configuration

Configure your environment variables in a `.env` file as follows:

```dotenv
POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_SERVER=your_postgres_server
POSTGRRES_PORT=your_postgres_port
POSTGRES_DB=your_postgres_db
GROQ_API_KEY=your_groq_api_key
SERP_API_KEY=your_serp_api_key
```
