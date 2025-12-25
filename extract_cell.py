import json
import sys

notebook_path = r'g:\中正大學\Data-Mining\Lab 2\DM2025-Lab2-Exercise\DM2025-Lab2-Master-Phase_2_Bonus.ipynb'

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    cells = nb.get('cells', [])
    print(f"Total cells: {len(cells)}")
    
    # Python indices are 0-based. User said cell 12. It might be the 13th cell (index 12) or the cell with execution_count 12.
    # I'll print a few around that index.
    
    for i, cell in enumerate(cells):
        if cell.get('cell_type') == 'code':
            # Check execution count if available
            exec_count = cell.get('execution_count')
            source = "".join(cell.get('source', []))
            
            # Print if it's the 12th cell (index 11) or 13th (index 12) or execution count 12
            # Let's just print indices 10 to 14 and check execution counts
            if 10 <= i <= 15:
                print(f"--- Cell Index {i} (Execution Count: {exec_count}) ---")
                print(source)
                print("-" * 20)

except Exception as e:
    print(f"Error: {e}")
