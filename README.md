<h1 align="center">🤖 ChatBot</h1>

## Overview

Welcome to the ChatBot! This chatbot uses a knowledge base stored in a JSON file to provide answers to user questions. The ChatBot allows customization of the user experience, including selecting a name, emoji, and color for the username. Additionally, it offers various commands to manage the knowledge base and enhance interaction.

## Features

- **User Customization:** Choose your username, emoji, and text color for a personalized chat experience.
- **Knowledge Base Management:** The chatbot can learn new questions and answers, correct existing ones, and remove outdated pairs.
- **Interactive Help Menu:** Access a list of available commands to navigate the chatbot's functionalities.

## How It Works

### Knowledge Base

The knowledge base is stored in a JSON file (`knowledge_base.json`). It contains a list of questions and corresponding answers that the chatbot references to respond to user inputs.

### Core Functions

#### Loading and Saving Knowledge Base
The knowledge base is loaded from and saved to a JSON file using the following functions:

```python
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data
```
```python
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)
```
### Finding Best Matches
To find the closest matches to user questions from the knowledge base, the difflib library is used:

```python
def find_best_matches(user_question: str, questions: list[str], n: int = 3, cutoff: float = 0.6) -> list[str]:
    matches: list = get_close_matches(user_question, questions, n=n, cutoff=cutoff)
    return matches
```

## Customization
### Username
Users can select their own username by typing it when prompted. If the user wants to skip this step and use the default name "You", they can simply type "Skip".

### Emoji
Users can choose an emoji to represent their username from a list of provided options. The selected emoji will be displayed next to their username in every chat message.

### Color
Users can select a color for their username from a list of provided options. This allows for a personalized chat experience with visually distinct usernames.

## Commands
### Help
Displays a help menu with all available commands.

### Remove
Removes the last question-answer pair from the knowledge base.

### Remove <question>
Removes a specific question-answer pair from the knowledge base.

### Correct <question>
Corrects the answer to a specific question in the knowledge base.

### Exit / Quit / Bye / Goodbye
Exits the chatbot.

## Example
### Starting the ChatBot
When you start the chatbot, you'll be prompted to select a name, emoji, and color for your username. For example:

```python
[Type Skip to select 'You'] Select name: Alice
Select an emoji for your username:
1. 👽
2. 💍
3. 🦊
...
Type the number of the emoji you want: 3
Select a color for your username:
red
green
yellow
...
Type the name of the color you want: blue
```

### Interacting with the ChatBot
Type your question and the chatbot will respond based on the knowledge base. If the question isn't found, the chatbot will ask you to teach it the answer.

```python
Alice🦊 blue: What is the capital of France?
🤖 ChatBot: Paris
```

If you need help, type help to see the list of available commands.

### Correcting an Answer
If the chatbot provides an incorrect answer, you can correct it:

```python
Alice🦊 blue: correct What is the capital of France?
🤖 ChatBot: Current answer: Paris
Type the correct answer: Lyon
🤖 ChatBot: Answer updated!
```

### Removing a Question-Answer Pair
To remove the last question-answer pair or a specific pair:

```python
Alice🦊 blue: remove
🤖 ChatBot: Are you sure you want to remove the last answer? (y/N): y
🤖 ChatBot: Removed the last pair.
```

or

```python
Alice🦊 blue: remove What is the capital of France?
🤖 ChatBot: Are you sure you want to remove the question 'What is the capital of France?' (y/N): y
🤖 ChatBot: Removed the question: 'What is the capital of France?'
```

### Exiting the ChatBot
To exit the chatbot, type exit, quit, bye, or goodbye.

```python
Alice🦊 blue: goodbye
👋 ChatBot: Goodbye! Have a nice day!
```

<h2 align="center">Enjoy using your personalized ChatBot!</h2>
