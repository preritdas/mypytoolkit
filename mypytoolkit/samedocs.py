class Document:
    """Document object with directory and contents attributes."""
    def __init__(self, directory: str):
        self.directory = directory
        
        ## Checks
        if ".txt" not in self.directory:
            raise Exception("You must compare two text files.")

        ## Contents
        with open(self.directory, 'r') as f:
            self.contents = f.read()

def are_docs_same(original_dir: str, new_dir: str):
    """Checks if the contents of two files are exactly identical. Returns boolean."""
    # Get contents
    Original = Document(directory = original_dir)
    New = Document(directory = new_dir)

    # Check contents
    if Original.contents == New.contents:
        print("Contents match.")
        return True
    else:
        print("Contents do not match.")
        return False