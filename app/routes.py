from flask import Blueprint, request, jsonify, current_app
from .models import HabitoAlimentar, db
from .utils import *

form_bp = Blueprint('formulario', __name__)



@form_bp.route('/formulario', methods=['POST'])
def formulario_dados():
    try:
        dados = request.get_json()
        current_app.logger.debug(f'Recebido JSON em /form/formulario: {dados}')
        if not dados:
            return jsonify({'erro': 'Dados não fornecidos'}), 400
        
        erros = []
        

        nome = dados.get('nome')
        sobrenome = dados.get('sobrenome')
        idade = dados.get('idade')
        genero = dados.get('genero')
        refeicoes_dia = dados.get('refeicoes_dia')
        consome_frutas = dados.get('consome_frutas')        
        consome_agua_litros = dados.get('consome_agua_litros')
        horario_jantar = dados.get('horario_jantar')
        
        validar_nome(erros, nome)
        validar_sobrenome(erros, sobrenome)
        validar_idade(erros, idade)
        validar_genero(erros, genero)
        validar_refeicoes_dia(erros, refeicoes_dia)
        validar_consumo_frutas(erros, consome_frutas)
        validar_consumo_agua(erros, consome_agua_litros)
        validar_horario(erros, horario_jantar)

        if erros:
            return jsonify({'erros': erros}), 400
        
        habito = HabitoAlimentar(
            nome=nome,
            sobrenome=sobrenome,
            idade=idade,
            genero=genero,
            refeicoes_dia=refeicoes_dia,
            consome_frutas=consome_frutas,
            consome_agua_litros=consome_agua_litros,
            horario_jantar=horario_jantar
        )

        db.session.add(habito)
        db.session.commit()

        return jsonify({
            'mensagem': 'Dados enviados com sucesso',
            'id': habito.id
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': 'Erro do servidor', 'detalhes': str(e)}), 500