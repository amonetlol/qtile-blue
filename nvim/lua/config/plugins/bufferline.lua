return {
  "akinsho/bufferline.nvim",
  version = "*", -- ou "main" para latest
  dependencies = {
    "nvim-tree/nvim-web-devicons", -- obrigatório para ícones coloridos
  },
  event = "VeryLazy", -- carrega só quando necessário (bom para startup rápido)
  keys = {
    -- Atalhos opcionais para navegar nas abas
  },
  config = function()
    require("bufferline").setup({
      options = {
        mode = "buffers", -- mostra buffers (arquivos), não tabs reais do Vim
        numbers = "ordinal", -- mostra 1, 2, 3... nas abas (opcional: "buffer_id")
        diagnostics = "nvim_lsp", -- mostra erros/warnings do LSP (se você usar LSP no futuro)
        diagnostics_indicator = function(count, level)
          local icon = level:match("error") and " " or " "
          return " " .. icon .. count
        end,
        offsets = { -- evita sobrepor com Neo-tree (se usar)
          {
            filetype = "neo-tree",
            text = "Neo-tree",
            highlight = "Directory",
            text_align = "left",
          },
        },
        separator_style = "thin", -- estilo das separações: "slant" | "slope" | "thick" | "thin"
        always_show_bufferline = false, -- só mostra quando tem +1 buffer
      },
    })
  end,
}
