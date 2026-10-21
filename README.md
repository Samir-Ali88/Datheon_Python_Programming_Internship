# Internship Projects

Hi! This repo holds the Python projects I built during my internship. They're small, practical, and each one taught me something different, from handling files to building a simple chatbot. Every project sits in its own folder with its own README.

## What's Inside

| Project | What it is |
|---------|-----------|
| **Hangman** | A word-guessing game you play in the terminal |
| **File Organizer** | A script that tidies a messy folder by sorting files by type |
| **Chatbot** | A simple chatbot that answers questions from a FAQ file |

## Repository Structure

```
Internship/
├── Hangman/
│   ├── hangman.py
│   └── README.md
├── Organizer/
│   ├── organizer.py
│   └── README.md
├── Chatbot/
│   ├── chatbot.py
│   ├── sample_faq.json
│   └── README.md
└── README.md
```

## The Projects

### Hangman
The classic game, played in the terminal. You guess one letter at a time and try to uncover the hidden word before you run out of attempts.

### File Organizer
Ever opened a folder and found a pile of random files? This script fixes that. It looks at each file's extension and moves it into a matching folder: Documents, Images, Videos, Archives, Code, or Installers. When it's done, it tells you how many files it moved.

### Chatbot
A simple chatbot that replies to user questions. Its answers come from `sample_faq.json`, a file of sample questions and responses, so you can change what the bot knows just by editing that file.

## What I Learned

- Writing clean Python with loops, conditions, and functions
- Working with files and folders using `os` and `shutil`
- Reading and using data from JSON files
- Handling errors so a script doesn't crash on the first problem
- Taking user input and building simple command-line programs

## Thanks for Stopping By

This is a learning project, so feedback and suggestions are always welcome. Feel free to open an issue or send a pull request.

## License

Free to use and modify for personal or educational purposes.
