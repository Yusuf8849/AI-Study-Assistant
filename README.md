# AI Study Assistant

A simple command-line study assistant built with Python that helps users manage study topics, track completion, search topics, and monitor study progress.

> **Version:** v0.1
> **Current Stage:** Python CLI application
> **AI APIs:** Not used yet

---

## Overview

The **AI Study Assistant** is a beginner-friendly Python project designed to practice real-world programming concepts while building the foundation for a future AI-powered study assistant.

The current version is a command-line application that allows users to:

* Add study topics
* View all topics
* Mark topics as completed
* Search for topics
* Track study progress
* Save and reload data using JSON

The project is intentionally built without AI APIs in v0.1. The goal of this version is to establish a clean application structure, persistent data storage, and core Python functionality before introducing AI features.

---

## Features

### 📚 Topic Management

* Add new study topics
* View all saved topics
* Mark topics as completed
* Search for topics by name

### 📊 Progress Tracking

The application displays:

* Total number of topics
* Completed topics
* Pending topics
* Overall completion percentage

### 💾 Persistent Data

Topics are stored in a JSON file so that data is not lost when the application is closed.

The application automatically:

* Loads existing topics when it starts
* Saves changes to `topics.json`

### 🧩 Modular Structure

The project is divided into multiple Python modules based on responsibility:

* Study logic
* Data management
* Utility functions
* Application control

---

## Tech Stack

### Language

* **Python 3**

### Concepts & Technologies

* Python Functions
* Lists
* Dictionaries
* Loops
* Conditional Statements
* File Handling
* JSON
* Exception Handling
* Python Modules
* `import` / `from ... import`
* Modular Programming

### Data Storage

* **JSON**

### Interface

* **Command Line Interface (CLI)**

---

## Project Structure

```text
AI-Study-Assistant/
│
├── main.py
├── data_manager.py
├── study_manager.py
├── utils.py
│
├── data/
│   └── topics.json
│
└── README.md
```

### File Responsibilities

#### `main.py`

The main entry point of the application.

Responsible for:

* Starting the application
* Loading topics
* Displaying the menu
* Handling user choices
* Calling the appropriate functions

#### `study_manager.py`

Contains the main study-related functionality.

Responsible for:

* Adding topics
* Viewing topics
* Marking topics as completed
* Searching topics
* Calculating study progress

#### `data_manager.py`

Handles persistent data storage.

Responsible for:

* Loading topics from JSON
* Saving topics to JSON
* Handling missing data files

#### `utils.py`

Contains reusable utility functions such as:

* Displaying the application menu
* Getting user input

#### `data/topics.json`

Stores the user's study topics and completion status.

Example:

```json
[
    {
        "name": "Python Functions",
        "completed": true
    },
    {
        "name": "Pandas",
        "completed": false
    }
]
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Study-Assistant.git
```

### 2. Open the project directory

```bash
cd AI-Study-Assistant
```

### 3. Run the application

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

### Requirements

Python 3.x is required.

No external Python packages are required for the current version.

---

## Screenshots

### Main Menu

Add a screenshot of the application's main menu here.

```markdown
![Main Menu](screenshots/main-menu.png)
```

### Adding a Topic

```markdown
![Add Topic](screenshots/add-topic.png)
```

### Study Progress

```markdown
![Study Progress](screenshots/progress.png)
```

> **Note:** Create a `screenshots` folder in the repository and place your screenshots inside it.

Recommended structure:

```text
AI-Study-Assistant/
│
├── screenshots/
│   ├── main-menu.png
│   ├── add-topic.png
│   └── progress.png
│
├── main.py
├── data_manager.py
├── study_manager.py
├── utils.py
├── data/
│   └── topics.json
│
└── README.md
```

---

## What I Learned

This project helped me strengthen my understanding of Python and basic software development practices.

### Python Fundamentals

* Working with lists and dictionaries
* Loops and conditional statements
* Functions and parameters
* Returning values
* Local and global variables

### File Handling

Learned how to:

* Open files using `open()`
* Read and write files
* Use `with open(...)`
* Work with JSON data
* Persist application data between sessions

### Exception Handling

Learned how to handle common runtime errors using:

```python
try:
    ...
except:
    ...
```

For example, handling a missing JSON file using `FileNotFoundError`.

### Modules

Learned how to split a Python application into multiple files and use:

```python
import
```

and:

```python
from ... import ...
```

### Software Structure

Learned the concept of **separation of concerns** by giving different files different responsibilities.

Instead of putting everything inside one Python file, the application is organized into:

```text
Application Logic
       ↓
Study Management
       ↓
Data Management
       ↓
JSON Storage
```

---

## Future Improvements

The current version is intentionally simple. Future versions will gradually introduce more advanced functionality.

### v0.2 — Better Study Management

* Add topic categories
* Add priority levels
* Add deadlines
* Add notes for each topic
* Add edit and delete functionality
* Improve input validation

### v0.3 — Better User Experience

* Improved CLI interface
* Better progress visualization
* Study streak tracking
* Daily study goals
* More detailed statistics

### Future AI Features

Eventually, the project can evolve into a true AI-powered study assistant with features such as:

* AI-generated study plans
* Personalized learning recommendations
* Topic explanations
* AI-generated quizzes
* Question answering
* Automatic revision schedules
* Progress-based recommendations
* Natural-language interaction

The AI functionality will be introduced gradually after the core application architecture is stable.

---

## Project Goal

The long-term goal of this project is to evolve from a simple Python CLI application into a **personal AI-powered learning assistant**.

This project is being developed incrementally to understand the engineering foundations behind AI products rather than simply connecting an AI API to a basic interface.

---

## License

This project is currently intended as a personal learning and portfolio project.
