return {
  -- 1. Mason (instalador) - carrega primeiro
  {
    "mason-org/mason.nvim",
    opts = {
      ui = {
        icons = {
          package_installed = "✓",
          package_pending = "➜",
          package_uninstalled = "✗",
        },
      },
    },
  },

  -- 2. Mason-lspconfig (auto-instala e auto-ativa servers)
  {
    "mason-org/mason-lspconfig.nvim",
    dependencies = {
      "mason-org/mason.nvim",
      "neovim/nvim-lspconfig",
    },
    opts = {
      ensure_installed = { "lua_ls" }, -- adicione mais: "rust_analyzer", "ts_ls", "pyright", etc.
      automatic_installation = true, -- instala automaticamente ao abrir arquivo com LSP faltando
      automatic_enable = true, -- ativa automaticamente com vim.lsp.enable() (novo padrão!)
    },
  },

  -- 3. nvim-lspconfig (configs + customizações)
  {
    "neovim/nvim-lspconfig",
    event = { "BufReadPre", "BufNewFile" },
    dependencies = { "hrsh7th/cmp-nvim-lsp" }, -- se usa nvim-cmp
    config = function()
      -- Capabilities (para autocompletion com cmp)
      local capabilities = vim.lsp.protocol.make_client_capabilities()
      capabilities = require("cmp_nvim_lsp").default_capabilities(capabilities)

      -- on_attach: keymaps, etc. (seus mapeamentos)
      local on_attach = function(client, bufnr)
        local opts = { buffer = bufnr, silent = true }
        local keymap = vim.keymap.set

        keymap("n", "gr", "<cmd>Telescope lsp_references<CR>", opts)
        keymap("n", "gd", vim.lsp.buf.declaration, opts)
        keymap("n", "gD", "<cmd>Telescope lsp_definitions<CR>", opts)
        keymap("n", "gi", "<cmd>Telescope lsp_implementations<CR>", opts)
        keymap("n", "gt", "<cmd>Telescope lsp_type_definitions<CR>", opts)
        keymap("n", "<leader>rn", vim.lsp.buf.rename, opts)
        keymap("n", "<leader>d", "<cmd>Telescope diagnostics bufnr=0<CR>", opts)
        keymap("n", "<leader>D", vim.diagnostic.open_float, opts)
        keymap("n", "[d", vim.diagnostic.goto_prev, opts)
        keymap("n", "]d", vim.diagnostic.goto_next, opts)
        keymap("n", "K", vim.lsp.buf.hover, opts)
        keymap("n", "<leader>rs", ":LspRestart<CR>", opts)
      end

      -- Ícones nos gutters (signs)
      local signs = { Error = " ", Warn = " ", Hint = "󰠠 ", Info = " " }
      for type, icon in pairs(signs) do
        local hl = "DiagnosticSign" .. type
        vim.fn.sign_define(hl, { text = icon, texthl = hl, numhl = "" })
      end

      -- Config custom para lua_ls (seu caso)
      vim.lsp.config("lua_ls", {
        capabilities = capabilities,
        on_attach = on_attach,
        settings = {
          Lua = {
            diagnostics = { globals = { "vim" } },
            completion = { callSnippet = "Replace" },
            -- workspace = { checkThirdParty = false },
          },
        },
      })

      -- Para outros servers: o mason-lspconfig ativa automaticamente
      -- Se quiser customizar outro, adicione vim.lsp.config("ts_ls", { ... })
    end,
  },
}
