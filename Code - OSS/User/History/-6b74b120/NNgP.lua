vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function()
  -- Packer сам себя
  use 'wbthomason/packer.nvim'

  -----------------------------------------------------------
  -- LSP & Autocomplete
  -----------------------------------------------------------
  use {
    "williamboman/mason.nvim",
    "williamboman/mason-lspconfig.nvim",
    "neovim/nvim-lspconfig",
  }

  -- Highlight, edit, and navigate code using a fast incremental parsing library
  use 'nvim-treesitter/nvim-treesitter'

  -- File manager
  
  use { 'nvim-tree/nvim-tree.lua',
  requires = 'nvim-tree/nvim-web-devicons',
  config = function() require'nvim-tree'.setup {} end, }

    -----------------------------------------------------------
  -- ПЛАГИНЫ ВНЕШНЕГО ВИДА
  -----------------------------------------------------------
  -- Иконки
  use 'nvim-tree/nvim-web-devicons'

  -- Информационная строка внизу
  use {'nvim-lualine/lualine.nvim',
  requires = {'kyazdani42/nvim-web-devicons', opt = true},
  config = function()
      require('lualine').setup()
  end, }

  -- Notifier
  use {"vigoux/notifier.nvim",
  config = function()
    require'notifier'.setup()
  end, }

  -- Цветовые схемы
  use {"ellisonleao/gruvbox.nvim", requires = {"rktjmp/lush.nvim"}}
  use 'marko-cerovac/material.nvim'
  use 'joshdick/onedark.vim'
  use 'ayu-theme/ayu-vim'



end)