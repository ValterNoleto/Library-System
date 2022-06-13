# Verificar se o livro já foi emprestado pela biblioteca = CONFERE!
# Buscar algum livro que não foi cadastrado na biblioteca = CONFERE!
# Devolução de um livro que não foi emprestado = CONFERE!
# Limitar o empréstimo para usuário em no máximo 3 livros = CONFERE!
# Empréstimo com um funcionário não cadastrado = CONFERE!

import unittest
from main import *


class TestCase(unittest.TestCase):

    # Verificar se o livro já foi emprestado pela biblioteca
    def test_verificandoLivroEmprestado(self):
        biblioteca = Biblioteca()
        livro = Livro("54", "O segredo da mente milionária")
        funcionario = Funcionario("01578932188", "Fulano de Tal")
        usuario = Usuario("Valtinho")

        biblioteca.cadastrarFuncionario(funcionario)
        biblioteca.cadastrarLivro(livro)

        biblioteca.realizarEmprestimo(funcionario, livro, usuario)

        verificacao_emprestimo = biblioteca.realizarEmprestimo(funcionario, livro, usuario)
        self.assertEqual(verificacao_emprestimo, "Empréstimo realizado com sucesso!")

    # Buscar algum livro que não foi cadastrado na biblioteca
    def test_buscandoLivroNaoCadastrado(self):
        biblioteca = Biblioteca()
        livro = Livro("1", "Diário de um banana")

        buscar_livro = biblioteca.procurarLivro(livro.nome)
        self.assertEqual(buscar_livro, "O livro procurado, não foi encontrado!")

    # Devolução de um livro que não foi emprestado
    def test_devolvendoLivroNaoEmprestado(self):
        biblioteca = Biblioteca()
        livro = Livro("69", "Dom Casmurro")
        funcionario = Funcionario("12332145665", "Caboclo")

        biblioteca.cadastrarFuncionario(funcionario)
        biblioteca.cadastrarLivro(livro)

        devolver_livro = biblioteca.realizarDevolucao(funcionario, livro)
        self.assertEqual(devolver_livro, "A devolução não pôde ser concluída, o livro não foi emprestado!")

    # Limitar o empréstimo para usuário em no máximo 3 livros
    def test_limitarEmprestimo(self):
        biblioteca = Biblioteca()
        livro_a = Livro("56", "Mein Kampf")
        livro_b = Livro("98", "Sútil arte de ligar o foda-se!")
        livro_c = Livro("41", "Pequeno princípe")
        livro_d = Livro("36", "1922")

        funcionario = Funcionario("79839648052", "Desconhecido")

        biblioteca.cadastrarFuncionario(funcionario)

        biblioteca.cadastrarLivro(livro_a)
        biblioteca.cadastrarLivro(livro_b)
        biblioteca.cadastrarLivro(livro_c)
        biblioteca.cadastrarLivro(livro_d)

        usuario = Usuario("Curioso")
        biblioteca.cadastrarLivro(usuario)

        biblioteca.realizarEmprestimo(funcionario, livro_a, usuario)
        biblioteca.realizarEmprestimo(funcionario, livro_b, usuario)
        biblioteca.realizarEmprestimo(funcionario, livro_c, usuario)

        verificar_emprestimo = biblioteca.realizarEmprestimo(funcionario, livro_d, usuario)
        self.assertEqual(verificar_emprestimo, "O limite máximo de empréstimos foi atingido!")

    # Empréstimo com um funcionário não cadastrado
    def test_funcionarioNaoCadastrado(self):
        biblioteca = Biblioteca()
        livro = Livro("22", "Endurance")
        funcionario = Funcionario("55549320846", "Doidão")
        usuario = Usuario("Irvayne")

        biblioteca.cadastrarLivro(livro)

        pedir_emprestimo = biblioteca.realizarEmprestimo(livro, funcionario, usuario)
        self.assertEqual(pedir_emprestimo, "Funcionário inválido!")
