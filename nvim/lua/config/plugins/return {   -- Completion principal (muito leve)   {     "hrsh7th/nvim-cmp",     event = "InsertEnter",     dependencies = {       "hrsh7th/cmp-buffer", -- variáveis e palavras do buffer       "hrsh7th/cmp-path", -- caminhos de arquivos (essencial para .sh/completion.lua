return {
  -- Completion principal (muito leve)
  {
    "hrsh7th/nvim-cmp",
    event = "InsertEnter",
    dependencies = {
      "hrsh7th/cmp-buffer", -- variáveis e palavras do buffer
      "hrsh7th/cmp-path", -- caminhos de arquivos (essencial para .sh/.py)
    },
    config = function()
      local cmp = require("cmp")

      cmp.setup({
        mapping = {
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_next_item()
            else
              fallback() -- insere tab normal se nada visível
            end
          end, { "i", "s" }),

          ["<S-Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_prev_item()
            else
              fallback()
            end
          end, { "i", "s" }),

          ["<CR>"] = cmp.mapping.confirm({ select = true }), -- Enter confirma
        },

        sources = {
          { name = "path", priority = 100 }, -- caminhos primeiro (prioridade alta)
          { name = "buffer", priority = 50, keyword_length = 2 }, -- variáveis locais
        },

        -- Visual clean (opcional)
        window = {
          completion = cmp.config.window.bordered(),
          documentation = cmp.config.window.bordered(),
        },
      })
    end,
  },
}
