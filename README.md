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
   git clone https://github.com/SomyaGarg611/DocuQuery.git
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

## Contributing
We welcome contributions to make DocuQuery even better! Here’s how you can get involved:

1. **Fork the Repository**: Click the "Fork" button at the top right of this page to create a copy of the repository in your GitHub account.

2. **Clone the Repository**: Clone your forked repository to your local machine using `git clone https://github.com/SomyaGarg611/DocuQuery.git`.

3. **Create a Branch**: Create a new branch for your feature or bug fix using git checkout -b your-branch-name.

4. **Make Your Changes**: Implement your feature or bug fix.

5. **Commit Your Changes**: Commit your changes with a descriptive commit message using git commit -m "Description of your changes".

6. **Push to the Branch**: Push your changes to your forked repository using git push origin your-branch-name.

7. **Create a Pull Request**: Go to the original repository on GitHub and create a pull request to merge your changes.
