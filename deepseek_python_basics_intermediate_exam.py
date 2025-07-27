Time: 30 minutes
Difficulty: Beginner → Intermediate

Task 1: List Manipulation
Write a function clean_data(data: list) -> list that:

Removes None values and duplicates from the list.

Converts all strings to lowercase.

Example:

python
input = ["Python", None, "PYTHON", "java", 2, None]
output = ["python", "java", 2]
Task 2: Dictionary Transformation
Given a dictionary scores = {"Alice": 85, "Bob": 90, "Charlie": 78}, write code to:

Invert the keys/values (output: {85: "Alice", 90: "Bob", 78: "Charlie"}).

Handle duplicate values (if any) by appending _1, _2, etc.

Task 3: File Processing
Read a CSV file data.csv (assume it has columns name, age, city):

Load it into a list of dictionaries (e.g., [{"name": "Alice", "age": 25}, ...]).

Filter rows where age > 30.

Task 4: Function with Generators
Create a generator function batch_processing(items: list, batch_size: int) that:

Yields items in batches of batch_size.

Example:

python
for batch in batch_processing([1, 2, 3, 4, 5], 2):
    print(batch)  # [1, 2], [3, 4], [5]
Task 5: Error Handling
Write a function safe_divide(a: int, b: int) -> float:

Returns a / b.

Handles ZeroDivisionError (return 0) and TypeError (return None).