import pytest
import pytest
import assert_utilities
import numpy as np
from all_questions import *
import yaml
import test_utils as u
from my_fixtures import *
from pytest_utils.decorators import max_score, visibility, partial_score, hide_errors

with open('type_handlers.yaml', 'r') as f:
    type_handlers = yaml.safe_load(f)

@hide_errors('')
def test_structure_question1_a_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question1_a_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question1_a_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_a_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question1_a_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(a) explain' not in correct_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question1_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) explain']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(a) explain' not in student_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question1_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_a_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question1_b_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question1_b_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question1_b_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_b_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question1_b_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(b) explain' not in correct_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question1_b_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) explain']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(b) explain' not in student_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question1_b_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_b_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question1_c_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question1_c_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question1_c_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_c_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question1_c_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(c) explain' not in correct_answer:
        explanation = "Key: '(c) explain' not found.\n"
        test_structure_question1_c_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) explain']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(c) explain' not in student_answer:
        explanation = "Key: '(c) explain' not found.\n"
        test_structure_question1_c_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_c_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question1_d_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(d)' not in correct_answer:
        explanation = "Key: '(d)' not found.\n"
        test_structure_question1_d_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d)']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(d)' not in student_answer:
        explanation = "Key: '(d)' not found.\n"
        test_structure_question1_d_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_d_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question1_d_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question1', 'i', **kwargs)
    if '(d) explain' not in correct_answer:
        explanation = "Key: '(d) explain' not found.\n"
        test_structure_question1_d_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) explain']
    student_answer = run_compute('all_questions', 'question1', 's', **kwargs)
    if '(d) explain' not in student_answer:
        explanation = "Key: '(d) explain' not found.\n"
        test_structure_question1_d_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question1_d_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_a_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question2_a_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question2_a_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_a_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_a_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(a) explain' not in correct_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question2_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) explain']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(a) explain' not in student_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question2_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_a_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_b_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question2_b_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question2_b_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_b_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_b_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(b) explain' not in correct_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question2_b_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) explain']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(b) explain' not in student_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question2_b_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_b_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_c_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question2_c_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question2_c_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_c_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_c_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(c) explain' not in correct_answer:
        explanation = "Key: '(c) explain' not found.\n"
        test_structure_question2_c_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) explain']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(c) explain' not in student_answer:
        explanation = "Key: '(c) explain' not found.\n"
        test_structure_question2_c_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_c_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_d_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(d)' not in correct_answer:
        explanation = "Key: '(d)' not found.\n"
        test_structure_question2_d_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d)']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(d)' not in student_answer:
        explanation = "Key: '(d)' not found.\n"
        test_structure_question2_d_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_d_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question2_d_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question2', 'i', **kwargs)
    if '(d) explain' not in correct_answer:
        explanation = "Key: '(d) explain' not found.\n"
        test_structure_question2_d_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) explain']
    student_answer = run_compute('all_questions', 'question2', 's', **kwargs)
    if '(d) explain' not in student_answer:
        explanation = "Key: '(d) explain' not found.\n"
        test_structure_question2_d_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question2_d_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question3_a_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question3_a_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question3_a_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question3_a_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question3_a_example_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if '(a) example' not in correct_answer:
        explanation = "Key: '(a) example' not found.\n"
        test_structure_question3_a_example_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) example']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if '(a) example' not in student_answer:
        explanation = "Key: '(a) example' not found.\n"
        test_structure_question3_a_example_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) example']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question3_a_example_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question3_b_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question3_b_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question3_b_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question3_b_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question3_b_example_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if '(b) example' not in correct_answer:
        explanation = "Key: '(b) example' not found.\n"
        test_structure_question3_b_example_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) example']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if '(b) example' not in student_answer:
        explanation = "Key: '(b) example' not found.\n"
        test_structure_question3_b_example_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) example']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question3_b_example_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question3_c_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question3_c_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question3_c_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question3_c_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question3_c_example_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question3', 'i', **kwargs)
    if '(c) example' not in correct_answer:
        explanation = "Key: '(c) example' not found.\n"
        test_structure_question3_c_example_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) example']
    student_answer = run_compute('all_questions', 'question3', 's', **kwargs)
    if '(c) example' not in student_answer:
        explanation = "Key: '(c) example' not found.\n"
        test_structure_question3_c_example_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) example']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question3_c_example_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_a_bool_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(a)' not in correct_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question7_a_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a)']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(a)' not in student_answer:
        explanation = "Key: '(a)' not found.\n"
        test_structure_question7_a_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_a_bool_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_a_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(a) explain' not in correct_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question7_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(a) explain' not in student_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question7_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_a_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_b_bool_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(b)' not in correct_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question7_b_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b)']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(b)' not in student_answer:
        explanation = "Key: '(b)' not found.\n"
        test_structure_question7_b_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_b_bool_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_b_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(b) explain' not in correct_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question7_b_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(b) explain' not in student_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question7_b_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_b_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_c_bool_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(c)' not in correct_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question7_c_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c)']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(c)' not in student_answer:
        explanation = "Key: '(c)' not found.\n"
        test_structure_question7_c_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_c_bool_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_c_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(c) explain' not in correct_answer:
        explanation = "Key: '(c) explain' not found.\n"
        test_structure_question7_c_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(c) explain' not in student_answer:
        explanation = "Key: '(c) explain' not found.\n"
        test_structure_question7_c_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_c_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_d_bool_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(d)' not in correct_answer:
        explanation = "Key: '(d)' not found.\n"
        test_structure_question7_d_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d)']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(d)' not in student_answer:
        explanation = "Key: '(d)' not found.\n"
        test_structure_question7_d_bool_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_answer_bool(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_d_bool_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question7_d_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question7', 'i', **kwargs)
    if '(d) explain' not in correct_answer:
        explanation = "Key: '(d) explain' not found.\n"
        test_structure_question7_d_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) explain']
    student_answer = run_compute('all_questions', 'question7', 's', **kwargs)
    if '(d) explain' not in student_answer:
        explanation = "Key: '(d) explain' not found.\n"
        test_structure_question7_d_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question7_d_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_a_PX_1_1_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) P(X_1 = 1 | +)' not in correct_answer:
        explanation = "Key: '(a) P(X_1 = 1 | +)' not found.\n"
        test_structure_question8_a_PX_1_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(X_1 = 1 | +)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) P(X_1 = 1 | +)' not in student_answer:
        explanation = "Key: '(a) P(X_1 = 1 | +)' not found.\n"
        test_structure_question8_a_PX_1_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(X_1 = 1 | +)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_a_PX_1_1_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_a_PX_1_1_minus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) P(X_1 = 1 | -)' not in correct_answer:
        explanation = "Key: '(a) P(X_1 = 1 | -)' not found.\n"
        test_structure_question8_a_PX_1_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(X_1 = 1 | -)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) P(X_1 = 1 | -)' not in student_answer:
        explanation = "Key: '(a) P(X_1 = 1 | -)' not found.\n"
        test_structure_question8_a_PX_1_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(X_1 = 1 | -)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_a_PX_1_1_minus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_a_PX_2_1_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) P(X_2 = 1 | +)' not in correct_answer:
        explanation = "Key: '(a) P(X_2 = 1 | +)' not found.\n"
        test_structure_question8_a_PX_2_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(X_2 = 1 | +)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) P(X_2 = 1 | +)' not in student_answer:
        explanation = "Key: '(a) P(X_2 = 1 | +)' not found.\n"
        test_structure_question8_a_PX_2_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(X_2 = 1 | +)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_a_PX_2_1_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_a_PX_2_1_minus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) P(X_2 = 1 | -)' not in correct_answer:
        explanation = "Key: '(a) P(X_2 = 1 | -)' not found.\n"
        test_structure_question8_a_PX_2_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(X_2 = 1 | -)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) P(X_2 = 1 | -)' not in student_answer:
        explanation = "Key: '(a) P(X_2 = 1 | -)' not found.\n"
        test_structure_question8_a_PX_2_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(X_2 = 1 | -)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_a_PX_2_1_minus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_a_PX_3_1_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) P(X_3 = 1 | +)' not in correct_answer:
        explanation = "Key: '(a) P(X_3 = 1 | +)' not found.\n"
        test_structure_question8_a_PX_3_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(X_3 = 1 | +)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) P(X_3 = 1 | +)' not in student_answer:
        explanation = "Key: '(a) P(X_3 = 1 | +)' not found.\n"
        test_structure_question8_a_PX_3_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(X_3 = 1 | +)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_a_PX_3_1_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_a_PX_3_1_minus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(a) P(X_3 = 1 | -)' not in correct_answer:
        explanation = "Key: '(a) P(X_3 = 1 | -)' not found.\n"
        test_structure_question8_a_PX_3_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(X_3 = 1 | -)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(a) P(X_3 = 1 | -)' not in student_answer:
        explanation = "Key: '(a) P(X_3 = 1 | -)' not found.\n"
        test_structure_question8_a_PX_3_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(X_3 = 1 | -)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_a_PX_3_1_minus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_b_label_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(b) label' not in correct_answer:
        explanation = "Key: '(b) label' not found.\n"
        test_structure_question8_b_label_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) label']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(b) label' not in student_answer:
        explanation = "Key: '(b) label' not found.\n"
        test_structure_question8_b_label_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) label']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_b_label_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_c_PX_1_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(c) P(X_1=1)' not in correct_answer:
        explanation = "Key: '(c) P(X_1=1)' not found.\n"
        test_structure_question8_c_PX_1_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) P(X_1=1)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(c) P(X_1=1)' not in student_answer:
        explanation = "Key: '(c) P(X_1=1)' not found.\n"
        test_structure_question8_c_PX_1_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) P(X_1=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_c_PX_1_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_c_PX_2_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(c) P(X_2=1)' not in correct_answer:
        explanation = "Key: '(c) P(X_2=1)' not found.\n"
        test_structure_question8_c_PX_2_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) P(X_2=1)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(c) P(X_2=1)' not in student_answer:
        explanation = "Key: '(c) P(X_2=1)' not found.\n"
        test_structure_question8_c_PX_2_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) P(X_2=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_c_PX_2_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_c_PX_1_1_comma_X_2_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(c) P(X_1=1,X_2=1)' not in correct_answer:
        explanation = "Key: '(c) P(X_1=1,X_2=1)' not found.\n"
        test_structure_question8_c_PX_1_1_comma_X_2_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) P(X_1=1,X_2=1)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(c) P(X_1=1,X_2=1)' not in student_answer:
        explanation = "Key: '(c) P(X_1=1,X_2=1)' not found.\n"
        test_structure_question8_c_PX_1_1_comma_X_2_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) P(X_1=1,X_2=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_c_PX_1_1_comma_X_2_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_c_Relationship_between_X_1_and_X_2_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(c) Relationship between X_1 and X_2' not in correct_answer:
        explanation = "Key: '(c) Relationship between X_1 and X_2' not found.\n"
        test_structure_question8_c_Relationship_between_X_1_and_X_2_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) Relationship between X_1 and X_2']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(c) Relationship between X_1 and X_2' not in student_answer:
        explanation = "Key: '(c) Relationship between X_1 and X_2' not found.\n"
        test_structure_question8_c_Relationship_between_X_1_and_X_2_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) Relationship between X_1 and X_2']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_c_Relationship_between_X_1_and_X_2_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_d_PA_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(d) P(A=1)' not in correct_answer:
        explanation = "Key: '(d) P(A=1)' not found.\n"
        test_structure_question8_d_PA_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) P(A=1)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(d) P(A=1)' not in student_answer:
        explanation = "Key: '(d) P(A=1)' not found.\n"
        test_structure_question8_d_PA_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) P(A=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_d_PA_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_e_PX_1_1_comma_X_2_1_Class_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(e) P(X_1=1, X_2=1|Class=+)' not in correct_answer:
        explanation = "Key: '(e) P(X_1=1, X_2=1|Class=+)' not found.\n"
        test_structure_question8_e_PX_1_1_comma_X_2_1_Class_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(e) P(X_1=1, X_2=1|Class=+)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(e) P(X_1=1, X_2=1|Class=+)' not in student_answer:
        explanation = "Key: '(e) P(X_1=1, X_2=1|Class=+)' not found.\n"
        test_structure_question8_e_PX_1_1_comma_X_2_1_Class_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(e) P(X_1=1, X_2=1|Class=+)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_e_PX_1_1_comma_X_2_1_Class_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_e_PX_1_1_Class_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(e) P(X_1=1|Class=+)' not in correct_answer:
        explanation = "Key: '(e) P(X_1=1|Class=+)' not found.\n"
        test_structure_question8_e_PX_1_1_Class_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(e) P(X_1=1|Class=+)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(e) P(X_1=1|Class=+)' not in student_answer:
        explanation = "Key: '(e) P(X_1=1|Class=+)' not found.\n"
        test_structure_question8_e_PX_1_1_Class_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(e) P(X_1=1|Class=+)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_e_PX_1_1_Class_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_e_PX_2_1_Class_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(e) P(X_2=1|Class=+)' not in correct_answer:
        explanation = "Key: '(e) P(X_2=1|Class=+)' not found.\n"
        test_structure_question8_e_PX_2_1_Class_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(e) P(X_2=1|Class=+)']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(e) P(X_2=1|Class=+)' not in student_answer:
        explanation = "Key: '(e) P(X_2=1|Class=+)' not found.\n"
        test_structure_question8_e_PX_2_1_Class_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(e) P(X_2=1|Class=+)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_e_PX_2_1_Class_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_e_A_and_B_conditionally_independent_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(e) A and B conditionally independent' not in correct_answer:
        explanation = "Key: '(e) A and B conditionally independent' not found.\n"
        test_structure_question8_e_A_and_B_conditionally_independent_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(e) A and B conditionally independent']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(e) A and B conditionally independent' not in student_answer:
        explanation = "Key: '(e) A and B conditionally independent' not found.\n"
        test_structure_question8_e_A_and_B_conditionally_independent_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(e) A and B conditionally independent']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_e_A_and_B_conditionally_independent_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question8_d_Training_error_rate_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question8', 'i', **kwargs)
    if '(d) Training error rate' not in correct_answer:
        explanation = "Key: '(d) Training error rate' not found.\n"
        test_structure_question8_d_Training_error_rate_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) Training error rate']
    student_answer = run_compute('all_questions', 'question8', 's', **kwargs)
    if '(d) Training error rate' not in student_answer:
        explanation = "Key: '(d) Training error rate' not found.\n"
        test_structure_question8_d_Training_error_rate_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) Training error rate']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question8_d_Training_error_rate_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question9_a_K_int_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(a) K' not in correct_answer:
        explanation = "Key: '(a) K' not found.\n"
        test_structure_question9_a_K_int_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) K']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(a) K' not in student_answer:
        explanation = "Key: '(a) K' not found.\n"
        test_structure_question9_a_K_int_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) K']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_int(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question9_a_K_int_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question9_a_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(a) explain' not in correct_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question9_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) explain']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(a) explain' not in student_answer:
        explanation = "Key: '(a) explain' not found.\n"
        test_structure_question9_a_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question9_a_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question9_b_K_int_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(b) K' not in correct_answer:
        explanation = "Key: '(b) K' not found.\n"
        test_structure_question9_b_K_int_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) K']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(b) K' not in student_answer:
        explanation = "Key: '(b) K' not found.\n"
        test_structure_question9_b_K_int_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) K']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_int(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question9_b_K_int_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question9_b_explain_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question9', 'i', **kwargs)
    if '(b) explain' not in correct_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question9_b_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) explain']
    student_answer = run_compute('all_questions', 'question9', 's', **kwargs)
    if '(b) explain' not in student_answer:
        explanation = "Key: '(b) explain' not found.\n"
        test_structure_question9_b_explain_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) explain']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question9_b_explain_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_a_PA_1_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) P(A=1|+)' not in correct_answer:
        explanation = "Key: '(a) P(A=1|+)' not found.\n"
        test_structure_question10_a_PA_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(A=1|+)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) P(A=1|+)' not in student_answer:
        explanation = "Key: '(a) P(A=1|+)' not found.\n"
        test_structure_question10_a_PA_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(A=1|+)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_a_PA_1_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_a_PB_1_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) P(B=1|+)' not in correct_answer:
        explanation = "Key: '(a) P(B=1|+)' not found.\n"
        test_structure_question10_a_PB_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(B=1|+)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) P(B=1|+)' not in student_answer:
        explanation = "Key: '(a) P(B=1|+)' not found.\n"
        test_structure_question10_a_PB_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(B=1|+)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_a_PB_1_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_a_PC_1_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) P(C=1|+)' not in correct_answer:
        explanation = "Key: '(a) P(C=1|+)' not found.\n"
        test_structure_question10_a_PC_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(C=1|+)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) P(C=1|+)' not in student_answer:
        explanation = "Key: '(a) P(C=1|+)' not found.\n"
        test_structure_question10_a_PC_1_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(C=1|+)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_a_PC_1_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_a_PA_1_minus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) P(A=1|-)' not in correct_answer:
        explanation = "Key: '(a) P(A=1|-)' not found.\n"
        test_structure_question10_a_PA_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(A=1|-)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) P(A=1|-)' not in student_answer:
        explanation = "Key: '(a) P(A=1|-)' not found.\n"
        test_structure_question10_a_PA_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(A=1|-)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_a_PA_1_minus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_a_PB_1_minus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) P(B=1|-)' not in correct_answer:
        explanation = "Key: '(a) P(B=1|-)' not found.\n"
        test_structure_question10_a_PB_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(B=1|-)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) P(B=1|-)' not in student_answer:
        explanation = "Key: '(a) P(B=1|-)' not found.\n"
        test_structure_question10_a_PB_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(B=1|-)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_a_PB_1_minus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_a_PC_1_minus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) P(C=1|-)' not in correct_answer:
        explanation = "Key: '(a) P(C=1|-)' not found.\n"
        test_structure_question10_a_PC_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(C=1|-)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) P(C=1|-)' not in student_answer:
        explanation = "Key: '(a) P(C=1|-)' not found.\n"
        test_structure_question10_a_PC_1_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(C=1|-)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_a_PC_1_minus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_a_PA_1_plus_explain_your_answer_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(a) P(A=1|+) explain your answer' not in correct_answer:
        explanation = "Key: '(a) P(A=1|+) explain your answer' not found.\n"
        test_structure_question10_a_PA_1_plus_explain_your_answer_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(a) P(A=1|+) explain your answer']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(a) P(A=1|+) explain your answer' not in student_answer:
        explanation = "Key: '(a) P(A=1|+) explain your answer' not found.\n"
        test_structure_question10_a_PA_1_plus_explain_your_answer_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(a) P(A=1|+) explain your answer']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_a_PA_1_plus_explain_your_answer_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_b_P_plus_R_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(b) P(+|R)' not in correct_answer:
        explanation = "Key: '(b) P(+|R)' not found.\n"
        test_structure_question10_b_P_plus_R_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) P(+|R)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(b) P(+|R)' not in student_answer:
        explanation = "Key: '(b) P(+|R)' not found.\n"
        test_structure_question10_b_P_plus_R_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) P(+|R)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_b_P_plus_R_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_b_PR_plus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(b) P(R|+)' not in correct_answer:
        explanation = "Key: '(b) P(R|+)' not found.\n"
        test_structure_question10_b_PR_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) P(R|+)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(b) P(R|+)' not in student_answer:
        explanation = "Key: '(b) P(R|+)' not found.\n"
        test_structure_question10_b_PR_plus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) P(R|+)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_b_PR_plus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_b_PR_minus_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(b) P(R|-)' not in correct_answer:
        explanation = "Key: '(b) P(R|-)' not found.\n"
        test_structure_question10_b_PR_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) P(R|-)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(b) P(R|-)' not in student_answer:
        explanation = "Key: '(b) P(R|-)' not found.\n"
        test_structure_question10_b_PR_minus_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) P(R|-)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_b_PR_minus_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_b_class_label_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(b) class label' not in correct_answer:
        explanation = "Key: '(b) class label' not found.\n"
        test_structure_question10_b_class_label_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) class label']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(b) class label' not in student_answer:
        explanation = "Key: '(b) class label' not found.\n"
        test_structure_question10_b_class_label_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) class label']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_b_class_label_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_b_Explain_your_reasoning_explain_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(b) Explain your reasoning' not in correct_answer:
        explanation = "Key: '(b) Explain your reasoning' not found.\n"
        test_structure_question10_b_Explain_your_reasoning_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(b) Explain your reasoning']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(b) Explain your reasoning' not in student_answer:
        explanation = "Key: '(b) Explain your reasoning' not found.\n"
        test_structure_question10_b_Explain_your_reasoning_explain_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(b) Explain your reasoning']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_explain_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_b_Explain_your_reasoning_explain_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_c_PA_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) P(A=1)' not in correct_answer:
        explanation = "Key: '(c) P(A=1)' not found.\n"
        test_structure_question10_c_PA_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) P(A=1)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) P(A=1)' not in student_answer:
        explanation = "Key: '(c) P(A=1)' not found.\n"
        test_structure_question10_c_PA_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) P(A=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_c_PA_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_c_PB_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) P(B=1)' not in correct_answer:
        explanation = "Key: '(c) P(B=1)' not found.\n"
        test_structure_question10_c_PB_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) P(B=1)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) P(B=1)' not in student_answer:
        explanation = "Key: '(c) P(B=1)' not found.\n"
        test_structure_question10_c_PB_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) P(B=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_c_PB_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_c_PA_1_comma_B_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) P(A=1,B=1)' not in correct_answer:
        explanation = "Key: '(c) P(A=1,B=1)' not found.\n"
        test_structure_question10_c_PA_1_comma_B_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) P(A=1,B=1)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) P(A=1,B=1)' not in student_answer:
        explanation = "Key: '(c) P(A=1,B=1)' not found.\n"
        test_structure_question10_c_PA_1_comma_B_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) P(A=1,B=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_c_PA_1_comma_B_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_c_A_independent_of_B_ques_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(c) A independent of B?' not in correct_answer:
        explanation = "Key: '(c) A independent of B?' not found.\n"
        test_structure_question10_c_A_independent_of_B_ques_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(c) A independent of B?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(c) A independent of B?' not in student_answer:
        explanation = "Key: '(c) A independent of B?' not found.\n"
        test_structure_question10_c_A_independent_of_B_ques_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(c) A independent of B?']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_c_A_independent_of_B_ques_string_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_d_PA_1_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(d) P(A=1)' not in correct_answer:
        explanation = "Key: '(d) P(A=1)' not found.\n"
        test_structure_question10_d_PA_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) P(A=1)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(d) P(A=1)' not in student_answer:
        explanation = "Key: '(d) P(A=1)' not found.\n"
        test_structure_question10_d_PA_1_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) P(A=1)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_d_PA_1_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_d_PB_0_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(d) P(B=0)' not in correct_answer:
        explanation = "Key: '(d) P(B=0)' not found.\n"
        test_structure_question10_d_PB_0_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) P(B=0)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(d) P(B=0)' not in student_answer:
        explanation = "Key: '(d) P(B=0)' not found.\n"
        test_structure_question10_d_PB_0_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) P(B=0)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_d_PB_0_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_d_PA_1_comma_B_0_float_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(d) P(A=1,B=0)' not in correct_answer:
        explanation = "Key: '(d) P(A=1,B=0)' not found.\n"
        test_structure_question10_d_PA_1_comma_B_0_float_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) P(A=1,B=0)']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(d) P(A=1,B=0)' not in student_answer:
        explanation = "Key: '(d) P(A=1,B=0)' not found.\n"
        test_structure_question10_d_PA_1_comma_B_0_float_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) P(A=1,B=0)']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_float(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_d_PA_1_comma_B_0_float_lparen_rparen.explanation = explanation
    assert is_success

