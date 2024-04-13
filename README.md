## README

### JSON Verification Script

This script is designed to verify JSON files following a specific format, particularly the AWS IAM Role Policy format.
It checks if the input JSON *Resource* field contains a single asterisk; if it does, it returns false; otherwise,
it returns true.

### Usage

To use this script, follow these steps:

1. **Install Python:** Ensure you have Python installed on your system. This script is compatible with Python 3.x.

2. **Clone the Repository:** Clone or download this repository to your local machine.

3. **Navigate to the Directory:** Open a terminal or command prompt and navigate to the directory containing the script.

4. **Run the Script:** Execute the script by running the following command:

   ### Windows
    ```
    python aws_format_verifier.py <path_to_json_file>
    ```
   
   ### Linux
   ```
    python3 aws_format_verifier.py <path_to_json_file>
    ```

    Replace `<path_to_json_file>` with the path to the JSON file you want to verify. Remember to provide the absolute 
   file path

### Functionality

The script performs the following checks:

- **File Existence:** Verifies if the specified JSON file exists.
- **JSON Syntax:** Checks if the JSON file is correctly formatted.
- **Resource Field Check:** Detects if the "Resource" field contains a single asterisk (*).

### Errors and Exceptions

If any errors occur during the verification process, the script provides relevant error messages to assist in 
troubleshooting. If the program encounters an error, it will still return true because it is not a single asterisk 
in the *Resource* field.

### Example

Here's an example of how to use the script:

```bash
python aws_format_verifier.py example.json
```

Replace `example.json` with the path to your JSON file.

### Test cases

To run defined test cases, navigate to the directory and then execute the script `unit_tests.py` by running the 
following command:

 #### Windows
    python unit_tests.py <path_to_json_file>
   
#### Linux

    python3 unit_test.py <path_to_json_file>

