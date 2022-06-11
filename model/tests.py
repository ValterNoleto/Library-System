#verificar livro ja emprestado
#buscar livro nao cadastrado na biblioteca
#devolver um livro nao emprestado
#limitar emprestimo de no maximo 3 livros
#solicitar emprestimo com funcionario invalido

import unittest
from main import *

class Tests(unittest.TestCase):
    def test_VerificarLivroJaEmprestado(self):
        livro = Livro(1, "Como programar em python pulando paraquedas")
        biblioteca = Biblioteca()
        funcionario_novo = Funcionario(999999999999, "Dona Neusa")
        biblioteca.cadastrarFuncionario(funcionario_novo)

        usuario_qualquer = Usuario("Irvani", "Mora Na caixa prego")
        resposta = biblioteca.realizarEmprestimo(funcionario_novo, livro, usuario_qualquer)

        self.assertEqual("Emprestimo realizado com sucesso", resposta)

        nova_resposta = biblioteca.realizarEmprestimo(funcionario_novo, livro, usuario_qualquer)
        self.assertNotEquals("Emprestimo realizado com sucesso", nova_resposta)
