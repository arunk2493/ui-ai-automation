import google.generativeai as genai # type: ignore
import json

genai.api_key = "YOUR_GEMINI_API_KEY"

def generate_test_cases(command):
    """Generates structured Playwright test cases covering positive, negative, and edge cases."""

    prompt = f"""
    Given the test scenario: "{command}", generate structured Playwright test cases covering:
    - **Positive Cases:** Successful execution of the test scenario.
    - **Negative Cases:** Invalid inputs, missing fields, incorrect credentials, etc.
    - **Edge Cases:** Boundary values, extreme inputs, performance limits.

    **Test Case Format:**
    - Test Case ID: Unique identifier.
    - Description: Detailed explanation of the test.
    - Steps: Ordered list of actions for Playwright automation.
    - Expected Outcome: Expected behavior after execution.
    - Category: Positive, Negative, or Edge case.
    - Automation Script: Playwright test steps in Python.

    **Output JSON Format:**
    {{
        "test_cases": [
            {{
                "id": "TC001",
                "description": "Successful login with valid credentials",
                "steps": ["Navigate to login page", "Enter valid username", "Enter valid password", "Click login button"],
                "expected_outcome": "User is logged in and redirected to dashboard",
                "category": "Positive",
                "automation_script": "page.goto('https://example.com'); page.fill('#username', 'valid_user'); page.fill('#password', 'valid_pass'); page.click('button:has-text('Login')');"
            }},
            ...
        ]
    }}

    Generate at least **5-7 test cases** for the given scenario.
    """

    response = genai.ChatCompletion.create(
        model="gemini-pro",
        messages=[{"role": "system", "content": prompt}]
    )

    return json.loads(response["choices"][0]["message"]["content"])
