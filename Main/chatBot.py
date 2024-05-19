import json
from difflib import get_close_matches


# Load the knowledge base from the file to the program
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data: dict = json.load(file)
    return data


# Save the knowledge base from the program to the file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


# Finds the best matches for the user question (multiple matches)
def find_best_matches(
    user_question: str, questions: list[str], n: int = 3, cutoff: float = 0.6
) -> list[str]:
    matches: list = get_close_matches(user_question, questions, n=n, cutoff=cutoff)
    return matches


def display_help():
    help_message = """
    \nℹ️ \033[1;34;40mChatBot Help Menu:\033[1;37;40m
    \033[1;32;40mhelp\033[1;37;40m: Display this help message
    \033[1;32;40mremove\033[1;37;40m: Remove the last question-answer pair
    \033[1;32;40mremove <question>\033[1;37;40m: Remove a specific question-answer pair
    \033[1;32;40mcorrect <question>\033[1;37;40m: Correct the answer to a specific question
    \033[1;32;40mexit / quit / bye / goodbye\033[1;37;40m: Exit the chatbot
    """
    print(help_message)


# Get the answer for the question
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


def get_user_name() -> str:
    name = input(
        "\n\033[1;33;40m[Type Skip to select 'You'] Select name: \033[1;37;40m"
    )
    if name.lower() == "skip":
        return "You"
    return name


def get_user_emoji() -> str:
    emojis = ["👽", "💍", "🦊", "🕶️", "🍄", "🍒", "🎲", "🍀", "🥚", "🎧", "🐸"]
    print("\n\033[1;33;40mSelect an emoji for your username:\033[1;37;40m")
    for i, emoji in enumerate(emojis, start=1):
        print(f"\033[1;32;40m{i}.\033[1;37;40m {emoji}")
    choice = int(
        input("\n\033[1;33;40mType the number of the emoji you want: \033[1;37;40m")
    )
    return emojis[choice - 1]


def get_user_color() -> str:
    colors = {
        "red": "\033[1;31;40m",
        "green": "\033[1;32;40m",
        "yellow": "\033[1;33;40m",
        "blue": "\033[1;34;40m",
        "magenta": "\033[1;35;40m",
        "cyan": "\033[1;36;40m",
        "white": "\033[1;37;40m",
    }
    print("\n\033[1;33;40mSelect a color for your username:\033[1;37;40m")
    for color_name, color_code in colors.items():
        print(f"{color_code}{color_name}\033[1;37;40m")
    choice = input(
        "\n\033[1;33;40mType the name of the color you want: \033[1;37;40m"
    ).lower()
    return colors.get(choice, "\033[1;37;40m")


def remove_pair(target_question: str, knowledge_base: dict):
    removed = False
    for i, q in enumerate(knowledge_base["questions"]):
        if q["question"].lower() == target_question.lower():
            del knowledge_base["questions"][i]
            removed = True
            save_knowledge_base("knowledge_base.json", knowledge_base)
            print(
                f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Removed the question: '{target_question}'"
            )
            break
    if not removed:
        print(
            f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m The question '{target_question}' does not exist."
        )


def remove_last_pair(knowledge_base: dict):
    if knowledge_base["questions"]:
        last_pair = knowledge_base["questions"].pop()
        save_knowledge_base("knowledge_base.json", knowledge_base)
        print(
            f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Removed the last pair: {last_pair}"
        )
    else:
        print("\n🤖 \033[1;34;40mChatBot:\033[1;37;40m No pairs to remove.")


def correct_answer(user_input: str, knowledge_base: dict):
    best_match = find_best_matches(
        user_input,
        [q["question"] for q in knowledge_base["questions"]],
        n=1,
        cutoff=0.6,
    )
    if best_match:
        print(
            f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Current answer: {get_answer_for_question(best_match[0], knowledge_base)}"
        )
        new_answer = input("\033[1;32;40mType the correct answer: \033[1;37;40m")
        for q in knowledge_base["questions"]:
            if q["question"] == best_match[0]:
                q["answer"] = new_answer
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print("\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Answer updated!")
                break
    else:
        print(
            "\n🤖 \033[1;34;40mChatBot:\033[1;37;40m No matching question found to correct."
        )


