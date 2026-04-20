from pathlib import Path
import getpass
import shutil


# directory se torna um objeto que representa uma pasta do sistema
pasta = Path.home() / "Downloads"
# com isso alguns métodos podem ser desenvolvidos

#Categorias de arquivos
categorias = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audios": [".mp3", ".wav", ".flac"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Programas": [".exe", ".msi"]
}

# Percorre tudo que há na pasta
for arquivo in pasta.iterdir(): #iterdir() retorna cada arquivo encontrado

    if arquivo.is_file(): #checa se o arquivo atual é um arquivo (diferente de pasta)
        extensao = arquivo.suffix.lower() #pega a extensão do erquivo em minúsculo
        movido = False

        for categoria, extensoes in categorias.items(): #para categoria[extensões] em todas as categorias

            if extensao in extensoes: #verifica se a extensão atual está na categoria

                destino = pasta / categoria #cria o caminho para a parta de destino
                destino.mkdir(exist_ok=True) #cria a pasta de caminho caso não exista

                novo_caminho = destino / arquivo.name
                shutil.move(str(arquivo), str(novo_caminho))
                movido = True

                break

        if not movido:
            destino = pasta / "Outros"
            destino.mkdir(exist_ok=True)

            novo_caminho = destino / arquivo.name
            shutil.move(str(arquivo), str(novo_caminho))