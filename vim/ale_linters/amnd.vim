call ale#linter#Define('amnd', {
\   'name': 'amnd',
\   'executable': '~/workspace/Mindustry/AdvancedMindustryLogic/main.py',
\   'command': '~/workspace/Mindustry/AdvancedMindustryLogic/main.py %s',
\   'callback': 'ale#handlers#unix#HandleAsWarning',
\   'output_stream': 'stdout',
\})
