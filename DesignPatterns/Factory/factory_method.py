
"""
O Objetivo desse padrão de projeto é desacoplar as classes, o exemplo é de uma empresa de taxis
onde temos duas empreas, uma na ZonaNorte e outra ZonaSul e queremos que tenham diferentes
tipos de veiculos em cada zona, por isso criamos o VeiculoFactory como uma interface,
onde as subclasses iram determinar como será seu metodo abstrato que no nosso caso é
saber quais carros terão em cada zona;
"""
from abc import ABC, abstractclassmethod

# Interface
class Veiculo(ABC):
    @abstractclassmethod
    def buscar_cliente(self) -> None: pass

class CarroLuxo(Veiculo):

    def buscar_cliente(self) -> None:
        print('Carro de Luxo está buscando cliente...')

class CarroPopular(Veiculo):

    def buscar_cliente(self) -> None:
        print('Carro de Popular está buscando cliente...')

# Interface
class VeiculoFactory(ABC):
    
    def __init__(self, tipo: str) -> None:
        self.carro = self.get_carro(tipo)
    
    @staticmethod
    @abstractclassmethod
    def get_carro(tipo: str) -> Veiculo: pass

    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        """."""
        if tipo == 'Luxo':
            return CarroLuxo()
        elif tipo == 'Popular':
            return CarroPopular()
        else:
            assert 0, 'Veiculo não existe.'

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        """."""
        if tipo == 'Popular':
            return CarroPopular()
        else:
            assert 0, 'Veiculo não existe.'
