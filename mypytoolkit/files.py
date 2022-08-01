"""
Working with files.
"""
import os


class Document:
    """Document object with directory and contents attributes."""
    def __init__(self, path: str):
        # Ensure path exists
        if not os.path.exists(path):
            raise FileNotFoundError("No file could be found at the provided path.")
        
        self.path = path

        def contents(self) -> str:
            with open(self.directory, 'r') as f: self.contents = f.read()
            return self.contents


def are_docs_same(original_dir: str, new_dir: str) -> bool:
    """Checks if the contents of two files are exactly identical. Returns boolean."""
    # Get contents
    original = Document(directory = original_dir)
    new = Document(directory = new_dir)

    # Check contents
    if original.contents == new.contents:
        print("Contents match.")
        return True
    else:
        print("Contents do not match.")
        return False


def append_by_query(
    query: str, 
    content: str, 
    file: str | Document, 
    insert_above: bool = False
) -> None:
    """
    Required args: query, content, and file path. 
    Optional args: insert_above

    Searches through the contents of the target file and inserts content a line below \
        the first occurence. 
    """
    # Get contents
    if isinstance(file, str):
        with open(file, 'r') as f: data = f.readlines()
        file_path = file
    elif isinstance(file, Document):
        data = file.contents()
        file_path = file.path

    # Check for the <title>
    for pos, line in enumerate(data):
        if query in line:
            break
    else: # Quit the program if <title> wasn't found
        raise Exception(f"{query} not found in any lines of {file_path}.") 

    # Insert after? Increase line number by 1.
    if not insert_above:
        pos += 1

    # Append the string
    data.insert(pos, (content + '\n'))
    with open(file_path, 'w') as f: f.writelines(data)
