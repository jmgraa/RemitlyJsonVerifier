import json
import sys


def verify_json(input_file):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
            for statement in data['PolicyDocument']['Statement']:
                if 'Resource' in statement:
                    if statement['Resource'] == '*':
                        print("Resource field contains a single asterisk (*)")
                        return False

            return True

    except FileNotFoundError:
        print("File not found:", input_file)
        return False
    except json.JSONDecodeError:
        print("Invalid JSON format in the file:", input_file)
        return False
    except KeyError:
        print("File is not formatted correctly in the AWS::IAM::Role Policy format:", input_file)
        return False
    except Exception as e:
        print(f"An error occurred\nType = {type(e).__name__}\nMessage = {e}\n")
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_json_file>\n")
        sys.exit(1)

    print("Verification result:", verify_json(sys.argv[1]))
