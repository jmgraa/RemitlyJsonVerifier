import json
import os
import tempfile
import unittest
from aws_format_verifier import verify_json


class TestVerifyJSON(unittest.TestCase):
    def setUp(self):
        self.valid_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "valid data"
                    }
                ]
            }
        }
        self.invalid_data = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "*"
                    }
                ]
            }
        }
        self.multiple_asterisk = {
            "PolicyName": "root",
            "PolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "IamListAccess",
                        "Effect": "Allow",
                        "Action": [
                            "iam:ListRoles",
                            "iam:ListUsers"
                        ],
                        "Resource": "**"
                    }
                ]
            }
        }
        self.invalid_aws_format = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "IamListAccess",
                    "Effect": "Allow",
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ],
                    "Resource": "**"
                }
            ]
        }
        self.invalid_text = "invalid text, not json formatted"

    def test_valid_json(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            json.dump(self.valid_data, temp_file)
            temp_file_path = temp_file.name
        self.assertTrue(verify_json(temp_file_path))
        os.unlink(temp_file_path)

    def test_invalid_json(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            json.dump(self.invalid_data, temp_file)
            temp_file_path = temp_file.name
        self.assertFalse(verify_json(temp_file_path))

        os.unlink(temp_file_path)

    def test_multiple_asterisk(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            json.dump(self.multiple_asterisk, temp_file)
            temp_file_path = temp_file.name
        self.assertTrue(verify_json(temp_file_path))
        os.unlink(temp_file_path)

    def test_nonexistent_file(self):
        self.assertFalse(verify_json("nonexistent.json"))

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file_path = temp_file.name
        self.assertFalse(verify_json(temp_file_path))
        os.unlink(temp_file_path)

    def test_invalid_aws_format(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            json.dump(self.invalid_aws_format, temp_file)
            temp_file_path = temp_file.name
        self.assertFalse(verify_json(temp_file_path))
        os.unlink(temp_file_path)

    def test_invalid_file_content(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(self.invalid_text)
            temp_file.seek(0)
            temp_file_path = temp_file.name
        self.assertFalse(verify_json(temp_file_path))
        os.unlink(temp_file_path)


if __name__ == '__main__':
    unittest.main()
