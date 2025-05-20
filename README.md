# guess_countries

## Troubleshooting

If you encounter an error like:
  from ._pydantic_core import (  
  ImportError: dlopen(... _pydantic_core.so ... symbol not found in flat namespace '_PyList_GetItemRef'

try one of the following:
- Upgrade pydantic-core with: pip install -U pydantic-core
- Verify that your Python version is compatible. Consider using Python 3.10 or 3.11 if using Python 3.13 causes issues.
