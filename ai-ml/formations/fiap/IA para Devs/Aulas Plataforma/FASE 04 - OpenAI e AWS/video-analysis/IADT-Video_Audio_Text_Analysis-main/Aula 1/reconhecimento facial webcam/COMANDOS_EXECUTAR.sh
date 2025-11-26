#!/bin/bash

# Script para habilitar webcam temporariamente no Linux
# Execute este arquivo OU copie os comandos abaixo

echo "======================================================"
echo "HABILITANDO WEBCAM TEMPORARIAMENTE"
echo "======================================================"
echo ""
echo "Este script dá permissão temporária para acessar a webcam."
echo "A permissão será revertida ao reiniciar o computador."
echo ""
echo "Para solução permanente:"
echo "  1. sudo usermod -a -G video \$USER"
echo "  2. Fazer logout e login"
echo ""

# Dar permissão aos principais dispositivos de vídeo
sudo chmod 666 /dev/video0
sudo chmod 666 /dev/video2
sudo chmod 666 /dev/video4
sudo chmod 666 /dev/video6

echo ""
echo "✅ Permissões aplicadas!"
echo ""
echo "Agora execute:"
echo "  cd \"$(pwd)\""
echo "  source .venv/bin/activate"
echo "  python3 encontrar_webcam_linux.py"
echo ""




