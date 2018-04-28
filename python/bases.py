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

def draw_base(num, base, k, width=1, height=1, scale=1):
    L = len(str(num))
    digits = '0'*(k-L) + str(num)
    print('\\begin{{tikzpicture}}[scale={}]'.format(scale))
    val = int(digits, base)
    for i, digit in enumerate(digits):
        print('\\draw[thick] ({},0) rectangle ({},{});'.format(i*width, (i+1)*width, height))
        print('\\node[thick] at ({},{}) {{{}}};'.format((i+.5)*width, height/2, digit))
        print('\\node[thick] at ({},{}) {{ $\\times$ }};'.format((i+.5)*width, -.3*height))
        print('\\node[thick] at ({},{}) {{ ${}^{{ {} }}$ }};'.format((i+.5)*width, -.75*height, base, k-i-1))
        print('\\node[thick] at ({},{}) {{ $\\left({}\\right)$ }};'.format((i+.5)*width, -1.5*height, base**(k-i-1)))
        print('\\draw[thick, ->] ({},{}) to ({},{});'.format((i+.5)*width, -2*height, (i+.5)*width, -3*height))
        print('\\node[thick] at ({},{}) {{ ${}_{{10}}$ }};'.format((i+.5)*width, -3.5*height, d[digit]*base**(k-i-1)))
        if i!=0:
            print('\\node[] at ({},{}) {{$+$}};'.format(i*width, -3.5*height))
        print('\\node[] at ({},{}) {{ $={}_{{10}}$ }};'.format(width*(k+.5), -3.5*height, val))
    print('\\end{tikzpicture}')

def draw_base_fancy(num, base, k, args=[], scale=1.0):
	digits_str = k*'0' + str(num)
	val = sum(d[digit]*base**i for i, digit in enumerate(digits_str[::-1]))
	L = len(digits_str)
	box_args = ','.join(args)
	print('\\begin{{tikzpicture}}[scale={}]'.format(scale))
	print('\\node[] at ({},.5) {{Base-{} Value}};'.format((1.5*L+5)/3, base))
	print('\\node[rotate=270] at ({},{}) {{Base-10 Value}};'.format(1.5*L+5, -(L+k)/2-1, base))
	for i, digit in enumerate(digits_str):
		j = L+k-i-1
		print('\\node[draw, fit={{({},0)({},-1)}}, inner sep=0pt]({}) {{ ${}$ }};'.format(1.5*i, 1.5*(i+1), 'top'+str(i), digit))
		print('\\node[draw, fit={{({},{})({},{})}}, inner sep=0pt]({}) {{ ${}$ }};'.format(1.5*L, -i-1, 1.5*(L+1), -i-2, 'right'+str(i), base**i))
		print('\\draw[->] ({},{}) -- ({},{}) -- ({},{});'.format(1.5*j+.75, -1, 1.5*j+.75, -i-1.5, 1.5*L, -i-1.5))
		print('\\node[draw, fit={{({},{})({},{})}}, inner sep=0pt] {{ $\\times{}=$ }};'.format(1.5*(L+1), -i-1, 1.5*(L+2), -i-2, d[digits_str[L+k-i-1]]))
		print('\\node[draw, fit={{({},{})({},{})}}, inner sep=0pt] {{ ${}$ }};'.format(1.5*(L+2), -i-1, 1.5*(L+3), -i-2, d[digits_str[L+k-i-1]]*base**i))
	print('\\node[draw, fit={{({},{})({},{})}}, inner sep=0pt] {{ Total }};'.format(1.5*(L), -L-1, 1.5*(L+2), -L-2))
	print('\\node[draw, fit={{({},{})({},{})}}, inner sep=0pt] {{ ${}$ }};'.format(1.5*(L+2), -L-1, 1.5*(L+3), -L-2, val))
	print('\\end{tikzpicture}')
