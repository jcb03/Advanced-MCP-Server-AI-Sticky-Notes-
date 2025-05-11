from mcp.server.fastmcp import FastMCP
import os


#create an instance of FastMCP
mcp = FastMCP("AI Stick Notes") # name of the app

# saving file in this directory only
NOTES_FILE= os.path.join(os.path.dirname(__file__), "notes.txt") # file to store notes

# check if the file exists
def ensure_file_exists():
    # check if the file exists
    if not os.path.exists(NOTES_FILE):
        # create the file if it doesn't exist
        with open(NOTES_FILE, "w") as f:
            f.write("")

# function to add a note
@mcp.tool()
def add_note(message: str) -> str: #specify type for parameters
    """
    Append a new note to the sticky note file.

    Args:
        message (str): The note to be added.
    Returns:
        str: A message indicating the note was added successfully.

    """
    ensure_file_exists()
    # open the file in append mode
    with open(NOTES_FILE, "a") as f:
        # write the note to the file
        f.write(message + "\n")
    return "Note added successfully!"
# function to get all notes


# tool to read all notes
@mcp.tool()
def read_notes() -> str:
    """
    Read all notes from the sticky note file.

    Returns:
        str: All notes in the file, separated by new lines.
    """
    ensure_file_exists()
    # open the file in read mode
    with open(NOTES_FILE, "r") as f:
        # read the notes from the file
        content = f.read().strip()
    return content or "No notes yet."

# resource to get the file
@mcp.resource("notes://latest")
def get_notes_notesfile() -> str:
    """
    Get the path to the notes file.

    Returns:
        str: The path to the notes file.
    """
    ensure_file_exists()
    with open(NOTES_FILE, "r") as f:
        # read the notes from the file
        with open(NOTES_FILE, "r") as f:
            # read the notes from the file
            lines = f.readlines()
        return lines[-1].strip() if lines else "No notes yet." # return the last note

# mcp prompt to summarize the notes
@mcp.prompt()
def prompt_for_note() -> str:
    """
    Prompt the user to summarize the notes.
    
    Returns:
        str: A prompt to summarize the notes.
        if no notes exist, return a message indicating that. 
    """
    ensure_file_exists()
    with open(NOTES_FILE, "r") as f:
        content= f.read().strip()
    if not content:
        return "No notes yet."
    # prompt the user for a note
    return f"Summarize the notes: {content}" 