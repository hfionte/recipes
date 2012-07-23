" SET COLORSCHEME
set t_Co=256
set number
syntax enable
set background=dark
colorscheme zenburn

" SET TABS AND INDENTS
au FileType javascript setl tabstop=2 shiftwidth=2
au FileType html setl tabstop=2 shiftwidth=2
set tabstop=4
set shiftwidth=4
set expandtab
set autoindent
set smartindent
set smarttab

" SET SEARCH STUFF
set ignorecase
set smartcase
set hlsearch

" MAPPINGS
map <F4> <Esc>:tabnew<cr>
map <C-right> <Esc>:tabn<cr>
map <C-left> <Esc>:tabp<cr>
