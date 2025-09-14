#!/usr/bin/env python3
"""
Script para testar o Hello World Agent localmente.
"""

import os
import sys

# Verifica se a API key está configurada
if not os.getenv('GOOGLE_API_KEY'):
    print("❌ GOOGLE_API_KEY não encontrada!")
    print("\n📋 Para configurar:")
    print("1. Obtenha sua API key em: https://aistudio.google.com/app/apikey")
    print("2. Copie .env.example para .env")
    print("3. Substitua 'your_google_api_key_here' pela sua API key real")
    print("4. Execute: source .venv/bin/activate && export GOOGLE_API_KEY=sua_chave_aqui")
    sys.exit(1)

print("✅ Configuração encontrada!")
print("🚀 Iniciando teste do Hello World Agent...")

try:
    from hello_world_agent.agent import root_agent
    print("✅ Agente importado com sucesso!")
    print(f"📝 Nome: {root_agent.name}")
    print(f"📝 Modelo: {root_agent.model}")
    print(f"🔧 Ferramentas disponíveis: {len(root_agent.tools)}")
    
    for i, tool in enumerate(root_agent.tools, 1):
        print(f"   {i}. {tool.func.__name__}")
    
    print("\n🎯 Para testar o agente:")
    print("   adk web")
    print("   ou")
    print("   adk run hello_world_agent")
    
except Exception as e:
    print(f"❌ Erro ao importar agente: {e}")
    sys.exit(1)