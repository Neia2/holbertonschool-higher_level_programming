#!/usr/bin/python3
import marshal
import types

def get_defined_names(file_path):
    """Extract and return all names defined in the compiled module."""
    with open(file_path, 'rb') as file:
        # Skip the magic number and timestamp in the .pyc file
        file.read(16)
        # Load the module's code object from the .pyc file
        code = marshal.load(file)
    
    # Create a module from the code object
    module = types.ModuleType('hidden')
    exec(code, module.__dict__)
    
    # Get all names defined in the module
    defined_names = dir(module)
    return [name for name in defined_names if not name.startswith('__')]

def main():
    """Main function to print defined names in alphabetical order."""
    file_path = '/tmp/hidden_4.pyc'
    names = get_defined_names(file_path)
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()
