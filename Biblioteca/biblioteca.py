# Classe para gerenciar
# Atributos: acervo (uma lista de objetos Livro e Revista) e usuarios (uma lista de objetos Usuario).

#Métodos:
# adicionar_material(material)
# remover_material(material)
# emprestar_material(usuario, titulo): Este método deve verificar se o material existe no acervo e se está disponível. 
# Se sim, remove do acervo e adiciona ao historico_emprestimos do usuario.
# devolver_material(usuario, titulo): Faz o processo inverso.
# consultar_acervo(): Exibe todos os materiais disponíveis no acervo, utilizando o método exibir_informacoes() de cada objeto.