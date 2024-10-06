from main import db
from modelos import PaginaJogo
from itertools import islice

atributosma = [
    'ResumoJogo', 'LinkDownload', 'DescricaoJogo',
    'TituloTutorial', 'DescricaoTutorial', 'TituloNoticia1', 'DescricaoNoticia1',
    'TituloNoticia2', 'DescricaoNoticia2', 'TituloVideo', 'DescricaoVideo',
    'LinkVideo', 'JogoID', 'FormValidado', 'FormToken'
]
atributosmi = [
    'resumojogo', 'linkdownload', 'descricaojogo',
    'titulotutorial', 'descricaotutorial', 'titulonoticia1', 'descricaonoticia1',
    'titulonoticia2', 'descricaonoticia2', 'titulovideo', 'descricaovideo',
    'linkvideo', 'jogoid', 'formvalidado', 'formtoken'
]
class Pagina:
    def __init__(self, **kwargs) -> None:
        for atributo in atributosma:
            setattr(self, atributo.lower(), kwargs.get(atributo))
    
    def __repr__(self) -> str:
        valores = ', '.join(f"{atributo}={getattr(self, atributo)!r}" for atributo in atributosmi)
        return f"Pagina({valores})"

    def atualizar_pagina_forms(*args):
        try:
            kwargs = {atributo: valor for atributo, valor in zip(atributosma, args)}
            kwargs_limited = dict(islice(kwargs.items(), 13))  # Pega apenas os 13 primeiros itens
            pagina = PaginaJogo.get_pagina_by_jogoid(kwargs_limited['JogoID'])  # Obtém a instância existente
            pagina.update_columns(kwargs_limited)  # Atualiza a instância
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao atualizar: {e}")