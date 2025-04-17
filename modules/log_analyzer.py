from collections import Counter
from flask import Flask, render_template
import sqlite3
import subprocess
from datetime import datetime

def analyze():
    """Analisa logs de autenticação falha via journalctl e armazena no banco de dados"""
    try:
        print("\n[+] Analisando logs de autenticação...")
        
        # Usa journalctl para logs modernos, fallback para auth.log
        logs = get_auth_logs()
        
        failed_logs = [line for line in logs if 'Failed password' in line]
        ips = []
        
        for line in failed_logs:
            try:
                ip = line.split('from ')[1].split(' ')[0]
                ips.append(ip)
            except IndexError:
                continue
        
        top_attackers = Counter(ips).most_common(10)
        
        print("\n🔴 Lista de IPS:")
        for ip, count in top_attackers:
            print(f"  → {ip}: {count} tentativas")
            log_to_db(ip, count)
            
        return top_attackers
            
    except Exception as e:
        print(f"[!] Erro na análise: {str(e)}")
        return []

def get_auth_logs():
    """Obtém logs de autenticação do systemd ou arquivo tradicional"""
    try:
        # Tenta primeiro com journalctl (sistemas modernos)
        logs = subprocess.check_output(
            ['journalctl', '-u', 'ssh', '--no-pager', '-n', '500', '--since', 'today'],
            universal_newlines=True,
            stderr=subprocess.DEVNULL
        ).split('\n')
        return logs
    except:
        # Fallback para auth.log (sistemas legados)
        try:
            with open('/var/log/auth.log', 'r') as f:
                return f.readlines()
        except PermissionError:
            print("[!] Execute com sudo ou ajuste permissões")
            return []

def log_to_db(ip, count):
    """Armazena ataques no banco de dados SQLite"""
    conn = None
    try:
        conn = sqlite3.connect('attackers.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS attackers
                    (ip TEXT PRIMARY KEY, 
                     count INTEGER,
                     last_attempt TIMESTAMP,
                     first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        
        # Atualiza ou insere o registro
        c.execute('''INSERT OR REPLACE INTO attackers 
                    (ip, count, last_attempt) 
                    VALUES (?, ?, CURRENT_TIMESTAMP)''', 
                    (ip, count))
        conn.commit()
    except sqlite3.Error as e:
        print(f"[!] Erro no banco de dados: {str(e)}")
    finally:
        if conn:
            conn.close()

def generate_html_report():
    """Gera relatório HTML com os dados de ataques"""
    try:
        app = Flask(__name__)
        with app.app_context():
            conn = sqlite3.connect('attackers.db')
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
            # Obtém os 20 IPs mais ativos
            attackers = c.execute('''
                SELECT ip, count, last_attempt 
                FROM attackers 
                ORDER BY count DESC 
                LIMIT 20
            ''').fetchall()
            
            # Formata dados para o template
            report_data = [{
                'ip': row['ip'],
                'count': row['count'],
                'last_attempt': row['last_attempt'],
                'threat_level': 'high' if row['count'] > 10 else 'medium' if row['count'] > 5 else 'low'
            } for row in attackers]
            
            return render_template('report.html', attackers=report_data)
            
    except Exception as e:
        print(f"[!] Erro ao gerar relatório: {str(e)}")
        return "<h1>Erro ao gerar relatório</h1>"
