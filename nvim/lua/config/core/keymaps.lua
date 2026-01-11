vim.g.mapleader = " "

vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

vim.keymap.set("n", "J", "mzJ`z")
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")

vim.keymap.set("i", "kj", "<Esc>")

vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])

vim.keymap.set("n", "<leader><leader>", function()
  vim.cmd("so")
end)

vim.keymap.set("n", "<leader>qq", function()
  vim.cmd("q")
end)

vim.keymap.set("n", "<leader>w", function()
  vim.cmd("w")
end)

vim.keymap.set('n', 'y', '"+y')
vim.keymap.set('v', 'y', '"+y')

vim.keymap.set("n", "<leader>oc", "O{/*")
vim.keymap.set("n", "<leader>op", "o*/}")

vim.keymap.set("n", "<leader>jf", function()
  vim.cmd("%!jq '.'")
end)

vim.keymap.set("n", "<leader>bb", function()
  vim.cmd("e #")
end)

-- Focar no Neo-tree (ou abrir se estiver fechado)
vim.keymap.set("n", "<leader>t", "<Cmd>NvimTreeFocus<CR>")

-- ╔══════════════════════════════════════════════════════════════╗
-- ║                SALVAR E SAIR (Ctrl + S / Ctrl + Q)           ║
-- ╚══════════════════════════════════════════════════════════════╝

-- Ctrl + S → Salvar o buffer atual (:w)
vim.keymap.set({ "n", "i", "v" }, "<C-s>", "<Cmd>w<CR>", { noremap = true, silent = true })

-- Ctrl + Q → Salvar e sair (:wq)
vim.keymap.set("n", "<C-q>", "<Cmd>wqa<CR>", { noremap = true, silent = true })
