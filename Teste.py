from Conexao import criar_tabela, inserir_registro, consultar_todos, remover_registro

# criar_tabela()
#inserir_registro("Maria", "maria@email.com")
#remover_registro(7)

clientes = consultar_todos()
for cliente in clientes:
    print(cliente)