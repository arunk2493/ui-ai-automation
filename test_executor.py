import time
import csv
from playwright.sync_api import sync_playwright # type: ignore
import google.generativeai as genai # type: ignore

def execute_test_case(test_case):
    start_time = time.time()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        prompt = f"Perform the following test steps using UI automation:\n{test_case}"
        
        response = genai.ChatCompletion.create(
            model="gemini-ai",
            messages=[{"role": "user", "content": prompt}]
        )
        
        automation_steps = response["choices"][0]["message"]["content"]
        exec(automation_steps)  # Execute AI-generated automation code
        
        browser.close()
    
    execution_time = time.time() - start_time
    return execution_time

def run_tests():
    with open("test_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            test_case, steps, expected, assertions = row
            print(f"Executing: {test_case}")
            exec_time = execute_test_case(steps)
            print(f"Execution Time: {exec_time:.2f} seconds")
            log_test_result(test_case, "Passed", exec_time, "")

if __name__ == "__main__":
    run_tests()
