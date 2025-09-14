# Projeto Hello World Agent - Google ADK

Este é um projeto de exemplo que demonstra como criar um agente básico usando o Google Agent Development Kit (ADK).

## Configuração

1. **Instalar dependências:**
   ```bash
   pip install google-adk
   ```

2. **Configurar API Key:**
   - Copie o arquivo `.env.example` para `.env`
   - Obtenha sua API key em https://aistudio.google.com/app/apikey
   - Adicione sua API key no arquivo `.env`

3. **Executar o agente:**
   ```bash
   # Modo interativo
   adk run hello_world_agent

   # Servidor web (UI)
   adk web
   ```

## Estrutura do Projeto

```
hello_world_agent/
├── __init__.py          # Configuração do pacote Python
├── agent.py            # Implementação do agente
└── tools.py           # Ferramentas customizadas do agente
```

## Funcionalidades

O agente Hello World inclui:
- Saudações personalizadas
- Resposta a perguntas básicas
- Exemplo de uso de ferramentas customizadas
- Integração com o modelo Gemini

## Recursos Adicionais

- [Documentação do ADK](https://google.github.io/adk-docs/)
- [Exemplos do ADK](https://github.com/google/adk-samples)
- [API Reference](https://google.github.io/adk-docs/api-reference/)