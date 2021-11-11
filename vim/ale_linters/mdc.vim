call ale#linter#Define('mdc', {
\   'name': 'mdc',
\   'executable': '/opt/MindustryParser/main.py',
\   'command': '/opt/MindustryParser/main.py %s',
\   'callback': 'ale#handlers#unix#HandleAsWarning',
\   'output_stream': 'stdout',
\})
