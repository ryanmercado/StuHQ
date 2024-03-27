import pytest
import sys

path_to_stuhq = sys.path[0]
back_end_module = path_to_stuhq + '/backend'
recipe_module = back_end_module + '/recipe'
resume_module = back_end_module + '/resume'
sys.path.append(back_end_module)

sys.path.append(recipe_module)
sys.path.append(resume_module)

pytest.main()

# to run specific file: 
# pytest.main(['backend/tests/test_resume.py'])

