# CS Concepts Visualized

## Description

A web-based application designed to visually and interactively introduce users to core concepts in Computer Science, particularly focusing on the C programming language. The project integrates multiple technologies for an immersive learning experience and is intended for personal and educational use.

### Backend:
- Flask
- Python
- SQL (SQLite3)

### Frontend:
- JavaScript
- CSS
- HTML

This application includes multiple interactive modules that simplify learning fundamental CS topics such as arrays, loops, conditionals, recursion, and more. It includes a login-based quiz functionality, real-time algorithm visualization, Blockly workspace integration, and dynamic C code examples formatted for clarity.

## Table of Contents

1. HTML Templates
2. Static Files and Styling
3. Features
4. API Usage
5. Algorithm and Concept Visualization
6. Installation
7. Usage

## 1. HTML Templates

The app uses 19 HTML templates for different functionalities, including:

- **layout.html** – Core design and API script references.
- **index.html** – Landing page with instructions.
- **apology.html** – Error rendering with messages.
- **login.html / register.html** – User authentication.
- **algorithms.html** – Algorithm explanations and links to visualization.
- **arrays.html / cipher.html** – Explanation and dynamic Caesar Cipher demo.
- **commands.html / conditionals.html / functions.html / loops.html / operators.html / recursion.html / types.html / variables.html** – Interactive educational pages with examples and visualizations.
- **quiz.html / scores.html** – Quiz interface and score tracking.
- **sort.html** – Real-time sort algorithm visualization.

## 2. Static Files and Styling

- Two main CSS files: one for layout and one for the quiz interface.
- JavaScript logic housed in **script.js** for quizzes and visual interactions.
- Dark theme design prioritizing accessibility and reduced eye strain.
- Syntax highlighting via **highlight.js**.
- Extensive use of **Bootstrap** for UI components.
- Custom ASCII art integrated for fun aesthetics.

## 3. Features

- Full-stack app with **Flask** handling backend logic.
- RESTful API handling using Flask and `jsonify`.
- Session-based login system using cookies and **flask-sessions**.
- User authentication with password hashing via `generate_password_hash`.
- Quiz system with persistent score tracking.
- Multiple sub-applications for:
  - Encryption (Caesar Cipher)
  - Algorithm visualization (sorting)
  - Blockly-based loop workspace
  - Data visualization via Chart.js
- Dynamic user feedback and error handling using `apology()` function with [Memegen](https://memegen.link/).

## 4. API Usage

- **Bootstrap**: UI layout, accordions, buttons.
- **highlight.js**: Syntax formatting for C code.
- **Chart.js**: Variable and data visualization.
- **Blockly**: Visual block-based coding environment.
- **D3.js**: Custom algorithm animation and visualization.

## 5. Algorithm and Concept Visualization

- Real-time bubble sort and other sorting algorithm visualizations.
- Variable animations and conditional logic demos.
- Interactive Blockly workspace for loops.
- Encryption tool to visualize array and pointer usage.
- Quiz to reinforce learning through active testing.

## 6. Installation

1. Clone the repository.
2. Ensure Python and Flask are installed.
3. Install required dependencies:
   ```bash
   pip install flask
   ```
4. Run the Flask application:
   ```bash
   flask run
   ```

## 7. Usage

- Navigate to the local server URL (usually http://127.0.0.1:5000/).
- Register a new account or log in.
- Explore core CS concepts through various sections.
- Take the quiz and review your results.

---

> This project is intended to serve as an educational resource and a deployable application showcasing the integration of frontend and backend technologies for interactive learning.

