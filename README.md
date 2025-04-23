# Project Overview

This project uses Locust to perform API load testing.
With a simple command, you can easily stress test APIs and generate detailed test reports.
---
## Installation Steps
1. Clone the repository
```bash
git clone <your-repo-link>
cd <your-project-folder>
````
2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # For Linux / Mac
venv\Scripts\activate      # For Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
````

---
## Project Structure
```bash
.gitignore            # Git ignore settings
locustfile.py         # Main Locust load test script
test_data.csv         # Test data file 
requirements.txt      # Dependency list
```

---

## How to Run the Test
Run the following command in your terminal:
```bash
locust -f locustfile.py -u 1 -t 30 -r 1 --host=https://reqres.in --headless --html locust_report.html --logfile=locust.log --csv=locust_results
```
Command Parameters Explained:

| Parameter                 | Description                          |
|---------------------------|--------------------------------------|
| -f locustfile.py          | Specify the Locust test file         |
| -u 1                      | Number of users (CCU - concurrent users) |
| -t 30                     | Total test duration: 30 seconds      |
| -r 1                      | Spawn rate: 1 user per second        |
| -host=https://regres.in   | Target server for testing            |
| --headless                | Run in non-UI mode (no web interface)|
| --html locust_report.html | Generate HTML report after the test|
| -logfile=locust.log       | Save execution logs to a file|
| --csv=locust_results      | Export test results in CSV format|

---

## Test Results
- HTML report: locust_report.html
- CSV data: locust_results_stats.csv, locust_results_failures.csv, etc.
- Log file: locust.log

After the test is complete, you can open locust_report.html in your browser to view a detailed report!

---
## Notes
- You can adjust the number of users, test duration, and spawn rate by modifying the command parameters.
- For more advanced configuration, refer to the Locust Official Documentation.


