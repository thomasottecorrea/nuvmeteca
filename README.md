# Internal Library Management System

## Description
This project is a web-based platform designed to manage the internal library of a company. It allows users to register, view, and track the status of books (available or loaned). Each book has a profile page displaying detailed information, including a summary and loan history. Users can also reserve books and join a waiting list for loaned books. The platform leverages AWS infrastructure, utilizing DynamoDB for database management and a serverless architecture for scalability and performance. The frontend is built with Streamlit for simplicity, and the backend is implemented using FastAPI.

## Features
- Register and edit book information (title, author, category)
- View the status of books (available or loaned)
- Book profile page with details and loan history
- Reserve books and join a waiting list
- Authentication using AWS Cognito
- Serverless architecture with AWS Lambda and API Gateway
- Database management using DynamoDB

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Database**: DynamoDB
- **Authentication**: AWS Cognito
- **Infrastructure**: AWS Lambda, API Gateway, CloudWatch
- **Version Control**: GitHub

## Getting Started

### Prerequisites
- Python 3.7+
- AWS Account
- AWS CLI configured
- Git

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/internal-library-management-system.git
   cd internal-library-management-system
   
2. **Clone the repository:**
   ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt

4.  Set up AWS resources:

    -Configure DynamoDB tables
    -Set up AWS Cognito for user authentication
    -Deploy AWS Lambda functions and API Gateway

### Running the Application
1. **Start the FastAPI server:**
   ```bash
   uvicorn app.main:app --reload

2. **Run the streamlit front-end:**
   ```bash
     streamlit run app/frontend.py

3. **Access the Application:**
   -Open your web browser and go to http://localhost:8501


