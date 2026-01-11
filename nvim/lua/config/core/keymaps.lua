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

-- ╔══════════════════════════════════════════════════════════════╗
-- ║                      ABRIR TERMINAL                          ║
-- ╚══════════════════════════════════════════════════════════════╝

-- Ctrl + \ (backtick) → Toggle terminal (abre/fecha)
vim.keymap.set({ "n", "t" }, "<C-\\>", "<Cmd>ToggleTerm<CR>", {
  noremap = true,
  silent = true,
  desc = "Toggle terminal (horizontal split)",
})

-- ╔══════════════════════════════════════════════════════════════╗
-- ║                      NAVEGAÇÃO NAS ABAS (BUFFERLINE)         ║
-- ╚══════════════════════════════════════════════════════════════╝

-- Próxima aba (Next buffer)
vim.keymap.set("n", "<Tab>", "<Cmd>BufferLineCycleNext<CR>", {
  noremap = true,
  silent = true,
  desc = "Próxima aba",
})

-- Aba anterior (Prev buffer)
vim.keymap.set("n", "<S-Tab>", "<Cmd>BufferLineCyclePrev<CR>", {
  noremap = true,
  silent = true,
  desc = "Aba anterior",
})

-- Pin/Despin aba atual (Toggle Pin)
vim.keymap.set("n", "<leader>bp", "<Cmd>BufferLineTogglePin<CR>", {
  noremap = true,
  silent = true,
  desc = "Pin/Despin aba",
})

-- Fechar todas as abas não-pinned (Delete non-pinned buffers)
vim.keymap.set("n", "<leader>bP", "<Cmd>BufferLineGroupClose ungrouped<CR>", {
  noremap = true,
  silent = true,
  desc = "Fechar abas não-pinned",
})
