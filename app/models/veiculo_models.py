# Importa os tipos de coluna e ForeignKey do SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

# Importa o relationship para navegação entre tabelas
from sqlalchemy.orm import relationship

# Importa a Base criada no database.py
from app.database import Base


# Classe que representa a tabela "veiculos"
class Veiculo(Base):

    # Nome da tabela no banco Azure SQL
    __tablename__ = "veiculos"

    # COLUNAS DA TABELA

    # ID do veículo (chave primária)
    id = Column(Integer, primary_key=True, index=True)

    # Placa do veículo (obrigatório e único, não podem existir duas iguais)
    placa = Column(String(10), nullable=False, unique=True)

    # Modelo e Marca
    modelo = Column(String(50), nullable=False)
    marca = Column(String(50), nullable=False)

    # Ano do veículo
    ano = Column(Integer)

    # CHAVE ESTRANGEIRA (Foreign Key)
    # Liga este veículo ao ID de um cliente na tabela "clientes"
    cliente_id = Column(Integer, ForeignKey("clientes.id"))

    # RELACIONAMENTOS (Mágica do SQLAlchemy)
    # Permite acessar os dados do cliente dono do veículo diretamente no código
    cliente = relationship("Cliente", back_populates="veiculos")

    # Permite acessar todas as ordens de serviço deste veículo
    ordens_servico = relationship("OrdemServico", back_populates="veiculo")
