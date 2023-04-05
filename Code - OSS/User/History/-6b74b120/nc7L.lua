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
end)
-- Highlight, edit, and navigate code using a fast incremental parsing library
use 'nvim-treesitter/nvim-treesitter'
  