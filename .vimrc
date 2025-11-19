" ================================
"        BASIC UI SETTINGS
" ================================

" Show relative line numbers, with absolute number on the current line
set relativenumber
set number

" Enable syntax highlighting
syntax on


" ================================
"        TABS & INDENTATION
" ================================

" Default indentation: 2 spaces
set tabstop=2        " How many spaces a <Tab> counts for
set shiftwidth=2     " How many spaces auto-indent uses
set softtabstop=2    " Makes backspace delete 2 spaces
set expandtab        " Convert tabs to spaces

" Python uses 4-space indentation
augroup python_indent
  autocmd!
  autocmd FileType python setlocal tabstop=4 shiftwidth=4 softtabstop=4 expandtab
augroup END

" Auto indentation settings
set autoindent       " Keep indentation from previous line
set smartindent      " Automatic smart indentation for many languages


" ================================
"           INSERT MODE
" ================================

" Map 'jj' and 'jk' to escape
inoremap jj <Esc>
inoremap jk <Esc>
set timeoutlen=500   " Shorter timeout so jj/jk feels instant


" ================================
"           NAVIGATION
" ================================

nnoremap gf <C-]>    " Go to file under cursor or tag jump
nnoremap Q <nop>     " Disable Ex mode (dangerous)


" ================================
"           LEADER KEY
" ================================

let mapleader = " "  " Space as <Leader>


" ================================
"          FILE OPERATIONS
" ================================

nnoremap <Leader>w :w<CR>      " Save file
nnoremap <Leader>q :q<CR>      " Quit
nnoremap <Leader>x :x<CR>      " Save and quit

" System clipboard
nnoremap <Leader>y "+y         " Yank to system clipboard
nnoremap <Leader>p "+p         " Paste from system clipboard


" ================================
"         MOVEMENT HELPERS
" ================================

nnoremap <Leader>h ^           " Jump to first non-blank char
nnoremap <Leader>l $           " Jump to end of line
nnoremap <Leader>j 20j         " Move 20 lines down
nnoremap <Leader>k 20k         " Move 20 lines up


" ================================
"        BUFFER MANAGEMENT
" ================================

nnoremap <Leader>bd :bd<CR>    " Delete buffer
nnoremap <Leader>bn :bnext<CR> " Next buffer
nnoremap <Leader>bp :bprevious<CR> " Previous buffer


" ================================
"           TAB MANAGEMENT
" ================================

nnoremap <Leader>tn :tabnew<CR>    " Open new tab
nnoremap <Leader>tc :tabclose<CR>  " Close current tab
nnoremap <Leader>to :tabonly<CR>   " Close all other tabs


" ================================
"       SEARCH & REPLACE (smart)
" ================================

" Case-sensitive rename word under cursor (global)
nnoremap <Leader>r :%s/\<<C-r><C-w>\>/<C-r><C-w>/g<Left><Left><Left>

" Case-insensitive rename word under cursor (global)
nnoremap <Leader>R :%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>


" ================================
"       UNYANKED OPERATIONS
" ================================

" Delete line without yanking (silent dd)
nnoremap <leader>D "_dd

" ================================
"        VISUAL LINE MOVEMENT
" ================================

" Move visual selection down
vnoremap J :m '>+1<CR>gv=gv

" Move visual selection up
vnoremap K :m '<-2<CR>gv=gv


" ================================
"      CENTERED MOVEMENT
" ================================

" Keep cursor centered when moving half-page
nnoremap <C-d> <C-d>zz
nnoremap <C-u> <C-u>zz

" Keep cursor centered during search navigation
nnoremap n nzzzv
nnoremap N Nzzzv


" ================================
"     RE-INDENT PASTED BLOCK
" ================================

" Re-indent last pasted text (useful after 'p')
nnoremap =ap ma=ap'a

