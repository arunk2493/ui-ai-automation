from voice_input import capture_voice_command
from ai_test_generator import generate_test_cases
from test_executor import run_tests
from test_logger import convert_csv_to_html

def main():
    scenario = capture_voice_command 
    if scenario:
        generate_test_cases(scenario)
        run_tests()
        convert_csv_to_html()

if __name__ == "__main__":
    main()