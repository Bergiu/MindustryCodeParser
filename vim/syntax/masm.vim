if exists('b:current_syntax')
    finish
endif

syn keyword masmConditional jump end
syn keyword masmIO read write draw print drawflush printflush
syn keyword masmKeyword getlink control radar sensor ubind ucontrol uradar ulocate noop
" syn match masmSubcommands 
syn keyword masmTodos TODO XXX FIXME NOTE
syn keyword masmStructure set
syn keyword masmOperator op
syn match masmNumber "\v<\d+>"
syn match masmNumber "\v<\d+\.\d+>"
syn keyword masmBool true false
syn match masmComment "\v#.*$"
syn match masmAt "@[a-zA-Z0-9]*"
syntax region masmString start=/"/ end=/"/ oneline contains=masmInterpolatedWrapper
syntax region masmInterpolatedWrapper start="\v\\\(\s*" end="\v\s*\)" contained containedin=masmString contains=masmInterpolatedString
syntax match masmInterpolatedString "\v\w+(\(\))?" contained containedin=masmInterpolatedWrapper

hi def link masmConditional Conditional
hi def link masmOperator Operator
hi def link masmIO PreProc
hi def link masmKeyword Keyword
" hi def link masmSubcommands vimCommand
hi def link masmStructure Macro
hi def link masmNumber Number
hi def link masmString String
hi def link masmBool Boolean
hi def link masmAt Statement
hi def link masmComment Comment
highlight default link masmInterpolatedWrapper Delimiter

let b:current_syntax = 'masm'
