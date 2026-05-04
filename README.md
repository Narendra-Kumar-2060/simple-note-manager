# Note Manager CLI

A command-line note management application that lets you store, retrieve, and manage notes with ease. Comes pre-loaded with interesting facts, motivational quotes, and a touch of humor!

## Features

- Display a random note from your collection
- Add new notes with simple commands
- Delete notes by their index number
- List all notes with numbered references
- Pre-populated with 40+ interesting facts and quotes
- Persistent storage using a text file

## Tech Stack

- Python 3
- Random module
- File I/O operations

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/note-manager.git
cd note-manager

# Run the application
python main.py
```

## Usage

### Commands

| Command            | Description                 |
| ------------------ | --------------------------- |
| `!note`            | Show a random note          |
| `!add <your note>` | Add a new note              |
| `!delete <number>` | Delete a note by its number |
| `!list`            | Show all notes              |
| `!help`            | Display help message        |
| `!exit` or `!quit` | Exit the program            |

### Examples

```bash
# Start the application
python main.py

# Show a random note
Enter Command: !note

# Add a new note
Enter Command: !add Don't forget to buy groceries tomorrow

# List all notes
Enter Command: !list

# Delete note #5
Enter Command: !delete 5

# Get help
Enter Command: !help

# Exit
Enter Command: !exit
```

### Sample Output

```
Welcome to the Note Manager!
Type !help to see available commands.

Enter Command: !list
1. "The only way to do great work is to love what you do." — Steve Jobs
2. "Success is not final, failure is not fatal: It is the courage to continue that counts." — Winston Churchill
3. Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.

Enter Command: !note
"I'm not arguing, I'm just explaining why I'm right."

Enter Command: !add Remember to water the plants
Added Note: Remember to water the plants
```

## File Structure

```
note-manager/
├── main.py      # Main application logic
├── utils.py     # Helper functions (read, write, delete, list)
└── notes.txt    # Note storage file (pre-populated)
```

## Pre-loaded Content

The application comes with 40+ notes including:

- Inspirational quotes from Steve Jobs, Einstein, Roosevelt, and more
- Interesting facts (octopus hearts, Venus days, immortal jellyfish)
- Humorous one-liners
- Historical trivia

## Future Improvements

- Search notes by keyword
- Edit existing notes
- Categorize notes (quotes, facts, todos, etc.)
- Export/import notes
- Add timestamps to notes
- Tagging system
- GUI version

## License

MIT
