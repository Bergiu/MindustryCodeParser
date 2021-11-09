from .utils import load_code
import ply.lex as lex

instruction_names = [
    'write',
    'read',
    'draw',
    'drawflush',
    'print',
    'printflush',
    'getlink',
    'control',
    'radar',
    'sensor',
    'set',
    'op',
    'end',
    'jump',
    'ubind',
    'ucontrol',
    'uradar',
    'ulocate',
    'noop',
]

sub_instructions_draw = [
    'clear',
    'color',
    'stroke',
    'line',
    'rect',
    'lineRect',
    'poly',
    'linePoly',
    'triangle',
    'image',
]

sub_instructions_control = [
    'enabled',
    'shoot',
    'shootp',
    'configure',
    'color',
]

sub_instructions_radar_target = [
    'any',
    'enemy',
    'ally',
    'player',
    'attacker',
    'flying',
    'boss',
    'ground',
]

sub_instructions_radar_sort = [
    'distance',
    'health',
    'shield',
    'armor',
    'maxHealth',
]

sub_instructions_op = [
    'add',
    'sub',
    'mul',
    'div',
    'idiv',
    'mod',
    'pow',
    'equal',
    'notEqual',
    'land',
    'lessThan',
    'lessThanEq',
    'greaterThan',
    'greaterThanEq',
    'strictEqual',
    'shl',
    'shr',
    'or',
    'and',
    'xor',
    'not',
    'max',
    'min',
    'angle',
    'len',
    'noise',
    'abs',
    'log',
    'log10',
    'sin',
    'cos',
    'tan',
    'floor',
    'ceil',
    'sqrt',
    'rand',
]

# (only the ones that are missing)
sub_instructions_jump = [
    'always',
]

sub_instructions_ucontrol = [
    'idle',
    'stop',
    'move',
    'approach',
    'boost',
    'pathfind',
    'target',
    'targetp',
    'itemDrop',
    'itemTake',
    'payDrop',
    'payTake',
    'mine',
    'flag',
    'build',
    'getBlock',
    'within',
]

sub_instructions_ulocate = [
    'ore',
    'building',
    'spawn',
    'damaged',
    'core',
    'storage',
    'generator',
    'turret',
    'factory',
    'repair',
    'rally',
    'battery',
    'resupply',
    'reactor',
]


reserved_keys = [
    # 'if': 'IF',
    # 'then': 'THEN',
    # 'else': 'ELSE',
    # 'while': 'WHILE',
    # 'import',
    # 'define',
    # 'function',
    # 'exec',
]

reserved_keys.extend(instruction_names)
reserved_keys.extend(sub_instructions_draw)
reserved_keys.extend(sub_instructions_control)
reserved_keys.extend(sub_instructions_radar_target)
reserved_keys.extend(sub_instructions_radar_sort)
reserved_keys.extend(sub_instructions_op)
reserved_keys.extend(sub_instructions_jump)
reserved_keys.extend(sub_instructions_ucontrol)
reserved_keys.extend(sub_instructions_ulocate)

reserved = {res: res.upper() for res in reserved_keys}

# List of token names.   This is always required
tokens = [
             'INT',
             'DOUBLE',
             'STRING',
             'BOOL',
             'NEWLINE',
             'ID',
         ] + list(reserved.values())


def t_ID(t):
    r'@?[a-zA-Z_][a-zA-Z_0-9/.]*'
    t.type = reserved.get(t.value, 'ID')
    return t


# Regular expression rules for simple tokens
t_STRING = r'".*"'
t_BOOL = r'"(true|false)"'

t_ignore_COMMENT = r'\#.*'
# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


def t_DOUBLE(t):
    r'-?\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'-?\d+'
    t.value = int(t.value)
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


def do_lexing(data):
    lexer.input(data)
    while True:
        i = lexer.token()
        if i is None:
            break
        print(i)


if __name__ == '__main__':
    import sys
    text = load_code(sys.argv[1])
    do_lexing(text)
