"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID

ANOTAÇÕES SOBRE COMPRRENSÃO DO TEMA:

    -> Utilizamos as Factory para gerenciar qual classe será enviada
    para o cliente, ou seja, utilizamos basicamente o (Principio de inverão de dependencia)
    onde poderemos editar tranquilamente os métodos e funcionalidades
    das classes que o cliente não instancia e apenas modificamos as
    informações dentro da Factory, sem precisar que o usuário mude
    os métodos que ele já utiliza.
"""
from abc import ABC, abstractclassmethod

# Interface
class Veiculo(ABC):

    @abstractclassmethod
    def buscar_cliente(self) -> None: 
        pass

# Classes Concretas
class CarroLuxo(Veiculo):

    def buscar_cliente(self) -> None:
        print('Carro de Luxo está buscando cliente...')

class CarroPopular(Veiculo):

    def buscar_cliente(self) -> None:
        print('Carro de Popular está buscando cliente...')

# Factory
class VeiculoFactory:
    
    def __init__(self, tipo: str) -> None:
        self.carro = self.get_carro(tipo)
    
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        """."""
        if tipo == 'Luxo':
            return CarroLuxo()
        elif tipo == 'Popular':
            return CarroPopular()
        else:
            assert 0, 'Veiculo não existe.'

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


if __name__ == '__main__':
    from random import choice

    carros_disponiveis = ['Luxo', 'Popular']
    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()