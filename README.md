# Downloads Simple Organizer

Um organizador simples de arquivos para a pasta Downloads, feito em Python.

O script separa automaticamente os arquivos em categorias com base na extensão, criando pastas como:

- Imagens
- Documentos
- Vídeos
- Áudios
- Compactados
- Programas
- Outros

## Funcionalidades

- Organiza automaticamente a pasta Downloads do usuário atual
- Cria pastas por categoria
- Move arquivos para suas respectivas categorias
- Cria uma pasta `Outros` para extensões não reconhecidas
- Não precisa alterar manualmente o nome do usuário
- Usa apenas bibliotecas nativas do Python

## Categorias suportadas

### Imagens
- `.jpg`
- `.jpeg`
- `.png`
- `.gif`
- `.webp`

### Documentos
- `.pdf`
- `.docx`
- `.doc`
- `.txt`
- `.xlsx`
- `.pptx`

### Vídeos
- `.mp4`
- `.mkv`
- `.avi`
- `.mov`

### Áudios
- `.mp3`
- `.wav`
- `.flac`

### Compactados
- `.zip`
- `.rar`
- `.7z`

### Programas
- `.exe`
- `.msi`

## Como executar

Clone o repositório:

```bash
git clone https://github.com/joaovdiasferreira/downloads-simple-organizer.git
```

Entre na pasta do projeto:

```bash
cd downloads-simple-organizer
```

Execute o script:

```bash
python organizer.py
```

## Como funciona

O script utiliza:

- `pathlib` para manipular caminhos e pastas
- `shutil` para mover arquivos

A pasta Downloads é identificada automaticamente usando:

```python
from pathlib import Path

pasta = Path.home() / "Downloads"
```

## Gerando executável

Se quiser transformar o projeto em um arquivo `.exe`:

Instale o PyInstaller:

```bash
pip install pyinstaller
```

Depois execute:

```bash
pyinstaller --onefile organizer.py
```

O executável será gerado dentro da pasta:

```text
dist/
```

## Possíveis melhorias futuras

- Evitar sobrescrever arquivos repetidos
- Selecionar outras pastas além de Downloads
- Interface gráfica
- Barra de progresso
- Relatório final
- Arquivo de configuração para personalizar extensões
- Modo simulação antes de mover os arquivos

## Licença

Este projeto é livre para estudo, modificação e uso pessoal.

