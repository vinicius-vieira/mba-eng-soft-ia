"""
Ferramentas customizadas para o Hello World Agent.
"""

import random
from typing import Any

from google.adk.tools import FunctionTool


def say_hello(name: str = "mundo") -> str:
    """
    Cumprimenta uma pessoa de forma amigável.
    
    Args:
        name: O nome da pessoa para cumprimentar (padrão: "mundo")
    
    Returns:
        Uma saudação personalizada
    """
    greetings = [
        f"Olá, {name}! Como você está hoje?",
        f"Oi {name}! É um prazer falar com você!",
        f"Saudações, {name}! Espero que esteja tendo um ótimo dia!",
        f"E aí, {name}! Como posso te ajudar hoje?",
        f"Bem-vindo(a), {name}! Vamos conversar!"
    ]
    return random.choice(greetings)


def roll_dice(sides: int = 6) -> dict[str, Any]:
    """
    Rola um dado com número especificado de lados.
    
    Args:
        sides: Número de lados do dado (padrão: 6)
    
    Returns:
        Dicionário com o resultado do dado e informações adicionais
    """
    if sides < 2:
        return {"error": "O dado deve ter pelo menos 2 lados!"}
    
    result = random.randint(1, sides)
    
    return {
        "result": result,
        "sides": sides,
        "message": f"🎲 Você rolou um dado de {sides} lados e tirou: {result}!"
    }


def get_random_fact() -> str:
    """
    Retorna um fato curioso aleatório.
    
    Returns:
        Um fato interessante
    """
    facts = [
        "🐙 Os polvos têm três corações e sangue azul!",
        "🍯 O mel nunca estraga - potes de mel com mais de 3000 anos ainda são comestíveis!",
        "🦆 Os patos têm um quack que não produz eco, mas ninguém sabe exatamente por quê!",
        "🌙 A Lua está se afastando da Terra aproximadamente 3,8 cm por ano!",
        "🐧 Os pinguins podem pular até 2,7 metros de altura!",
        "🧠 O cérebro humano usa apenas cerca de 20% da energia total do corpo!",
        "🦋 As borboletas provam com os pés!",
        "🐨 Os coalas dormem de 18 a 22 horas por dia!",
        "⚡ Um raio é cinco vezes mais quente que a superfície do Sol!",
        "🍌 As bananas são tecnicamente frutas vermelhas!"
    ]
    return random.choice(facts)


def calculate_simple_math(operation: str, a: float, b: float) -> dict[str, Any]:
    """
    Realiza operações matemáticas simples.
    
    Args:
        operation: Operação a ser realizada (+, -, *, /)
        a: Primeiro número
        b: Segundo número
    
    Returns:
        Resultado da operação matemática
    """
    try:
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            if b == 0:
                return {"error": "Não é possível dividir por zero!"}
            result = a / b
        else:
            return {"error": f"Operação '{operation}' não suportada. Use: +, -, *, /"}
        
        return {
            "result": result,
            "operation": f"{a} {operation} {b} = {result}",
            "message": f"📊 Calculei: {a} {operation} {b} = {result}"
        }
    
    except Exception as e:
        return {"error": f"Erro no cálculo: {str(e)}"}


def get_motivational_quote() -> str:
    """
    Retorna uma frase motivacional aleatória.
    
    Returns:
        Uma frase inspiradora
    """
    quotes = [
        "💪 'O sucesso é a soma de pequenos esforços repetidos dia após dia.' - Robert Collier",
        "🌟 'Acredite em si mesmo e chegará um dia em que os outros não terão outra escolha senão acreditar com você.' - Cynthia Kersey",
        "🚀 'O futuro pertence àqueles que acreditam na beleza de seus sonhos.' - Eleanor Roosevelt",
        "🎯 'Não é sobre ser perfeito, é sobre ser melhor do que você era ontem.'",
        "🌱 'Todo expert foi um iniciante. Todo profissional foi um amador. Todo ícone foi um desconhecido.'",
        "⭐ 'A única maneira de fazer um excelente trabalho é amar o que você faz.' - Steve Jobs",
        "🔥 'Seja você mesmo; todos os outros já existem.' - Oscar Wilde",
        "🏆 'O caminho para o sucesso e o caminho para o fracasso são quase exatamente os mesmos.' - Colin R. Davis"
    ]
    return random.choice(quotes)


# Criando instâncias das ferramentas usando FunctionTool
say_hello_tool = FunctionTool(say_hello)
roll_dice_tool = FunctionTool(roll_dice)
get_random_fact_tool = FunctionTool(get_random_fact)
calculate_simple_math_tool = FunctionTool(calculate_simple_math)
get_motivational_quote_tool = FunctionTool(get_motivational_quote)

# Lista de todas as ferramentas para uso no agente
ALL_TOOLS = [
    say_hello_tool,
    roll_dice_tool,
    get_random_fact_tool,
    calculate_simple_math_tool,
    get_motivational_quote_tool
]