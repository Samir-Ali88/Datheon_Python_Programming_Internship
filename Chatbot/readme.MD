# FAQ Chatbot

A simple rule-based chatbot that runs in the terminal. It answers questions from a JSON file, can handle more than one question in a single message, and learns new answers when it doesn't know something.

## Features

- Answers questions using fuzzy matching, so small typos still work
- Keyword matching with stop words and synonyms (for example "opening", "timing" and "hours" all mean the same thing)
- Multi-question messages: ask about two topics at once and it answers both
- Greeting and exit detection
- Teach mode: if the bot doesn't know the answer, you can type one in and it saves it

## Requirements

- Python 3.10 or newer (the code uses `str | None` type hints)
- No extra packages, only the standard library (`json`, `re`, `difflib`)

## Project files

```
chatbot.py        the chatbot
sample_faq.json   the knowledge base (questions, answers, greetings)
```

## How to run

```bash
python chatbot.py
```

Make sure `simple_faq.json` is in the same folder you run the command from.

## Knowledge base format

The bot loads `simple_faq.json`. It needs a list of questions and, optionally, a list of greetings. The list can be called either `questions` or `faqs`.

```json
{
  "greetings": ["hi", "hello", "hey"],
  "questions": [
    {"question": "What are your opening hours?", "answer": "We open 9am to 5pm."},
    {"question": "How do I submit my assignment?", "answer": "Upload it on the portal."},
    {"question": "When will I get my certificate?", "answer": "Within 2 weeks."}
  ]
}
```

## Example chat

```
Bot: Hi! Ask me a question, or type 'bye' to leave.
You: hello
Bot: Hello! How can I help you today?
You: What are your opening hours?
Bot: We open 9am to 5pm.
Bot: Anything else I can help with? (type 'bye' to exit)
You: Where is the library?
Bot: I don't know the answer. Can you teach me?
Type the answer or 'skip' to skip: Second floor, Block B
Bot: Thank you! I learned a new response!
You: bye
Bot: Goodbye! Have a great day.
```

## How it works

Each message goes through these steps:

1. **Clean the input.** Lowercase it and remove punctuation and extra spaces.
2. **Check for exit.** Typing `bye`, `exit` or `quit` ends the chat.
3. **Check for a greeting.** If the message is only a greeting, the bot says hello and waits for the next message.
4. **Find matches.**
   - Fuzzy match: finds the stored question that is at least 60% similar to the message.
   - Keyword match: finds every stored question that shares keywords with the message. This is what allows several questions in one message.
5. **Answer.** If either match works, the bot prints the answers. If both fail, it asks you to teach it.

## Teach mode

When the bot can't find an answer, it asks you for one. Type the answer to add it as a new question, or type `skip` to move on.

Note: new answers are saved to `knowledge_base.json`, not to the file the bot loads from. Change the save line in `chatbot.py` if you want them saved back into `simple_faq.json`.

## Customizing

- **Add more filler words:** edit `STOP_WORDS` in `chatbot.py`
- **Add more synonyms:** edit `SYNONYMS` in `chatbot.py`
- **Make fuzzy matching stricter or looser:** change `cutoff=0.6` in `find_best_match` (higher is stricter)
- **Make keyword matching stricter or looser:** change `0.3` in `find_keyword_matches`