def chat_bot():
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")
    print(
        "\n✅ \033[1;32;40mChat bot is ready! Type 'help' or 'h' to view the list of commands\033[1;37;40m"
    )

    user_name: str = get_user_name()
    user_emoji: str = get_user_emoji()
    user_color: str = get_user_color()
    user_display: str = f"{user_emoji}{user_color} {user_name}:\033[1;37;40m"

    while True:
        user_input: str = input(f"\n{user_display} \033[1;37;40m")

        if user_input.lower() in ["bye", "goodbye"]:
            print("\n👋 \033[1;34;40mChatBot:\033[1;37;40m Goodbye! Have a nice day!")
            break

        if user_input.lower() == "exit":
            print(
                "\n👋 \033[1;34;40mChatBot:\033[1;37;40m The exit is right there! Goodbye!"
            )
            break

        if user_input.lower() == "quit":
            print("\n👋 \033[1;34;40mChatBot:\033[1;37;40m Quitting... Goodbye!")
            break

        if (
            user_input.lower() == "help"
            or user_input.lower() == "h"
            or user_input.lower() == "?"
            or user_input.lower() == "/help"
            or user_input.lower() == "/h"
            or user_input.lower() == "Help"
            or user_input.lower() == "H"
            or user_input.lower() == "/?"
        ):
            display_help()
            continue

        if user_input.lower().startswith("remove"):
            if user_input.lower() == "remove":
                confirmation = input(
                    "\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Are you sure you want to remove the last answer? (y/N): \033[1;37;40m"
                )
                if confirmation.lower() == "y":
                    remove_last_pair(knowledge_base)
                else:
                    print("\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Removal cancelled.")
            else:
                question_to_remove = user_input[7:].strip()
                confirmation = input(
                    f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Are you sure you want to remove the question '{question_to_remove}'? (y/N): \033[1;37;40m"
                )
                if confirmation.lower() == "y":
                    remove_pair(question_to_remove, knowledge_base)
                else:
                    print("\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Removal cancelled.")
            continue

        if user_input.lower().startswith("correct"):
            if user_input.lower() == "correct":
                question_to_correct = input(
                    "\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Type the question you want to correct: \033[1;37;40m"
                )
            else:
                question_to_correct = user_input[8:].strip()
            correct_answer(question_to_correct, knowledge_base)
            continue

        exact_match = next(
            (
                q
                for q in knowledge_base["questions"]
                if q["question"].lower() == user_input.lower()
            ),
            None,
        )
        if exact_match:
            print(f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m {exact_match['answer']}")
            continue

        best_matches: list[str] = find_best_matches(
            user_input, [q["question"] for q in knowledge_base["questions"]]
        )

        if best_matches:
            print(
                f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m I found multiple possible answers. Please choose the best one:"
            )
            for i, match in enumerate(best_matches, start=1):
                print(f"\033[1;32;40m{i}.\033[1;37;40m {match}")
            print(
                f"\033[1;32;40m{len(best_matches) + 1}.\033[1;37;40m None of these. Add a new answer."
            )

            choice = input(
                "\033[1;32;40mType the number or the closest question: \033[1;37;40m"
            )
            try:
                choice = int(choice)
                if choice == len(best_matches) + 1:
                    new_answer: str = input(
                        "\033[1;32;40mType the answer: \033[1;37;40m"
                    )
                    knowledge_base["questions"].append(
                        {"question": user_input, "answer": new_answer}
                    )
                    save_knowledge_base("knowledge_base.json", knowledge_base)
                    print(
                        "\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Thanks for teaching me!"
                    )
                else:
                    chosen_question = best_matches[choice - 1]
                    answer = get_answer_for_question(chosen_question, knowledge_base)
                    print(f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m {answer}")
            except (ValueError, IndexError):
                if choice in best_matches:
                    answer = get_answer_for_question(choice, knowledge_base)
                    print(f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m {answer}")
                else:
                    print(
                        "\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Invalid choice. Please try again."
                    )
        else:
            print(
                f"\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Sorry, I do not know the answer. Can you teach me?\n"
            )
            new_answer: str = input(
                '\033[1;32;40mType the answer or type "Skip" to skip: \033[1;37;40m'
            )

            if new_answer.lower() != "skip":
                knowledge_base["questions"].append(
                    {"question": user_input, "answer": new_answer}
                )
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print("\n🤖 \033[1;34;40mChatBot:\033[1;37;40m Thanks for teaching me!")


if __name__ == "__main__":
    chat_bot()
