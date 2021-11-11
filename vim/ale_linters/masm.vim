call ale#linter#Define('masm', {
\   'name': 'masm',
\   'executable': '/opt/mindustry_parser/main.py',
\   'command': '/opt/mindustry_parser/main.py %s',
\   'callback': 'ale#handlers#unix#HandleAsWarning',
\   'output_stream': 'stdout',
\})
