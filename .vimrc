" Show relative line numbers
set relativenumber
set number  " still shows the absolute number on the current line

" Enable syntax highlighting
syntax on

" Set tab width to 2 spaces for general use
set tabstop=2        " Number of spaces a <Tab> counts for when editing
set shiftwidth=2     " Number of spaces used for autoindent
set softtabstop=2    " Makes backspace remove 2 spaces at once
set expandtab        " Insert spaces instead of tab characters

" Language-specific override: Python
augroup python_indent
  autocmd!
  autocmd FileType python setlocal tabstop=4 shiftwidth=4 softtabstop=4 expandtab
augroup END

" Auto-indent new lines to match the previous line
set autoindent
set smartindent       " Optional: Smarter indentation for some languages

" Map jj and jk to Escape in insert mode
inoremap jj <Esc>
inoremap jk <Esc>
set timeoutlen=500  " Shorten timeout for quicker Escape recognition

" Leader stuff
let mapleader = " "

nnoremap <Leader>w :w<CR>
nnoremap <Leader>q :q<CR>
nnoremap <Leader>x :x<CR>            " Save and quit
nnoremap <Leader>y "+y
nnoremap <Leader>p "+p

nnoremap <Leader>h ^
nnoremap <Leader>l $
nnoremap <Leader>j 20j
nnoremap <Leader>k 20k

nnoremap <Leader>bd :bd<CR>          " Delete buffer
nnoremap <Leader>bn :bnext<CR>       " Next buffer
nnoremap <Leader>bp :bprevious<CR>   " Previous buffer
nnoremap <Leader>tn :tabnew<CR>      " New tab
nnoremap <Leader>tc :tabclose<CR>    " Close tab
nnoremap <Leader>to :tabonly<CR>     " Close other tabs

