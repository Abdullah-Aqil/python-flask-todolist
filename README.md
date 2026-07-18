# Simple Python To-Do List Engine

## Overview
This repository contains a lightweight, functional **To-Do List Application** built using Python. The primary focus of this project is fundamental **Data Management**—mastering how to manipulate structured elements inside a single collection variable and shifting them from volatile memory (RAM) into persistent disk storage.

## Engineering Architecture
The application follows standard software engineering blueprints:
* **Decoupled Layout:** The backend data engine (`app.py`) is decoupled from the user interface layout (`templates/index.html`).
* **Data Simulation:** Tasks are handled as objects within a primitive sequence array to mimic clean data records.
* **Disk Persistence:** Mitigates the volatile memory trap by serializing state information into a permanent `tasks_data.json` file.
* **Operations Matrix:** Fully supports programmatic workflows for **Adding** records, **Viewing** collections, **Removing** specific indexes, and **Exiting** the running environment securely.

## Repository File Structure
```text
├── app.py                  # Core Backend Logic Layer
├── tasks_data.json         # Permanent Disk Storage File
└── templates/              # View Architecture Directory
    └── index.html          # Web User Interface Document
```
## Usage

To use the To-Do List application, you can follow these steps:

1. Install the necessary dependencies by running the following command:

   ```bash
   pip install flask
   ```
2. Clone the repository:

```Bash
git clone <repository_url>
```
3. Navigate to the project directory:

```Bash
cd python-flask-todolist
```
4. Run the application using Python:
```Bash
python app.py
```
   
