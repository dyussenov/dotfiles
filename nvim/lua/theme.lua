local cmd = vim.cmd             -- execute Vim commands
local g = vim.g                 -- global variables
local opt = vim.opt             -- global/buffer/windows-scoped options

-----------------------------------------------------------
-- Цветовая схема
-----------------------------------------------------------
opt.termguicolors = true      --  24-bit RGB colors

-- gruvbox
-- opt.background = "light" -- "dark" by default
-- cmd 'colorscheme gruvbox'

-- ayu
-- g.ayucolor="light"
-- cmd 'colorscheme ayu'

-- ondedark
-- cmd 'colorscheme onedark'

-- material.nvim
-- g.material_style = "palenight"
-- g.material_style = "lighter"
-- g.material_style = "oceanic"
cmd 'colorscheme material'
