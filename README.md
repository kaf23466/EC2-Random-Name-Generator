
# EC2 Unique Name Generator

A simple Python script to generate unique names for Amazon EC2 instances based on the department name and random characters/numbers.

## Features
- Generate unique names based on user-inputted department name.
- Provide the desired number of EC2 instance names.
- Each generated name consists of the department name followed by a hyphen and then five random lowercase letters and/or numbers.

## Usage

1. Clone the repository or download the Python script.
2. Run the script using the command:
   ```
   python ec2_name_generator.py
   ```
3. When prompted, enter the number of EC2 names you need.
4. Enter the department name.
5. The script will then print unique names for each instance.

## Example

Input:
```
Number of EC2 names needed? 2
Department name: finance
```

Output:
```
finance-j4k3l
finance-q2p5z
```

---

Save the above content in a file named `README.md`. This will provide a good introduction and usage guide for anyone looking at the repository. If you're using GitHub, the content of this file will be displayed on the main page of the repository, formatted using Markdown.
