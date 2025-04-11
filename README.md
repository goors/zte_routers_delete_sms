# SMS Deletion Script for ZTE Modem

This Python script allows you to fetch SMS messages from a ZTE modem and delete them automatically.

### I can do same in ui so why this repository exists?

I created this repository because I encountered performance issues with the ZTE modem's UI when trying to manage a large number of SMS messages. The modem's interface became unresponsive and failed to open the SMS inbox when there were too many messages.

Despite being able to perform the same actions (like deleting messages) through the UI, the UI simply couldn't handle the large volume of messages, causing frustration and inefficiency. This repository provides an alternative way to interact with the modem via API calls, automating the process of managing and deleting SMS messages directly without relying on the UI.
 
## Requirements

- Python 3.9 or higher
- `requests` library

## Instructions

### Step 1: Set Up Virtual Environment

To isolate your dependencies and avoid conflicts with other projects, it's recommended to use a virtual environment.

1. Open a terminal/command prompt.
2. Navigate to the directory where you want to store the project.
3. Run the following command to create a virtual environment:

    ```bash
    python3.9 -m venv venv
    ```

### Step 2: Activate Virtual Environment

#### On Windows:
1. After creating the virtual environment, activate it by running:

    ```bash
    .\venv\Scripts\activate
    ```

#### On macOS/Linux:
1. Activate the virtual environment by running:

    ```bash
    source venv/bin/activate
    ```

### Step 3: Install Dependencies

You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```


### Step 4: Run script
```bash
python delete_messages.py
```
