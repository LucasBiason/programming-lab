#!/bin/bash

# Script para iniciar a aplicação React Router
# Resolve o problema de ENOSPC (file watchers limit)

echo "🚀 Iniciando aplicação React Router..."
echo "📍 Porta: 8089"
echo ""

# Verificar se estamos no diretório correto
if [ ! -f "package.json" ]; then
    echo "❌ Erro: Execute este script no diretório da aplicação (onde está o package.json)"
    exit 1
fi

# Função para aumentar o limite de file watchers
increase_file_watchers() {
    echo "🔧 Aumentando limite de file watchers..."
    
    # Verificar se é necessário executar com sudo
    if [ "$EUID" -eq 0 ]; then
        echo "📝 Executando como root..."
        echo "fs.inotify.max_user_watches=524288" >> /etc/sysctl.conf
        sysctl -p
    else
        echo "⚠️  Para resolver permanentemente o problema de file watchers, execute:"
        echo "   sudo bash -c 'echo \"fs.inotify.max_user_watches=524288\" >> /etc/sysctl.conf && sysctl -p'"
        echo ""
        echo "🔄 Tentando aumentar temporariamente..."
        echo 524288 | sudo tee /proc/sys/fs/inotify/max_user_watches > /dev/null 2>&1
    fi
    
    echo "✅ Limite de file watchers atualizado"
}

# Função para verificar dependências
check_dependencies() {
    echo "📦 Verificando dependências..."
    
    if [ ! -d "node_modules" ]; then
        echo "📥 Instalando dependências..."
        npm install
        if [ $? -ne 0 ]; then
            echo "❌ Erro ao instalar dependências"
            exit 1
        fi
        echo "✅ Dependências instaladas"
    else
        echo "✅ Dependências já instaladas"
    fi
}

# Função para iniciar a aplicação
start_application() {
    echo "🎯 Iniciando aplicação na porta 8089..."
    
    # Modificar temporariamente o script para usar a porta 8089
    if ! grep -q "dev.*--port 8089" package.json; then
        echo "🔧 Configurando porta 8089..."
        # Backup do package.json original
        cp package.json package.json.backup
        
        # Modificar o script dev para usar porta 8089
        sed -i 's/"dev": "react-router dev"/"dev": "react-router dev --port 8089"/' package.json
    fi
    
    echo "🌐 Aplicação será iniciada em: http://localhost:8089"
    echo "🔄 Para parar: Ctrl+C"
    echo ""
    
    # Iniciar a aplicação
    npm run dev
}

# Função para limpeza
cleanup() {
    echo ""
    echo "🧹 Restaurando package.json original..."
    if [ -f "package.json.backup" ]; then
        mv package.json.backup package.json
        echo "✅ package.json restaurado"
    fi
    echo "👋 Aplicação finalizada"
}

# Capturar Ctrl+C para limpeza
trap cleanup SIGINT

# Executar funções
echo "🔍 Verificando sistema..."
increase_file_watchers
echo ""

check_dependencies
echo ""

start_application

# Se chegou aqui, houve algum erro
echo "❌ Erro ao iniciar a aplicação"
exit 1

