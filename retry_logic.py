import time

def retry_test_case(func, test_case, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func(test_case)
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            time.sleep(2)
    print("Max retries reached. Test failed.")
