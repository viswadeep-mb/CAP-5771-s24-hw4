#!/bin/bash

# Runs on Gradescope server
# CODE: student code

# student_code_with_answers is on my local system
export PYTHONPATH=student_code_with_answers:/autograder/MAKE-STUDENT-OUTPUT/CODE:.:pytest_utils:instructor_code_with_answers

due_date="2024-02-20"

# Current date in YYYY-MM-DD format
current_date=$(date '+%Y-%m-%d')
echo "current_date" : $current_date
echo "due_date" : $due_date

if [[ "$current_date" < "$due_date" ]]; then
    echo "Current date is earlier than the due date."

#pytest -s tests/test_structure.py 
pytest -s tests/test_structure.py tests/test_answers.py
#pytest -s tests/test_answers.py

#pytest -s tests/test_structure.py::test_structure_question3_a_SSE_eval_float_lparen_rparen
#pytest -s tests/test_answers.py::test_answers_question7_a_string
#pytest -s tests/test_answers.py::test_answers_question3_a_SSE_eval_float


elif [[ "$current_date" > "$due_date" ]]; then
    echo "Current date is later than the due date."

#pytest -s tests/test_structure.py
#pytest -s tests/test_answers.py
else
    echo "Current date is the due date."
fi

