# TeleShell Executor

Este é um bot do Telegram que executa comandos PowerShell enviados pelos usuários e fornece uma interface simples para gerenciar sessões em segundo plano.

## Requisitos

- Python 3.x
- Bibliotecas Python: `python-telegram-bot`

## Configuração

1. Clone este repositório:

    ```
    git clone https://github.com/seu-usuario/teleshell-executor.git
    ```

2. Instale as dependências:

    ```
    pip install python-telegram-bot
    ```

3. Configure as seguintes variáveis no arquivo `config.py`:

    - `TOKEN`: Token do bot do Telegram.
    - `GRUPO_CHAT_ID`: ID do chat/grupo onde o bot irá operar.

## Uso

Execute o arquivo `main.py` para iniciar o bot:



O bot irá iniciar e aguardar por comandos enviados pelos usuários. Além disso, ele oferece as seguintes funcionalidades:

- `/send_ps`: Enviar um comando PowerShell para execução.
- `/list`: Listar sessões em execução.
- `/background`: Deixar um comando em segundo plano para execução contínua.
- `/menu`: Exibir o menu de opções.

## Notas

- Certifique-se de que o bot tem permissão para ler e enviar mensagens no chat/grupo especificado.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
