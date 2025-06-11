import os
import markdown
from flask import Blueprint, render_template_string

guide_bp = Blueprint('guide', __name__)

# Conteúdo do guia embutido diretamente no código
GUIDE_CONTENT = """# Guia de Identificação Visual para GeoGuessr

## 1. Carros e Placas

Os carros do Google Street View e as placas de veículos são uma das pistas mais confiáveis para identificar países. Cada país possui características específicas:

### Carros do Google Street View:
- **Geração da câmera**: Diferentes países usam diferentes gerações de câmeras do Google
- **Posição da câmera**: A altura e posição da câmera podem variar
- **Antenas e equipamentos**: Alguns países têm antenas ou equipamentos específicos visíveis
- **Reflexos e sombras**: O carro pode ser parcialmente visível através de reflexos

### Placas de Veículos:
- **Formato**: Retangular, quadrado, ou formatos únicos
- **Cores**: Combinações específicas de cores de fundo e texto
- **Posição**: Dianteira, traseira, ou ambas
- **Padrões**: Letras, números, símbolos especiais

## 2. Paisagens

A paisagem oferece pistas valiosas sobre a localização geográfica:

### Vegetação:
- **Biomas**: Floresta tropical, savana, deserto, tundra, floresta temperada
- **Tipos de árvores**: Palmeiras (regiões tropicais), coníferas (regiões frias), eucaliptos (Austrália)
- **Densidade**: Vegetação densa vs. esparsa

### Solo e Terreno:
- **Cor do solo**: Vermelho (África, Austrália), preto (vulcânico), amarelo (arenoso)
- **Topografia**: Montanhas, planícies, colinas, vales
- **Formações rochosas**: Características específicas de certas regiões

### Clima:
- **Condições do céu**: Ensolarado, nublado, chuvoso
- **Estação do ano**: Folhagem de outono, neve, vegetação seca

## 3. Placas de Trânsito e Sinais

As placas de trânsito são altamente específicas por país:

### Formato e Design:
- **Forma**: Triangular, circular, retangular, octogonal
- **Cores**: Combinações de vermelho, azul, amarelo, branco, preto
- **Bordas**: Espessura e cor das bordas

### Idioma e Texto:
- **Alfabeto**: Latino, cirílico, árabe, chinês, etc.
- **Idiomas**: Identificação através de palavras específicas
- **Fontes**: Estilos de letra característicos

### Símbolos e Setas:
- **Direção**: Formato das setas
- **Símbolos**: Ícones específicos para diferentes tipos de aviso

## 4. Escritas e Idiomas

O idioma é uma das pistas mais diretas para identificar um país:

### Alfabetos:
- **Latino**: Europa Ocidental, Américas, partes da África
- **Cirílico**: Rússia, Bulgária, Sérvia, etc.
- **Árabe**: Oriente Médio, Norte da África
- **Chinês**: China, Taiwan
- **Japonês**: Hiragana, Katakana, Kanji
- **Coreano**: Hangul

### Padrões Linguísticos:
- **Palavras comuns**: "Rua", "Avenida", "Centro" em diferentes idiomas
- **Terminações**: Sufixos característicos de certas línguas
- **Diacríticos**: Acentos e marcas especiais

## 5. Bollards

Bollards são postes de proteção na beira das estradas, muito específicos por país:

### Características:
- **Cores**: Branco, amarelo, vermelho, combinações
- **Formato**: Cilíndrico, retangular, com formatos únicos
- **Faixas reflexivas**: Padrões de faixas horizontais ou diagonais
- **Material**: Concreto, metal, plástico

### Exemplos por Região:
- **Europa**: Bollards brancos com faixas vermelhas são comuns
- **Ásia**: Designs mais variados e coloridos
- **Américas**: Estilos mais simples, frequentemente amarelos

## 6. Chevrons

Chevrons são marcas em placas ou muros que indicam curvas:

### Padrões Visuais:
- **Cores**: Amarelo e preto, branco e vermelho, outras combinações
- **Formato das setas**: Pontiagudas, arredondadas, estilizadas
- **Densidade**: Número de chevrons por placa
- **Posicionamento**: Em guard-rails, muros, ou placas independentes

## 7. Linhas de Estrada

As marcações rodoviárias variam significativamente entre países:

### Características:
- **Cor**: Branco, amarelo, ocasionalmente outras cores
- **Padrão**: Contínuas, tracejadas, duplas
- **Espaçamento**: Distância entre as linhas tracejadas
- **Largura**: Espessura das linhas

### Exemplos:
- **EUA**: Linhas amarelas no centro, brancas nas bordas
- **Reino Unido**: Linhas brancas com padrões específicos
- **Brasil**: Linhas amarelas contínuas e tracejadas

## 8. Arquitetura e Construções

O estilo arquitetônico é uma forte indicação geográfica:

### Tipos de Telhado:
- **Material**: Telha de cerâmica, metal, palha, concreto
- **Formato**: Inclinado, plano, em formato específico
- **Cor**: Vermelho (Mediterrâneo), cinza (Norte da Europa)

### Materiais de Construção:
- **Tijolo**: Vermelho (Norte da Europa), adobe (América Latina)
- **Madeira**: Comum em países nórdicos e América do Norte
- **Concreto**: Estilo brutalista ou moderno

### Estilo Arquitetônico:
- **Colonial**: Influências históricas específicas
- **Moderno**: Designs contemporâneos
- **Tradicional**: Estilos locais únicos

## 9. Cabos e Postes

A infraestrutura elétrica varia entre países:

### Tipos de Postes:
- **Material**: Madeira, concreto, metal
- **Formato**: Cilíndrico, retangular, com formatos únicos
- **Altura**: Baixos vs. altos

### Cabos:
- **Visibilidade**: Aéreos vs. subterrâneos
- **Densidade**: Muitos cabos emaranhados vs. organizados
- **Transformadores**: Presença e tipo de equipamentos

## 10. Código de Direção

O lado da estrada em que se dirige é uma pista fundamental:

### Mão Direita:
- **Países**: Maioria dos países do mundo
- **Características**: Volante à esquerda, tráfego pela direita

### Mão Inglesa:
- **Países**: Reino Unido, Irlanda, Austrália, Nova Zelândia, Japão, Índia, África do Sul, etc.
- **Características**: Volante à direita, tráfego pela esquerda

## 11. Cultura Visual Local

Elementos culturais específicos podem indicar a localização:

### Outdoors e Publicidade:
- **Idioma**: Textos em idiomas locais
- **Marcas**: Empresas específicas de certas regiões
- **Estilo**: Design característico de diferentes culturas

### Bandeiras:
- **Nacionais**: Bandeiras do país
- **Regionais**: Bandeiras de estados ou províncias
- **Organizações**: Bandeiras de instituições locais

### Vestimentas e Pessoas:
- **Roupas tradicionais**: Vestimentas específicas de certas culturas
- **Estilo**: Moda local característica

### Vegetação Urbana:
- **Plantas ornamentais**: Espécies específicas de certas regiões
- **Paisagismo**: Estilo de jardinagem local

## 12. Sistema de Análise para Identificação de Locais

### Checklist de Análise Rápida:

1. **Código de Direção**: Mão direita ou inglesa?
2. **Idioma/Alfabeto**: Que tipo de escrita é visível?
3. **Carros e Placas**: Que tipo de veículo do Google? Formato das placas?
4. **Paisagem**: Que tipo de vegetação e clima?
5. **Arquitetura**: Que estilo de construções?
6. **Placas de Trânsito**: Formato, cores e idioma das placas?
7. **Bollards**: Cores e formato dos postes de proteção?
8. **Linhas de Estrada**: Cor e padrão das marcações?
9. **Infraestrutura**: Tipo de postes e cabos?
10. **Cultura Local**: Bandeiras, outdoors, vestimentas?

### Modelo de Justificativa Detalhada:

**Justificativa Detalhada:**

- **Carros e Placas:** [Descreva o que foi observado: ex: "Placas traseiras amarelas e dianteiras brancas, indicando padrão europeu. Carro do Google com rack de teto preto e antena visível, comum na [País/Região]."]
- **Paisagens:** [Descreva a vegetação, solo, formações geográficas e clima: ex: "Vegetação de savana com gramíneas altas e árvores esparsas, sugerindo clima tropical seco, típico da [País/Região]. Solo avermelhado, indicativo de alta concentração de óxido de ferro."]
- **Placas de Trânsito e Sinais:** [Descreva o formato, cor, idioma, fontes, bordas e setas: ex: "Placas de trânsito triangulares com borda vermelha e fundo branco, e fontes que correspondem ao padrão da [País/Região]. Idioma [Idioma] claramente visível."]
- **Escritas e Idiomas:** [Descreva o alfabeto e o idioma: ex: "Textos em alfabeto cirílico, com palavras que se assemelham ao [Idioma], comum na [País/Região]."]
- **Bollards:** [Descreva as cores e formas: ex: "Bollards brancos com faixas vermelhas horizontais, um design característico da [País/Região]."]
- **Chevrons:** [Descreva os padrões visuais: ex: "Chevrons amarelos e pretos com setas pontiagudas, padrão encontrado na [País/Região]."]
- **Linhas de Estrada:** [Descreva a cor, formato e estilo de pintura: ex: "Linhas de estrada brancas contínuas e tracejadas, com um padrão de espaçamento longo, típico da [País/Região]."]
- **Arquitetura e Construções:** [Descreva o tipo de telhado, material e estilo de casa: ex: "Casas com telhados íngremes de telha de cerâmica vermelha e paredes de estuque, estilo arquitetônico comum na [País/Região]."]
- **Cabos e Postes:** [Descreva o formato, visibilidade e localização: ex: "Postes de concreto com muitos cabos aéreos emaranhados e transformadores visíveis, padrão de infraestrutura comum na [País/Região]."]
- **Código de Direção:** [Indique se é mão inglesa ou direita e justifique: ex: "Tráfego de mão inglesa, com o volante do carro do Google no lado direito, confirmando a direção da [País/Região]."]
- **Cultura Visual Local:** [Descreva outdoors, grafites, bandeiras, roupas, vegetação urbana: ex: "Outdoors com anúncios em [Idioma] e bandeiras de [País/Região] visíveis. Vegetação urbana com palmeiras, indicando clima subtropical."]

**Nível de Confiança:** [Alto/Médio/Baixo] - Justifique o nível de confiança com base na quantidade e clareza das pistas.

### Priorização de Precisão e Rapidez

Para otimizar a precisão e a rapidez na identificação de locais, siga estas diretrizes:

1. **Priorize Pistas de Alta Confiança:** Concentre-se primeiro nas pistas que oferecem a maior certeza de identificação. O código de direção, o idioma e o alfabeto são geralmente as pistas mais rápidas e confiáveis para restringir as opções de país. Em seguida, as placas de veículos e de trânsito costumam ser muito distintivas.

2. **Busca por Pistas Múltiplas e Consistentes:** Não se baseie em apenas uma pista. Procure por múltiplas evidências que se complementem e apontem para a mesma região. Quanto mais pistas consistentes você encontrar, maior será a precisão da sua dedução.

3. **Eliminação Rápida de Opções:** Utilize as pistas de alta confiança para eliminar rapidamente países ou regiões que não se encaixam. Por exemplo, se o tráfego é de mão direita, você pode imediatamente descartar todos os países de mão inglesa.

4. **Atenção aos Detalhes Sutis:** Após a identificação das pistas mais óbvias, preste atenção aos detalhes mais sutis, como o estilo de postes, a cor do solo, o tipo de vegetação urbana e a arquitetura local. Esses detalhes podem ajudar a diferenciar entre países com características semelhantes.

5. **Gerenciamento do Tempo:** No contexto do jogo GeoGuessr, onde o tempo é um fator, é crucial equilibrar a busca por precisão com a rapidez. Se uma pista clara não surgir rapidamente, passe para a próxima categoria de pistas. Em situações de dúvida, faça uma dedução informada com base nas pistas mais fortes que você conseguiu coletar.

6. **Confiança e Justificativa:** O nível de confiança na sua dedução deve refletir a quantidade e a clareza das pistas encontradas. Uma justificativa detalhada, mesmo que a dedução não seja 100% precisa, demonstra um processo de análise sólido.

Ao seguir este sistema de análise, você estará bem equipado para abordar qualquer imagem do GeoGuessr com uma abordagem estruturada e eficaz, maximizando suas chances de identificar o local com precisão e rapidez.
"""

