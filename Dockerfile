# Use uma imagem base do Python
FROM python:3.13

# Configura o diretório de trabalho
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Dá permissão ao entrypoint
RUN chmod +x entrypoint.sh

# Roda migrations antes de iniciar
ENTRYPOINT ["./entrypoint.sh"]

# Comando para iniciar o servidor Django
CMD ["uvicorn", "core.asgi:application", "--host", "0.0.0.0", "--port", "8009"]