 # Python Developer Assessment
 This repository is for my developer assessment tasks

 # My First Python API Project

## 1. Project Overview
This project serves as my introduction to professional Python development. Throughout this assessment, I built a solid foundation in writing clean, structured code, managing projects with version control (Git & GitHub), implementing error handling, and interacting with live web servers.

The core application handles real-world programming workflows, ranging from formatting scripts according to strict industry guidelines to fetching and dynamically filtering user data from a mock REST API server.

---

## 2. Completed Tasks
Here is the breakdown of the engineering milestones achieved during this project, linked to their respective source files:

* **Task 1: Environment & VCS Setup**
    * Set up a local Python environment, initialized Git for version control, and linked the repository to GitHub.
    * Created the baseline entry-point script: [`hello.py`](https://github.com/ivanma-blip/python-dev-assessment/blob/a783cf20b420a45dfbe4b4efffd9f52898942360/hello.py)
* **Task 2: Code Style & Linting**
    * Configured **Black** (code formatter) and **Flake8** (linter).
    * Fixed styling conflicts, resolved permission errors, and manually handled implicit string continuations for maximum line-length compliance.
    * Files addressed: [`bad_style.py`](https://github.com/ivanma-blip/python-dev-assessment/blob/a783cf20b420a45dfbe4b4efffd9f52898942360/bad_style.py) and [`book_store.py`](https://github.com/ivanma-blip/python-dev-assessment/blob/a783cf20b420a45dfbe4b4efffd9f52898942360/book_store.py)
* **Task 3: Error Handling & Debugging**
    * Deeply explored data structures (Lists vs. Strings) to prevent index lookup mistakes.
    * Implemented exception-driven code patterns to safely handle unexpected data structures.
    * Files addressed: [`debug_errors.py`](https://github.com/ivanma-blip/python-dev-assessment/blob/a783cf20b420a45dfbe4b4efffd9f52898942360/debug_errors.py) and [`dsa_challenges.py`](https://github.com/ivanma-blip/python-dev-assessment/blob/a783cf20b420a45dfbe4b4efffd9f52898942360/dsa_challenges.py)
* **Task 4: Basic API Interaction**
    * Integrated the third-party `requests` library to connect to the JSONPlaceholder API.
    * Built structured `if/else` checks for HTTP status codes alongside localized exception handling to safely parse, filter, and output user details.
    * Primary client file: [`api_client.py`](https://github.com/ivanma-blip/python-dev-assessment/blob/a783cf20b420a45dfbe4b4efffd9f52898942360/api_client.py)

---

## 3. Running the Code

### Prerequisites
Ensure Python is installed on your machine. Next, install the necessary dependencies and development tools via your terminal:

```bash
python -m pip install requests black flake8

---

## 4. Reflections

4.1 What I Found Most Challenginggit 
 Coming from a background as a Java/Kotlin Android developer, adjusting to Python's syntax was the biggest hurdle. Being used to strictly typed languages (strogo tipirani jezici), Python's dynamic typing and heavy reliance on whitespace indentation felt completely unnatural at first. Debugging errors like TypeError: string indices must be integers required a shift in mindset, forcing me to carefully track data types manually since the compiler wasn't doing it for me up front.Furthermore, I made a mistake in a few of my final commit messages by accidentally forgetting to include the relevant task numbers—a great reminder of the importance of disciplined version control habits.

4.2 What I Found Most Interesting
The most enjoyable part of the project was working within the VS Code environment. The IDE's next-line code predictions were incredibly accurate and streamlined my workflow. I also loved utilizing ecosystem tools like Black and Flake8; having automated style linters that instantly pinpoint errors or automatically format layout discrepancies made managing a clean codebase exceptionally fun and satisfying.

4.3 One Thing I Learned or Improved
The biggest takeaway from this assessment was learning how easy it is to spin up and manage a lightweight, isolated local environment in Python. I didn't know it was possible to get an entirely separate development environment running so quickly and smoothly with just a few simple terminal commands. This is a massive contrast to the heavy setup requirements of Android Studio, and it greatly improved my appreciation for Python's agility.