@guide_bp.route('/guide')
def show_guide():
    try:
        # Converter Markdown para HTML
        html_content = markdown.markdown(GUIDE_CONTENT, extensions=['tables', 'toc'])
        
        # Template HTML com estilo
        template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia de Identificação Visual para GeoGuessr</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }
        .container {
            background-color: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            margin-bottom: 30px;
        }
        h2 {
            color: #34495e;
            margin-top: 40px;
            margin-bottom: 20px;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }
        h3 {
            color: #2c3e50;
            margin-top: 30px;
            margin-bottom: 15px;
        }
        ul, ol {
            margin-bottom: 20px;
        }
        li {
            margin-bottom: 8px;
        }
        strong {
            color: #2c3e50;
        }
        code {
            background-color: #f1f2f6;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background-color: #f1f2f6;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background-color: #3498db;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .toc {
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
        }
        .toc h2 {
            margin-top: 0;
            color: #2c3e50;
            border: none;
            padding: 0;
        }
        .toc ul {
            list-style-type: none;
            padding-left: 0;
        }
        .toc li {
            margin-bottom: 5px;
        }
        .toc a {
            color: #3498db;
            text-decoration: none;
        }
        .toc a:hover {
            text-decoration: underline;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .subtitle {
            color: #7f8c8d;
            font-size: 1.2em;
            margin-top: 10px;
        }
        @media (max-width: 768px) {
            body {
                padding: 10px;
            }
            .container {
                padding: 20px;
            }
            h1 {
                font-size: 1.8em;
            }
            h2 {
                font-size: 1.4em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌍 Guia de Identificação Visual para GeoGuessr</h1>
            <p class="subtitle">Seu guia completo para se tornar um especialista em GeoGuessr</p>
        </div>
        
        <div class="toc">
            <h2>📋 Índice</h2>
            <ul>
                <li><a href="#1-carros-e-placas">1. Carros e Placas</a></li>
                <li><a href="#2-paisagens">2. Paisagens</a></li>
                <li><a href="#3-placas-de-trânsito-e-sinais">3. Placas de Trânsito e Sinais</a></li>
                <li><a href="#4-escritas-e-idiomas">4. Escritas e Idiomas</a></li>
                <li><a href="#5-bollards">5. Bollards</a></li>
                <li><a href="#6-chevrons">6. Chevrons</a></li>
                <li><a href="#7-linhas-de-estrada">7. Linhas de Estrada</a></li>
                <li><a href="#8-arquitetura-e-construções">8. Arquitetura e Construções</a></li>
                <li><a href="#9-cabos-e-postes">9. Cabos e Postes</a></li>
                <li><a href="#10-código-de-direção">10. Código de Direção</a></li>
                <li><a href="#11-cultura-visual-local">11. Cultura Visual Local</a></li>
                <li><a href="#12-sistema-de-análise-para-identificação-de-locais">12. Sistema de Análise</a></li>
            </ul>
        </div>
        
        {{ content|safe }}
    </div>
</body>
</html>
        """
        
        return render_template_string(template, content=html_content)
        
    except Exception as e:
        return f"Erro ao carregar o guia: {str(e)}", 500

@guide_bp.route('/')
def index():
    return """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia GeoGuessr - Página Inicial</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background-color: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            text-align: center;
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 20px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #7f8c8d;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .description {
            color: #34495e;
            margin-bottom: 40px;
            text-align: left;
            line-height: 1.8;
        }
        .cta-button {
            display: inline-block;
            background: linear-gradient(45deg, #3498db, #2980b9);
            color: white;
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 25px;
            font-size: 1.1em;
            font-weight: bold;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            margin: 10px;
        }
        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4);
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }
        .feature {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            border-left: 4px solid #3498db;
        }
        .feature h3 {
            color: #2c3e50;
            margin-bottom: 10px;
        }
        .emoji {
            font-size: 2em;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌍 Guia GeoGuessr</h1>
        <p class="subtitle">Torne-se um especialista em identificação visual de locais</p>
        
        <div class="description">
            <p>Bem-vindo ao guia mais completo para dominar o GeoGuessr! Este guia foi desenvolvido com base em recursos especializados e técnicas de jogadores profissionais para ajudá-lo a identificar locais com máxima precisão.</p>
            
            <p>Aprenda a reconhecer e interpretar elementos visuais como carros, placas, paisagens, arquitetura, sinais de trânsito e muito mais. Com nosso sistema de análise estruturado, você será capaz de deduzir países e regiões rapidamente.</p>
        </div>
        
        <a href="/guide" class="cta-button">📖 Acessar o Guia Completo</a>
        
        <div class="features">
            <div class="feature">
                <div class="emoji">🚗</div>
                <h3>Carros e Placas</h3>
                <p>Identifique países através de placas de veículos e carros do Google Street View</p>
            </div>
            <div class="feature">
                <div class="emoji">🌿</div>
                <h3>Paisagens</h3>
                <p>Reconheça biomas, vegetação e formações geográficas características</p>
            </div>
            <div class="feature">
                <div class="emoji">🚦</div>
                <h3>Sinais de Trânsito</h3>
                <p>Decodifique placas de trânsito, bollards, chevrons e marcações rodoviárias</p>
            </div>
            <div class="feature">
                <div class="emoji">🏗️</div>
                <h3>Arquitetura</h3>
                <p>Analise estilos arquitetônicos, materiais de construção e infraestrutura</p>
            </div>
            <div class="feature">
                <div class="emoji">🔤</div>
                <h3>Idiomas e Alfabetos</h3>
                <p>Identifique países através de textos, alfabetos e padrões linguísticos</p>
            </div>
            <div class="feature">
                <div class="emoji">📋</div>
                <h3>Sistema de Análise</h3>
                <p>Use nosso checklist estruturado para análise rápida e precisa</p>
            </div>
        </div>
    </div>
</body>
</html>
    """

