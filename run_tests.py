import pytest
import sys

path_to_stuhq = sys.path[0]
back_end_module = path_to_stuhq + '/backend'
sys.path.append(back_end_module)
pytest.main()
