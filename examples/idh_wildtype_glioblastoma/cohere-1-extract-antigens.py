import cohere
import os
import sys

def read_file(file_path):
    """Read the contents of a file."""
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # Get the file name from the first command-line argument
    if len(sys.argv) < 2:
        print("Please provide the filename as a command-line argument.")
        sys.exit(1)
    
    file_name = sys.argv[1]
    
    # Read the content of the file
    file_content = read_file(file_name)

    content = file_content + "\n\nFrom this AI generated summary of antigens from a number of Pubmed Central Papers, please extract all unique antigen names and make a list of these with one entry per line."

    COHERE_API_KEY = os.getenv('COHERE_API_KEY')
    co = cohere.ClientV2(COHERE_API_KEY)

    response = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {
                "role": "user",
                "content": content
            }
        ]
    )

    print(response.message.content[0].text)

if __name__ == "__main__":
    main()
