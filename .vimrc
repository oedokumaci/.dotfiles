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

