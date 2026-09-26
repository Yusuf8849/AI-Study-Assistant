def add_topic(topics):
    name = input("Enter topic name: ")

    topic = {
        "name": name,
        "completed": False
    }

    topics.append(topic)

    print("Topic added successfully!")


def view_topics(topics):
    if len(topics) == 0:
        print("No topics found.")
        return

    print("\n--- Your Topics ---")

    for i, topic in enumerate(topics):
        if topic["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i + 1}. {topic['name']} - {status}")


def mark_completed(topics):
    if len(topics) == 0:
        print("No topics found.")
        return

    view_topics(topics)

    try:
        choice = int(input("\nEnter topic number to mark as completed: "))

        if 1 <= choice <= len(topics):
            topics[choice - 1]["completed"] = True
            print("Topic marked as completed!")
        else:
            print("Invalid topic number.")

    except ValueError:
        print("Please enter a valid number.")


def search_topic(topics):
    search = input("Enter topic to search: ").lower()

    found = False

    for topic in topics:
        if search in topic["name"].lower():

            if topic["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(f"- {topic['name']} ({status})")
            found = True

    if not found:
        print("No matching topic found.")


def show_progress(topics):
    total = len(topics)

    completed = 0

    for topic in topics:
        if topic["completed"]:
            completed += 1

    pending = total - completed

    print("\n--- Study Progress ---")
    print("Total topics:", total)
    print("Completed:", completed)
    print("Pending:", pending)

    if total > 0:
        progress = (completed / total) * 100
        print(f"Progress: {progress:.1f}%")
    else:
        print("Progress: 0%")