import sys
import re

# --- LEXICAL ANALYSIS ---
def tokenize(csv_text, delimiter=';'):
    # Remove carriage returns
    csv_text = csv_text.replace('\r', '')

    pattern = re.compile(
        r'(?P<DELIMITER>' + re.escape(delimiter) + r')'
        r'|(?P<NEWLINE>\n)'
        r'|(?P<QUOTE>\")'
        r'|(?P<CHAR>[^' + re.escape(delimiter) + r'\n\"]+)'
    )
    tokens = []
    for match in pattern.finditer(csv_text):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        tokens.append((token_type, token_value))
    return tokens

# --- SYNTACTIC ANALYSIS ---
def parse_tokens(tokens):
    rows = []          # List to hold all rows
    current_row = []   # Current row being built
    current_field = [] # Characters for the current field
    in_quotes = False  # Flag to track a quoted field
    i = 0

    while i < len(tokens):
        token_type, token_value = tokens[i]
        if in_quotes:
            if token_type == 'QUOTE':
                # Peek ahead
                if i + 1 < len(tokens) and tokens[i+1][0] == 'QUOTE':
                    current_field.append('"')
                    i += 1  # Skip
                else:
                    in_quotes = False
            else:
                # Inside a quoted field, all tokens are part of the field.
                current_field.append(token_value)
        else:
            if token_type == 'QUOTE':
                in_quotes = True
            elif token_type == 'DELIMITER':
                field = ''.join(current_field)
                current_row.append(field)
                current_field = []
            elif token_type == 'NEWLINE':
                field = ''.join(current_field)
                current_row.append(field)
                rows.append(current_row)
                current_row = []
                current_field = []
            else:
                current_field.append(token_value)
        i += 1

    # After processing all tokens, check if there's an unfinished field/row.
    if current_field or current_row:
        field = ''.join(current_field)
        current_row.append(field)
        rows.append(current_row)
    return rows

# --- SEMANTIC ANALYSIS ---
def semantic_analysis(rows):
    if not rows:
        return [], {}, {}

    header = rows[0]
    data_rows = rows[1:]

    # Use of a set to avoid duplicates.
    composers = set()
    period_distribution = {}
    period_titles = {}

    for row in data_rows:
        # Check if the row has the expected number of columns
        if len(row) < len(header):
            continue  # Skip incomplete rows
        nome = row[0].strip()
        periodo = row[3].strip()
        compositor = row[4].strip()

        composers.add(compositor)
        period_distribution[periodo] = period_distribution.get(periodo, 0) + 1
        period_titles.setdefault(periodo, []).append(nome)

    composers_list = sorted(list(composers))
    return composers_list, period_distribution, period_titles

# --- MAIN FUNCTION ---
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file>")
        sys.exit(1)

    csv_file_path = sys.argv[1]
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            csv_content = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Step 1: Lexical Analysis
    tokens = tokenize(csv_content, delimiter=';')
    # Step 2: Syntactic Analysis
    rows = parse_tokens(tokens)
    # Step 3: Semantic Analysis
    composers_list, period_distribution, period_titles = semantic_analysis(rows)

    # Display results
    print("Alphabetically ordered composers:")
    for composer in composers_list:
        print(" -", composer)

    print("\nDistribution of works by period:")
    for period, count in period_distribution.items():
        print(f" {period}: {count}")

    print("\nTitles by period:")
    for period, titles in period_titles.items():
        print(f" {period}:")
        for title in titles:
            print("    -", title)

if __name__ == '__main__':
    main()
