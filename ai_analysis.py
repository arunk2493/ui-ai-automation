import google.generativeai as genai # type: ignore

def analyze_failure(test_case, error):
    prompt = f"""
    The following UI test case failed:
    Test Case: {test_case}
    Error: {error}

    Perform root cause analysis and suggest fixes.
    """
    
    response = genai.ChatCompletion.create(
        model="gemini-ai",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]
