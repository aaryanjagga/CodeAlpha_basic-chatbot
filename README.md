# CodeAlpha_basic-chatbot
Project Overview

This repository contains a command-line interface (CLI) chatbot developed as part of my Python development internship. The project serves as a foundational exercise in understanding control flow, user input handling, and logic implementation in Python.
The bot runs in an infinite loop, processing user inputs against a set of predefined rules to generate context-aware responses, demonstrating the core mechanics of rule-based AI.

 Technical Concepts

This project demonstrates proficiency in the following Python fundamentals:
Infinite Loops (while True): Ensuring the application runs continuously until a specific exit condition is met.
Conditional Logic (if, elif, else): Making decisions based on string matching.
Input Sanitization: Using methods like .lower() to ensure case-insensitive matching.
String Operations: Checking for substring presence using the in keyword.

The Code

Below is the core logic used in the application. Note that input is normalized to handle various capitalization styles (e.g., "Hi", "hi", "HI").
print("Chatbot Initialized...")
print("Simple chatbot app ready.")

while True:
    # Get user input and convert to lowercase for matching
    user = input("User: ").lower()

    if user in ["hey", "hi", "hello"]:
        print("Chatbot: Hi there! How are you?")
    
    elif "fine" in user or "good" in user:
        print("Chatbot: That's great! How can I help you today?")
    
    elif "what is python programming" in user:
        print("Chatbot: Python is a high-level, interpreted programming language widely used for web development and AI.")
    
    elif "bye" in user:
        print("Chatbot: Goodbye! Have a nice day.")
        break # Exit the loop
    
    else:
        print("Chatbot: Sorry, I didn't understand that. Please ask something else.")

How to Run
To execute this chatbot on your local machine:
Clone the repository:

Navigate to the directory: 
basic-python-chatbot
Run the script:
python chatbot.py



👤 Author

Developed by Aaryan Jagga Python Intern

Feedback is always welcome! Feel free to open an issue or submit a pull request.
