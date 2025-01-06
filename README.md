# Automated API Testing Framework

This project is an automated API testing framework built using Python, Pytest, and Allure for reporting. It provides a modular, reusable structure for validating APIs and includes Docker support for consistent execution across environments.

---

## Prerequisites

Before running the project, ensure the following are installed:

1. **Python**: Version 3.9 or higher
   - [Download Python](https://www.python.org/downloads/)
2. **pip**: Python's package installer
   - Update pip if needed:
     ```bash
     pip install --upgrade pip
     ```
3. **Docker** (Optional for containerized execution)
   - [Install Docker](https://docs.docker.com/get-docker/)
4. **Allure CLI**: For generating and serving test reports
   - Install Allure:
     - **macOS**:
     ```bash
     brew install allure
     ```

---

## Installation

1. **Clone the Repository**:
   ```bash
    git clone <repository-url>
    cd <repository-directory>
   
2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For macOS/Linux
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

---

## Usage
1. **Run tests**: (Run the following command from the root directory of the project)
    ```bash
    pytest --alluredir=reports/allure-results
2. View Allure reports:
    ```bash
    allure serve reports/allure-results
    ```

---

