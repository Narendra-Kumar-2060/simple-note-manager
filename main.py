import sys
import utils


def display_help():
    print("\n" + "=" * 50)
    print("AVAILABLE COMMANDS:")
    print("  !note              - Show a random note")
    print("  !add <your note>   - Add a new note")
    print("  !delete <number>   - Delete a note by its number")
    print("  !list              - Show all notes")
    print("  !help              - Show this help message")
    print("  !exit or !quit     - Exit the program")
    print("=" * 50 + "\n")


def main():
    note_path = "data.txt"
    notes, note_count = utils.read_notes(note_path)

    print("Welcome to the Note Manager!")
    print("Type !help to see available commands.\n")

    while True:
        usr_input = input("Enter Command: ").strip()

        if not usr_input:
            continue

        usr_data = usr_input.split()
        usr_cmd = usr_data[0].lower()

        if usr_cmd == "!note":
            print("\n" + utils.pick_random_note(notes) + "\n")

        elif usr_cmd == "!add":
            if len(usr_data) < 2:
                print("Error: Please provide note content. Usage: !add <your note>")
                continue

            input_note = " ".join(usr_data[1:])
            if utils.write_note(note_path, input_note):
                print(f"Added Note: {input_note}")
                notes, note_count = utils.read_notes(note_path)

        elif usr_cmd == "!delete":
            if len(usr_data) < 2:
                print("Usage: !delete <number>")
                continue

            try:
                note_index = int(usr_data[1])
                if utils.delete_note(note_path, note_index):
                    notes, note_count = utils.read_notes(note_path)
            except ValueError:
                print("Error: Please provide a valid number for delete command")

        elif usr_cmd == "!list":
            utils.list_notes(notes)

        elif usr_cmd == "!help":
            display_help()

        elif usr_cmd in ["!exit", "!quit"]:
            print("Goodbye!")
            sys.exit(0)

        else:
            print(f"Unknown command: '{usr_cmd}'")
            print("Type !help to see available commands.")


if __name__ == "__main__":
    main()