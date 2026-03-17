import re

def upgrade_latex_delimiters(content):
    # Regex breakdown:
    # (?<!\$) - Negative lookbehind: Ensure there isn't a $ before this
    # \$       - Match a literal dollar sign
    # ([^\$]+) - Capture group: Match one or more characters that are NOT a $
    # \$       - Match a literal closing dollar sign
    # (?!\$)  - Negative lookahead: Ensure there isn't a $ after this
    pattern = r'(?<!\$)\$([^\$]+)\$(?!\$)'
    
    # Replace the single $ match with double $$
    upgraded_content = re.sub(pattern, r'$$\1$$', content)
    
    return upgraded_content

# --- Example Usage with your provided file content ---
file_path = '2026-03-17-k-means-clustering.md'
output_path = '2026-03-17-k-means-clustering-upgraded.md'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        original_text = f.read()

    new_text = upgrade_latex_delimiters(original_text)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_text)
        
    print(f"Success! Upgraded file saved as: {output_path}")

except FileNotFoundError:
    print("File not found. Please check the file path.")