# 1. Comece com uma imagem base que já tem Python instalado.
# Usamos a 'slim' por ser mais leve.
FROM python:3.9-slim

# 2. Define o diretório de trabalho padrão dentro do contêiner.
# Todos os comandos a seguir serão executados a partir de /app.
WORKDIR /app

# 3. Copia os arquivos da sua pasta local para dentro do contêiner.
# O primeiro "." é a sua pasta (ex: servico_soma).
# O "/app" é o diretório de trabalho que definimos acima.
COPY . /app

# 4. Instala as bibliotecas Python listadas no requirements.txt.
# Este comando é executado uma vez durante a construção da imagem.
RUN pip install --no-cache-dir -r requirements.txt

# 5. Informa ao Docker que o contêiner usará a porta 5001.
# É uma boa prática para documentar a porta usada.
EXPOSE 5002

# 6. O comando final que será executado quando o contêiner iniciar.
# É o mesmo que você digitaria no terminal: python app.py
CMD ["python", "app.py"]