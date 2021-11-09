if exists('b:current_syntax')
    finish
endif

syn keyword amndConditional jump end
syn keyword amndIO read write draw print drawflush printflush
syn keyword amndKeyword getlink control radar sensor ubind ucontrol uradar ulocate noop
" syn match amndSubcommands 
syn keyword amndTodos TODO XXX FIXME NOTE
syn keyword amndStructure set
syn keyword amndOperator op
syn match amndNumber "\v<\d+>"
syn match amndNumber "\v<\d+\.\d+>"
syn keyword amndBool true false
syn match amndComment "\v#.*$"
syn match amndAt "@[a-zA-Z0-9]*"
syntax region amndString start=/"/ end=/"/ oneline contains=amndInterpolatedWrapper
syntax region amndInterpolatedWrapper start="\v\\\(\s*" end="\v\s*\)" contained containedin=amndString contains=amndInterpolatedString
syntax match amndInterpolatedString "\v\w+(\(\))?" contained containedin=amndInterpolatedWrapper

hi def link amndConditional Conditional
hi def link amndOperator Operator
hi def link amndIO PreProc
hi def link amndKeyword Keyword
" hi def link amndSubcommands vimCommand
hi def link amndStructure Macro
hi def link amndNumber Number
hi def link amndString String
hi def link amndBool Boolean
hi def link amndAt Statement
hi def link amndComment Comment
highlight default link amndInterpolatedWrapper Delimiter

let b:current_syntax = 'amnd'
