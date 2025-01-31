import os
import re

def find_sql_in_java_project(project_path):
    """
    Finds all SQL queries within a Java project.

    Args:
        project_path: The root path of the Java project.

    Returns:
        A dictionary where keys are file paths and values are lists of SQL queries found in that file.
        Returns an empty dictionary if no files are found or if an error occurs.
    """

    sql_queries = {}

    try:
        for root, _, files in os.walk(project_path):
            for file in files:
                if file.endswith(".java"):  # Look only in Java files
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:  # Handle encoding
                            file_content = f.read()
                            found_queries = extract_sql_from_java(file_content)
                            if found_queries:  # Add only if queries are found
                                sql_queries[file_path] = found_queries
                    except Exception as e:  # Catch file reading errors
                        print(f"Error reading file {file_path}: {e}")
    except Exception as e:
        print(f"Error walking project directory: {e}")
        return {}  # Return empty dictionary in case of error

    return sql_queries


def extract_sql_from_java(java_code):
    """
    Extracts SQL queries from a Java code string.

    Args:
        java_code: The Java code as a string.

    Returns:
        A list of SQL queries found in the code.  Returns an empty list if none are found.
    """

    sql_queries = []

    # Improved regex to capture more SQL variations and handle multiline strings
    # This regex is more robust but might still need adjustments based on your project's coding style.
    sql_regex = r"(?i)\b(?:SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|TRUNCATE|GRANT|REVOKE)\b[\s\S]*?(?<!;)(?=(?:;|\"|\)|\n|$))" # Improved regex

    matches = re.findall(sql_regex, java_code)

    for match in matches:
        cleaned_sql = match.strip()  # Remove leading/trailing whitespace
        if cleaned_sql:  # Add only non-empty queries
            sql_queries.append(cleaned_sql)

    return sql_queries



if __name__ == "__main__":
    project_path = "/path/to/your/java/project"  # Replace with the actual path
    found_sql = find_sql_in_java_project(project_path)

    if found_sql:
        for file_path, queries in found_sql.items():
            print(f"File: {file_path}")
            for i, query in enumerate(queries):
                print(f"  Query {i+1}:\n{query}\n")
    else:
        print("No SQL queries found or an error occurred.")
      
