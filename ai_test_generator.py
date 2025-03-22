import openai
import csv

def generate_test_cases(scenario):
    prompt = f"""
    Generate UI automation test cases for the scenario: "{scenario}"
    Include:
    - Positive cases
    - Negative cases
    - Edge cases
    - Expected assertions for validation
    Format:
    Test Case, Steps, Expected Outcome, Assertions
    """

    response = openai.ChatCompletion.create(
        model="gemini-ai",
        messages=[{"role": "user", "content": prompt}]
    )

    test_cases = response["choices"][0]["message"]["content"].split("\n")
    
    with open("test_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Test Case", "Steps", "Expected Outcome", "Assertions"])
        for case in test_cases:
            writer.writerow(case.split(","))

    return test_cases