@hide_errors('')
def test_structure_question10_d_A_independent_of_B_ques_string_lparen_rparen(run_compute):
    kwargs = {'student_directory': 'student_code_with_answers' , 'instructor_directory': 'instructor_code_with_answers'}
    correct_answer = run_compute('all_questions', 'question10', 'i', **kwargs)
    if '(d) A independent of B?' not in correct_answer:
        explanation = "Key: '(d) A independent of B?' not found.\n"
        test_structure_question10_d_A_independent_of_B_ques_string_lparen_rparen.explanation = explanation
        assert False
    else:
        correct_answer = correct_answer['(d) A independent of B?']
    student_answer = run_compute('all_questions', 'question10', 's', **kwargs)
    if '(d) A independent of B?' not in student_answer:
        explanation = "Key: '(d) A independent of B?' not found.\n"
        test_structure_question10_d_A_independent_of_B_ques_string_lparen_rparen.explanation = explanation
        assert False
    else:
        student_answer = student_answer['(d) A independent of B?']
    print(f'is_fixture=True, is_student_file=True, is_instructor_file=True')
    answer = student_answer
    tol = 0.001
    keys = None
    msg = "assert_utilities.check_structure_string(student_answer, instructor_answer)"
    local_namespace={'array': np.array, 'assert_utilities': assert_utilities, 'student_answer': student_answer, 'instructor_answer': correct_answer, 'rel_tol':tol, 'keys':keys}
    is_success, explanation = eval(msg, {'__builtins__':{}}, local_namespace)
    test_structure_question10_d_A_independent_of_B_ques_string_lparen_rparen.explanation = explanation
    assert is_success
