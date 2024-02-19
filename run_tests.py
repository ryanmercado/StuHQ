import pytest
import sys

path_to_stuhq = sys.path[0]
back_end_module = path_to_stuhq + '/backend'
recipe_module = back_end_module + '/recipe'
sys.path.append(back_end_module)

sys.path.append(recipe_module)

pytest.main()

# to run specific file: 
# pytest.main(['backend/tests/test_registration_login.py'])

