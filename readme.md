# Mindustry Logic Parser

This parser can be used to validate the mindustry logic code. It detects illegal characters, wrong syntax and validates the grammar.

For example examples/main.masm contains a command that is unknown to mindustry "import". Also there is another syntax error in line 4, because the op command because "op sub" command needs to get an ID (variable name) in this field and not an integer. The last bug found in the example is on line 6, because op doesn't have a subcommand called "del".

# Install

Download a release from github and extract it to `/opt/MindustryParser/`. Then you can execute `/opt/MindustryParser/main.py filename.masm` to check the file called `filename.masm`.

# NeoVim

You can use this program as linter for neovim ale.

Copy the file `vim/ale_linters/mdc.vim` to `~/.config/nvim/ftdetect/mdc.vim`.

You also need to install [vim-mindustry-logic syntax plugin](https://github.com/purofle/vim-mindustry-logic)
