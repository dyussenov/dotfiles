local map = vim.api.nvim_set_keymap
local noremap = {noremap = true}
local default_opts = {noremap = true, silent = true}

-- config reloading
map('n', '<leader>R', ':source $MYVIMRC<CR>', noremap)