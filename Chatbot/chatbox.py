import json
import re
from difflib import get_close_matches


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


STOP_WORDS = {
    "a", "an", "the", "is", "are", "am", "do", "does", "did", "i", "my", "me",
    "you", "your", "we", "our", "of", "to", "for", "in", "on", "at", "and",
    "or", "what", "when", "how", "will", "can", "please", "about", "tell",
}

# different words, same meaning
SYNONYMS = {
    "open": "hour", "opening": "hour", "timing": "hour", "time": "hour",
    "upload": "submit", "send": "submit",
    "get": "receive", "certification": "certificate",
}

EXIT_PATTERN = re.compile(r"\b(bye|exit|quit)\b")


def normalize_text(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def extract_keywords(text):
    keywords = set()
    for word in re.findall(r"[a-z0-9']+", text):
        if word in STOP_WORDS:
            continue
        if word.endswith("s") and len(word) > 3:
            word = word[:-1]
        keywords.add(SYNONYMS.get(word, word))
    return keywords


def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None


# more than one result means the user asked about several things
def find_keyword_matches(clean_input, knowledge_base):
    user_keywords = extract_keywords(clean_input)
    found = []
    for q in knowledge_base["questions"]:
        question_keywords = extract_keywords(normalize_text(q["question"]))
        shared = user_keywords & question_keywords
        if shared and len(shared) / len(question_keywords) >= 0.3:
            found.append(q["question"])
    return found


def is_exit_command(clean_input):
    return bool(EXIT_PATTERN.search(clean_input))


def is_greeting(clean_input, greetings):
    return any(re.search(rf"\b{re.escape(g)}\b", clean_input) for g in greetings)


def chatbot():
    knowledge_base = load_knowledge_base('sample_faq.json')

    # sample file uses "faqs" instead of "questions"
    if "questions" not in knowledge_base:
        knowledge_base["questions"] = knowledge_base.get("faqs", [])

    greetings = knowledge_base.get('greetings', [])

    state = 'greeting'
    print("Bot: Hi! Ask me a question, or type 'bye' to leave.")

    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        clean_input = normalize_text(user_input)

        if is_exit_command(clean_input):
            state = 'exit'
            print('Bot: Goodbye! Have a great day.')
            break

        if not clean_input:
            print('Bot: Please type something so I can help.')
            continue

        if is_greeting(clean_input, greetings):
            print('Bot: Hello! How can I help you today?')
            state = 'intent'
            if clean_input in greetings:
                continue

        state = 'intent'
        keyword_matches = find_keyword_matches(clean_input, knowledge_base)
        best_match = find_best_match(
            user_input, [q['question'] for q in knowledge_base['questions']]
        )

        if best_match:
            print(f'Bot: {get_answer_for_question(best_match, knowledge_base)}')
            for question in keyword_matches:
                if question != best_match:
                    print(f'Bot: {get_answer_for_question(question, knowledge_base)}')
            state = 'resolution'
        elif keyword_matches:
            for question in keyword_matches:
                print(f'Bot: {get_answer_for_question(question, knowledge_base)}')
            state = 'resolution'
        else:
            print("Bot: I don't know the answer. Can you teach me?")
            new_answer = input("Type the answer or 'skip' to skip: ")

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append(
                    {"question": user_input, "answer": new_answer}
                )
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print('Bot: Thank you! I learned a new response!')

        if state == 'resolution':
            print("Bot: Anything else I can help with? (type 'bye' to exit)")
            state = 'intent'


if __name__ == '__main__':
    chatbot()