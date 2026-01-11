return {
  "akinsho/toggleterm.nvim",
  version = "*",
  opts = {
    direction = "horizontal", -- ou "float", "vertical"
    size = 15, -- altura se horizontal
    start_in_insert = true,
    insert_mappings = true, -- permite usar o toggle dentro do terminal
    terminal_mappings = true,
    persist_size = true,
    -- NÃO coloque open_mapping aqui!
  },
}
