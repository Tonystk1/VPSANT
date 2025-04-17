# 🔒 VPS Security Monitor

![Python Version](https://img.shields.io/badge/python-3.8+-blue) 
![License](https://img.shields.io/badge/license-MIT-green)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Tonystk1/VPSANT)
![Open Issues](https://img.shields.io/github/issues/Tonystk1/VPSANT)

Sistema avançado para monitoramento e proteção de servidores Linux, com detecção de intrusões em tempo real.

## ✨ Funcionalidades Principais
| Módulo         | Descrição                                                                 |
|----------------|---------------------------------------------------------------------------|
| **Log Analyzer** | Monitoramento contínuo de tentativas de acesso suspeitas via SSH          |
| **Threat Scanner** | Varredura de portas e vulnerabilidades com Nmap integrado                |
| **Auto-Hardening** | Configura automaticamente 10+ regras de segurança no servidor            |
| **Alert System**  | Notificações em tempo real via Telegram/Email para atividades suspeitas  |

## 🛠️ Tecnologias Utilizadas
- **Python 3.8+** (Análise de logs e automação)
- **Nmap** (Scanner de vulnerabilidades)
- **SQLite** (Armazenamento de dados de ataques)
- **Flask** (Dashboard de monitoramento)
- **Systemd** (Integração com logs modernos)

## 🚀 Instalação Rápida
```bash
# Clone o repositório
git clone https://github.com/Tonystk1/VPSANT.git && cd VPSANT

# Configure ambiente virtual (recomendado)
python3 -m venv venv
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Execute (modo interativo)
python3 main.py



