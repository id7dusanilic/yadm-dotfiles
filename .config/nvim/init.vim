" Plugins section *************************************************************
" Using vim-plug to handle plugins
call plug#begin('~/.local/share/nvim/plugged')
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'vim-python/python-syntax'
Plug 'kovetskiy/sxhkd-vim'
Plug 'ggandor/leap.nvim'
Plug 'sainnhe/edge'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

let g:coc_global_extensions = [
    \ 'coc-sh',
    \ 'coc-pyright',
    \ 'coc-json',
    \ 'coc-pairs',
    \ ]

" Autocmds ********************************************************************

" Update keyboard bindings when sxhkdrc is updated
autocmd BufWritePost *sxhkdrc !killall -s SIGUSR1 sxhkd

" Basic settings **************************************************************

" Encoding
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=utf-8

" Line numbers
set number relativenumber

" Tabs
set tabstop=4
set shiftwidth=4
set expandtab

" Clipboard
set clipboard=unnamedplus

" Set the viminfo file
set viminfo+=n~/.config/nvim/viminfo

" Enable mouse support
set mouse=a

" Keybindings
vmap q <Esc>
imap jk <Esc>
nmap j gj
nmap k gk

nnoremap <F5> :let _s=@/<Bar>:%s/\s\+$//e<Bar>:let @/=_s<Bar><CR>

" Shortcutting split navigation, saving a keypress
map <C-h> <C-w>h
map <C-j> <C-w>j
map <C-k> <C-w>k
map <C-l> <C-w>l

" Show cursorline
set cursorline

" Show matches for [], {}, ()
set showmatch

" Misc
set title
set hidden

" Colors
syntax enable
colorscheme edge

" Python syntax plugin
let g:python_highlight_all = 1
