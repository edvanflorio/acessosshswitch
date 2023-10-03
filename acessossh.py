#inicio são comandos de importação de bibliotecas - esta sendo copiado do chatgpt para aprendizado.

import paramiko
import logging 

#configuraçã de registro de log

logging.basicConfig(filename='acesso_ssh.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#lista de ips dos switches

ips_switchs = [
    #'10.0.5.0',
    #'10.0.23.0',
    #'10.0.24.0',
    #'10.0.34.0',
    #'10.0.50.0'

    #aqui dentro deve ser adicionado os ips que voce deseja
]

# lista de credencias para acessoa so switchs

credenciais = [
    {'username': 'login', 'password': 'senha'},
    {'username': 'login', 'password': 'login'}
]

# Função para executar comandos SSH em um switch

def executar_comando_ssh(ip, username='username', password='password'):
    try:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #conexão SSH

        client.connect(ip, username=username, password=password)

        #comando ssh

        comandos = ['comandos a serem usados']
        for comando in comandos:
            stdin, stdout, stderr = client.exec_command(comando)
            stdin.close()

            # Resgistra a saida no log

            logging.info(f'Executando comando em {ip}: {comando}')
            for line in stdout.readlines():
                print(line.replace('\n',''))
                # Registra a saida do log
                logging.info(line.strip())

            # Fechamento da conexão ssh
            client.close()
    except Exception as e:
        # casos de erro, registrar log.

        logging.error(f'Erro ao conectar-se ou executar comandos ssh em {ip}: {str(e)}')
        print(f'Erro ao conectar-se ou executar comandos ssh em {ip}: {str(e)}')

for ip in ips_switchs:
    for credencial in credenciais:
        username = credencial['username']
        password = credencial['password']
        executar_comando_ssh(ip, username, password)