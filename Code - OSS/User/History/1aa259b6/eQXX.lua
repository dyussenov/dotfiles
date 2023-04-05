local map = vim.api.nvim_set_keymap
local noremap = {noremap = true}
local default_opts = {noremap = true, silent = true}

-- System clopboard
map('v', '<leader>y', '"+y', noremap)
map('n', '<leader>y', '"+y', noremap)
map('n', '<leader>Y', '"+Y', noremap)
map('n', 'dD', '<esc>ggdGi', noremap)

-- clear last search highlight
map('n', ',<space>', ':nohl<CR>', default_opts)

-- deprecate skip selection after indenting
map('v', '<', '<gv', default_opts)
map('v', '>', '>gv', default_opts)

-- nvim-tree
map('n', '<leader>df', ':NvimTreeRefresh<CR>:NvimTreeToggle<CR>', default_opts)

-- Neovim motions on speed! 
map('n', 'f', '<cmd>:HopWord<CR>', default_opts)
map('v', 'f', '<cmd>:HopWord<CR>', default_opts)
map('n', 'F', '<cmd>:HopWordCurrentLine<CR>', default_opts)

-- LSP
map('n', '<leader>lr', ':LspRestart<CR>', default_opts) -- r=restart
map('n', '<leader>ll', ':LspStart<CR>', default_opts) -- l=launch
map('n', '<leader>ls', ':LspStop<CR>', default_opts) -- s=stop
map('n', '<leader>m', ':Mason<CR>', default_opts)

-- MarkDown
map('n', '<leader>t', ':TableFormat<CR>', default_opts)

-- <F11> Проверка орфографии  для русского и английского языка
map('n', '<F11>', ':set spell!<CR>', default_opts)
map('i', '<F11>', '<C-O>:set spell!<CR>', default_opts)

map('n', '<F5>', ':65vsplit | term python %<CR>i', default_opts)
-- map('n', '<leader>e', ':15split | term python %<CR>i', default_opts)

-- <F8>  Показ дерева классов и функций, плагин majutsushi/tagbar
-- map('n', '<F8>', ':TagbarToggle<CR>', default_opts)

-- config reloading
map('n', '<leader>R', ':source $MYVIMRC<CR>', default_opts)
