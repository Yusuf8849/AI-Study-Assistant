from data_manager import load_topics, save_topics
from study_manager import (
    add_topic,
    view_topics,
    mark_completed,
    search_topic,
    show_progress
)
from utils import show_menu, get_choice


def main():

    topics = load_topics()

    while True:

        show_menu()

        choice = get_choice()

        if choice == "1":
            add_topic(topics)
            save_topics(topics)

        elif choice == "2":
            view_topics(topics)

        elif choice == "3":
            mark_completed(topics)
            save_topics(topics)

        elif choice == "4":
            search_topic(topics)

        elif choice == "5":
            show_progress(topics)

        elif choice == "6":
            save_topics(topics)
            print("Goodbye! Keep studying!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()