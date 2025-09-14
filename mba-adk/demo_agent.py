#!/usr/bin/env python3
"""
Demo do Hello World Agent - sem necessidade de API key para verificação estrutural.
"""

import os
import sys

# Simula a existência da API key para teste estrutural
os.environ['GOOGLE_API_KEY'] = 'demo_key_for_structure_test'
os.environ['GOOGLE_GENAI_USE_VERTEXAI'] = 'FALSE'

print("🎯 Demo Hello World Agent - Verificação Estrutural")
print("=" * 50)

try:
    from hello_world_agent.agent import root_agent
    print("✅ Agente importado com sucesso!")
    print(f"📝 Nome: {root_agent.name}")
    print(f"🤖 Modelo: {root_agent.model}")
    print(f"📄 Descrição:")
    print(f"   {root_agent.description.strip()}")
    
    print(f"\n🔧 Ferramentas disponíveis ({len(root_agent.tools)}):")
    
    for i, tool in enumerate(root_agent.tools, 1):
        func = tool.func
        print(f"   {i}. {func.__name__}")
        print(f"      📋 {func.__doc__.split('.')[0] if func.__doc__ else 'Sem descrição'}")
    
    # Testa uma ferramenta simples sem fazer chamada ao LLM
    print(f"\n🧪 Teste das ferramentas (offline):")
    
    from hello_world_agent.tools import (
        say_hello, roll_dice, get_random_fact,
        calculate_simple_math, get_motivational_quote
    )
    
    # Testa say_hello
    result = say_hello("ADK Developer")
    print(f"   ✅ say_hello: {result}")
    
    # Testa roll_dice
    result = roll_dice(6)
    print(f"   ✅ roll_dice: {result['message']}")
    
    # Testa calculate_simple_math
    result = calculate_simple_math("+", 5, 3)
    print(f"   ✅ calculate_simple_math: {result['message']}")
    
    # Testa get_random_fact
    result = get_random_fact()
    print(f"   ✅ get_random_fact: {result}")
    
    # Testa get_motivational_quote
    result = get_motivational_quote()
    print(f"   ✅ get_motivational_quote: {result}")
    
    print(f"\n🎯 Próximos passos:")
    print("1. Configure sua GOOGLE_API_KEY no arquivo .env")
    print("2. Execute: adk web")
    print("3. Acesse a interface web e teste o agente")
    print("4. Ou execute: adk run hello_world_agent")
    
    print(f"\n🏆 Projeto Hello World Agent criado com sucesso!")
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    print("💡 Verifique se todas as dependências estão instaladas")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erro inesperado: {e}")
    sys.exit(1)