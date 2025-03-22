import csv

def log_test_result(test_case, status, execution_time, error=""):
    with open("test_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([test_case, status, f"{execution_time:.2f} seconds", error])

def convert_csv_to_html():
    with open("test_results.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    html_content = """
    <html>
    <head>
        <title>Test Results</title>
        <style>
            table {border-collapse: collapse; width: 100%;}
            th, td {border: 1px solid black; padding: 8px; text-align: left;}
            th {background-color: #f2f2f2;}
        </style>
    </head>
    <body>
        <h2>Test Execution Results</h2>
        <table>
    """

    for row in rows:
        html_content += "<tr>" + "".join(f"<td>{col}</td>" for col in row) + "</tr>"

    html_content += """
        </table>
    </body>
    </html>
    """

    with open("test_results.html", "w") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    convert_csv_to_html()