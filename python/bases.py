d = {'0':0,
     '1':1,
     '2':2,
     '3':3,
     '4':4,
     '5':5,
     '6':6,
     '7':7,
     '8':8,
     '9':9,
     'A':10,
     'B':11,
     'C':12,
     'D':13,
     'E':14,
     'F':15}

def draw_base_normal(num, base, k, width=1, height=1, scale=1, color='blue', box_args=['thick']):
    digits_str = k*'0' + str(num)
    val = sum(d[digit]*base**i for i, digit in enumerate(digits_str[::-1]))
    L = len(digits_str)
    box_args = ','.join(box_args)
    print('\\begin{{tikzpicture}}[scale={}]'.format(scale))
    for i, digit in enumerate(digits_str):
        j = L+k-i-1
        col = color + '!' + str(int(i/L*40+5))
        col_inv = color + '!' + str(int(j/L*40+5))
        print('\\node[fill={}, draw, fit={{({},0)({},-1)}}, inner sep=0pt, {}] {{ ${}$ }};'.format(col_inv, 1.5*i, 1.5*(i+1), box_args, digit))
    print('\\draw[<-, thick] (0.75, -1.25) to (0.75, -2);')
    print('\\node[]() at (0.75, -2.5) {{ Most Significant Digit }};')
    print('\\draw[<-, thick] ({}, -1.25) to ({}, -2);'.format(1.5*L-0.75, 1.5*L-0.75))
    print('\\node[]() at ({}, -2.5) {{ Least Significant Digit }};'.format(1.5*L-0.75))
    print('\\end{tikzpicture}')

def draw_base_fancy(num, base, k, box_args=['thick'], arrow_args=['thick'], color='blue', scale=1.0):
    digits_str = k*'0' + str(num)
    val = sum(d[digit]*base**i for i, digit in enumerate(digits_str[::-1]))
    L = len(digits_str)
    box_args = ','.join(box_args)
    arrow_args = ','.join(arrow_args)
    print('\\begin{{tikzpicture}}[scale={}]'.format(scale))
    print('\\node[] at ({},.5) {{Base-{} Value}};'.format((1.5*L+5)/3, base))
    print('\\node[rotate=270] at ({},{}) {{Base-10 Value}};'.format(1.5*L+3.5, -(L+k)/2-1, base))
    for i, digit in enumerate(digits_str):
        j = L+k-i-1
        col = color + '!' + str(int(i/L*40+5))
        col_inv = color + '!' + str(int(j/L*40+5))
        print('\\node[fill={}, draw, fit={{({},0)({},-1)}}, inner sep=0pt, {}] {{ ${}$ }};'.format(col_inv, 1.5*i, 1.5*(i+1), box_args, digit))
        print('\\node[fill={}, draw, fit={{({},{})({},{})}}, inner sep=0pt, {}] {{ $\\times{}$ }};'.format(col, 1.5*L, -i-1, 1.5*(L+1), -i-2, box_args, base**i))
        print('\\node[fill={}, draw, fit={{({},{})({},{})}}, inner sep=0pt, {}] {{ $={}$ }};'.format(col, 1.5*(L+1), -i-1, 1.5*(L+2), -i-2, box_args, d[digits_str[L+k-i-1]]*base**i))
        print('\\draw[->, {}] ({},{}) -- ({},{}) -- ({},{});'.format(arrow_args, 1.5*j+.75, -1, 1.5*j+.75, -i-1.5, 1.5*L, -i-1.5))
    print('\\node[draw, fit={{({},{})({},{})}}, inner sep=0pt, very thick] {{ Total }};'.format(1.5*(L), -L-1, 1.5*(L+1), -L-2))
    print('\\node[draw, fit={{({},{})({},{})}}, inner sep=0pt, very thick] {{ $={}$ }};'.format(1.5*(L+1), -L-1, 1.5*(L+2), -L-2, val))
    print('\\end{tikzpicture}')

