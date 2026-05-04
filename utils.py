import random


def read_notes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        notes = [line.rstrip("\n") for line in f.readlines()]
        return notes, len(notes)


def write_note(file_path, user_note):
    if not user_note or user_note.strip() == "":
        print("Error: Cannot add an empty note.")
        return False

    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n" + user_note.strip())
    return True


def pick_random_note(notes_list):
    if not notes_list:
        return "No notes available. Add some with !add <note>"

    random_int = random.randrange(len(notes_list))
    return notes_list[random_int]


def list_notes(notes_list):
    if not notes_list:
        print("No notes available.")
        return

    for i, note in enumerate(notes_list, 1):
        print(f"{i}. {note}")


def delete_note(file_path, note_index):
    with open(file_path, "r", encoding="utf-8") as f:
        notes = f.readlines()

    if note_index < 1 or note_index > len(notes):
        print(f"Error: Note index {note_index} is out of range (1-{len(notes)})")
        return False

    deleted_note = notes.pop(note_index - 1).strip()

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(notes)

    print(f"Deleted note: {deleted_note}")
    return True
