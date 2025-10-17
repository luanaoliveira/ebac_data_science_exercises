import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

print('Coleta de dados: ')
df = pd.read_csv('./ecommerce_preparados.csv')
print(df.head().to_string())

print('Verificação inicial: ')
df = df.drop(['Unnamed: 0'], axis=1)
print(df.head().to_string())
print(f"Quantidade de linhas e colunas: {df.shape}")
print(df.info())
print(df.dtypes)
print(df.describe().to_string())
print(df.nunique())
print(df['Gênero'].unique())

print('Identificar dados faltantes:')
print(df.isnull().sum())

print("Tratar valores nulos")

# Variáveis numéricas
df[['Nota', 'N_Avaliações', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto', 'Desconto_MinMax', 'Qtd_Vendidos_Cod', 'Material_Freq']] = df[['Nota', 'N_Avaliações', 'Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto', 'Desconto_MinMax', 'Qtd_Vendidos_Cod', 'Material_Freq']].fillna(0)

df[['Preço', 'Preço_MinMax']] = df[['Preço', 'Preço_MinMax']].fillna(df[['Preço', 'Preço_MinMax']].median())

# Variaveis categóricas
df.fillna({'Material': 'Desconhecido'}, inplace=True)
df[['Gênero']] = df[['Gênero']].fillna('Não informado')

for col in ['Review1', 'Review2', 'Review3']:
    df[col] = df[col].fillna('Sem Review')

print('Identificar dados faltantes:')
print(df.isnull().sum())

# Criando um dataframe
dictionary = pd.DataFrame([
    {
        "variavel": "Título",
        "descricao": "Nome completo do produto comercializado (modelo, marca e variações)",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Nota",
        "descricao": "Nota de avaliação atribuída pelos clientes (escala de 0 a 5)",
        "tipo": "quantitativa",
        "subtipo": "continua"
    },{
        "variavel": "N_Avaliações",
        "descricao": "Número total de avaliações recebidas pelo produto.",
        "tipo": "quantitativa",
        "subtipo": "discreta"
    },{
        "variavel": "Desconto",
        "descricao": "Percentual de desconto aplicado ao produto no momento da coleta dos dados.",
        "tipo": "quantitativa",
        "subtipo": "continua"
    },{
        "variavel": "Marca",
        "descricao": "Nome da marca do produto.",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Material",
        "descricao": "Nome do material principal de fabricação do produto.",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Gênero",
        "descricao": "Público-alvo do produto (Masculino, Feminino, Unissex ou Não informado).",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Temporada",
        "descricao": "Estação ou período do ano para o qual o produto é mais indicado (ex: primavera/verão).",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Review1",
        "descricao": "Comentário textual de um cliente sobre o produto (primeiro review disponível).",
        "tipo": "qualitativa",
        "subtipo": "texto livre"
    },{
        "variavel": "Review2",
        "descricao": "Comentário textual de outro cliente sobre o produto (segundo review disponível).",
        "tipo": "qualitativa",
        "subtipo": "texto livre"
    },{
        "variavel": "Review3",
        "descricao": "Comentário textual de outro cliente sobre o produto (terceiro review disponível).",
        "tipo": "qualitativa",
        "subtipo": "texto livre"
    },{
        "variavel": "Qtd_Vendidos",
        "descricao": "Quantidade de unidades vendidas do produto.",
        "tipo": "qualitativa",
        "subtipo": "ordinal"
    },{
        "variavel": "Preço",
        "descricao": "Preço de venda do produto em reais (R$).",
        "tipo": "quantitativa",
        "subtipo": "continua"
    },{
        "variavel": "Nota_MinMax",
        "descricao": "Nota média normalizada em escala min-max (0 a 1).",
        "tipo": "quantitativa",
        "subtipo": "continua"
    },{
        "variavel": "N_Avaliações_MinMax",
        "descricao": "Número de avaliações normalizado em escala min-max (0 a 1).",
        "tipo": "quantitativa",
        "subtipo": "continua"
    },{
        "variavel": "Desconto_MinMax",
        "descricao": "Percentual de desconto normalizado em escala min-max (0 a 1).",
        "tipo": "quantitativa",
        "subtipo": "continua"
    },{
        "variavel": "Preço_MinMax",
        "descricao": "Preço do produto normalizado em escala min-max (0 a 1).",
        "tipo": "quantitativa",
        "subtipo": "continua"
    },{
        "variavel": "Marca_Cod",
        "descricao": "Código numérico atribuído a cada marca para facilitar análises e agrupamentos.",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Material_Cod",
        "descricao": "Código numérico atribuído a cada tipo de material.",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Temporada_Cod",
        "descricao": "Código numérico atribuído a cada temporada.",
        "tipo": "qualitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Qtd_Vendidos_Cod",
        "descricao": "Versão numérica da variável 'Qtd_Vendidos', representando a estimativa quantitativa real.",
        "tipo": "quantitativa",
        "subtipo": "nominal"
    },{
        "variavel": "Marca_Freq",
        "descricao": "Frequência relativa de ocorrência da marca no conjunto de dados (proporção).",
        "tipo": "quantitativa",
        "subtipo": "continua"
},{
        "variavel": "Material_Freq",
        "descricao": "Frequência relativa de ocorrência do material no conjunto de dados (proporção).",
        "tipo": "quantitativa",
        "subtipo": "continua"
    }
])

print(dictionary.to_string())

# ======================= Histogramas =============================
fig, axes = plt.subplots(4, 3, figsize=(16,10), dpi=120)
fig.suptitle('Distribuição de variáveis quantitativas', fontweight='bold', fontsize=13)

axs = axes.flatten()
quantitative_columns = dictionary.query("tipo == 'quantitativa'").variavel.to_list()
for i, variavel in enumerate(quantitative_columns):
    ax = sns.histplot(
        data=df,
        x=variavel,
        ax=axs[i],
        bins=30
    )
    ax.set_title(f"Distribuição da variável '{variavel}'",  fontsize=10, pad=6)
    ax.set_xlabel(variavel, fontsize=9)
    ax.set_ylabel('Quantidade',  fontsize=9)

for j in range(len(quantitative_columns), len(axs)):
    axs[j].axis("off")

plt.tight_layout(rect=[0, 0, 1, 0.95], pad=0.8, w_pad=1.2, h_pad=2.2)
plt.show()

# Visualizando os histogramas, podemos afirmar que:

#   - A maior parte das variáveis apresenta distribuição assimétrica à direita (muitos valores pequenos e poucos valores altos);
#   - Isso indica concentração de produtos com baixo preço, desconto e número de avaliações, enquanto poucos produtos têm valores extremos (outliers);
#   - A variável Nota é uma exceção: a maioria das avaliações está próxima de 4 e 5, mostrando alta satisfação dos clientes.


# ============================== Gráfico de Dispersão ====================================
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Preço', y='Nota', color='#0F9D58', alpha=0.6, s=40)
plt.title('Relação entre Preço e Nota de Avaliação', fontweight='bold', fontsize=13)
plt.xlabel('Preço (R$)', fontsize=10)
plt.ylabel('Nota', fontsize=10)
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Desconto', y='Qtd_Vendidos_Cod', color='#0F9D58', alpha=0.6, s=40)
plt.yscale('log')
plt.title('Relação entre Desconto e Quantidade Vendida', fontweight='bold', fontsize=13)
plt.xlabel('Desconto (%))', fontsize=10)
plt.ylabel('Quantidade Vendidos', fontsize=10)
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='N_Avaliações', y='Nota', color='#0F9D58', alpha=0.6, s=40)
plt.xscale('log')
plt.title('Relação entre Número de Avaliações e Nota', fontweight='bold', fontsize=13)
plt.xlabel('Número de Avaliações', fontsize=10)
plt.ylabel('Nota', fontsize=10)
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Preço', y='Qtd_Vendidos_Cod', color='#0F9D58', alpha=0.6, s=40)
plt.yscale('log')
plt.title('Relação entre Preço e Quantidade Vendida', fontweight='bold', fontsize=13)
plt.xlabel('Preço (R$)', fontsize=10)
plt.ylabel('Quantidade vendidos', fontsize=10)
plt.show()

plt.figure(figsize=(8,5))
top_generos = df['Gênero'].value_counts().head(6).index
df_plot = df[df['Gênero'].isin(top_generos)].copy()
sns.scatterplot(data=df_plot, x='Desconto', y='Preço', hue='Gênero', alpha=0.6, s=40)
plt.title('Relação entre Desconto e Preço por Gênero', fontweight='bold', fontsize=13)
plt.xlabel('Desconto', fontsize=10)
plt.ylabel('Preço (R$)', fontsize=10)
plt.show()

# Visualizando os gráficos de dispersão, podemos observar que:

#   - Não há correlação clara entre preço e nota, logo produtos caros e baratos recebem notas semelhantes;
#   - A maioria das notas está entre 4 e 5, independentemente do preço, sugerindo que o valor do produto não influencia diretamente a avaliação dos consumidores;
#   - O gráfico mostra uma leve tendência de aumento na quantidade vendida conforme o desconto cresce, embora não seja uma relação linear forte;
#   - Mesmo com descontos altos (acima de 40%), há produtos com poucas vendas, o que sugere que o desconto sozinho não é suficiente para impulsionar as vendas em todos os casos;
#   - A maior concentração de pontos ocorre entre 0% e 20% de desconto, faixa na qual também estão os produtos com maior volume de vendas;
#   - Esse comportamento indica que, embora promoções atraiam consumidores, outros fatores, como marca, reputação e necessidade do produto também influenciam fortemente as vendas;
#   - A maioria dos produtos possui poucas avaliações, concentradas em notas altas (4 a 5);
#   - Produtos com muitas avaliações também tendem a manter boas notas, indicando consistência na qualidade percebida e confiança do consumidor;
#   - É possível perceber uma tendência negativa entre preço e quantidade vendida, conforme o preço aumenta, a quantidade vendida tende a diminuir;
#   - A maioria dos produtos concentra-se na faixa de preços entre R$ 50 e R$ 200, com volumes de venda variando amplamente entre 10 e 10 000 unidades;
#   - Há poucos produtos com preços acima de R$ 300, e esses tendem a apresentar baixas vendas, sugerindo sensibilidade do consumidor a preços altos;
#   - Descontos estão distribuídos por todas as faixas de preço e gêneros;
#   - Em geral, itens masculinos e femininos ocupam toda a faixa de descontos; não há um gênero com “descontos sistematicamente maiores”;

# =================== Mapa de Calor =========================
corr = df.corr(numeric_only = True)
mask = np.triu(np.ones_like(corr, dtype=bool))
plt.figure(figsize=(10,10))
ax = sns.heatmap(
    corr,
    mask=mask,
    cmap='coolwarm',
    square=True,
    linewidths=.5,
    cbar_kws={"shrink": .5},
    annot=True,
    fmt=".2f"
)
plt.title('Mapa de Calor - Correlação entre Variáveis Numéricas', fontweight='bold', fontsize=13)
plt.show()

# Visualizando o Mapa de Calor, podemos observar que:

#   - As maiores correlações são entre as variáveis normalizadas e seus pares originais (exemplo: N_Avaliações e N_Avaliações_MinMax);
#   - Preço, Desconto e Nota têm correlações fracas entre si (aproximadamente menor que 0.2), sugerindo relações não lineares;
#   - Qtd_Vendidos_Cod tem correlação moderada apenas com N_Avaliações_MinMax (aproximadamente 0.82), indicando que produtos com maior número de avaliações tendem também a registrar mais vendas.

# =================== Gráfico de Barras =========================
plt.figure(figsize=(10,6))
ordem = df.groupby('Gênero')['Preço'].mean().sort_values(ascending=False).index
sns.barplot(data=df, x='Gênero', y='Preço', order=ordem, estimator=np.mean, ci=None, palette='viridis')
plt.title('Preço médio por Gênero', fontweight='bold', fontsize=13)
plt.xlabel('Gênero', fontsize=10);
plt.ylabel('Preço médio (R$)', fontsize=10)
plt.xticks(rotation=50, ha='right', fontsize=9)

plt.tight_layout()
plt.show()

top_marcas = df.groupby('Marca')['Qtd_Vendidos_Cod'].mean().nlargest(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_marcas.values, y=top_marcas.index, orient='h')
plt.title('Top 10 marcas por média de quantidade vendida', fontweight='bold', fontsize=13)
plt.xlabel('Média de Qtd_Vendidos_Cod', fontsize=10)
plt.ylabel('Marca', fontsize=10)

plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Visualizando os Gráficos de Barras, podemmos observar que:

#   - O maior preço médio aparece em “menino” e “masculino”;
#   - “unissex” tem o menor preço médio;
#   - Diferenças de preço médio entre gêneros podem refletir mix de produtos (tamanho, material, kit, etc.), não apenas o gênero em si;
#   - 'moda llevo' e 'zaroc' lideram com folga a média de unidades vendidas, seguidas por 'zorba';
#   - O topo concentrado em poucas marcas sugere efeito de portfólio forte ou marketing mais eficientes;
#   - As demais marcas apresentam médias bem menores..

# =================== Gráfico de Pizza =========================
contagem = df['Gênero'].value_counts(normalize=True)
top_generos = contagem[contagem > 0.03].index  # exibe só gêneros com maior de 3% dos produtos

df_pizza = df.copy()
df_pizza['Gênero Agrupado'] = df_pizza['Gênero'].where(df_pizza['Gênero'].isin(top_generos), 'Outros')
plt.figure(figsize=(8,8))
df_pizza['Gênero Agrupado'].value_counts().plot(
    kind='pie',
    autopct='%.1f%%',
    startangle=90,
)
plt.title('Distribuição por Gênero', fontweight='bold', fontsize=13)
plt.tight_layout()
plt.show()

# Visualizando o Gráfico de Pizza, podemos observar que:

#   - A maior parte dos produtos é destinada ao público feminino (32,9%) e masculino (24,8%), somando juntos mais da metade do catálogo;
#   - Produtos voltados para bebês (14,1%) também representam uma fatia relevante;
#   - Já as categorias “sem gênero” e infantis (“meninos”, “meninas”) aparecem com menor participação;
#   - Essa distribuição mostra foco em público adulto, especialmente feminino.

# ================= Gráfico de Densidade =======================
plt.figure(figsize=(7,5))
sns.kdeplot(data=df, x='Preço', fill=True)
plt.title('Densidade – Preço', fontweight='bold', fontsize=13)
plt.xlabel('Preço (R$)', fontsize=10)
plt.ylabel('Densidade', fontsize=10)
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.show()

plt.figure(figsize=(8,5))
sns.kdeplot(data=df[df['Gênero'].isin(top_generos)], x='Preço', hue='Gênero', fill=True, common_norm=False, alpha=0.4)
plt.title('Densidade – Preço por Gênero', fontweight='bold', fontsize=13)
plt.xlabel('Preço (R$)', fontsize=10)
plt.ylabel('Densidade', fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Visulizando os Gráficos de Densidade, podemos observar que:

# A distribuição de preços é assimétrica à direita, com concentração entre R$50 e R$150.
# Há uma cauda longa de produtos mais caros (acima de R$300), indicando que poucos itens elevam o preço máximo.
# Essa forma sugere que o mercado tem foco em produtos de ticket médio-baixo.
# Todas as curvas têm comportamento semelhante, com pico de densidade entre R$50 e R$150.
# Produtos masculinos e para meninos mostram uma leve tendência a preços mais altos.
# A sobreposição indica que o gênero tem impacto limitado sobre a distribuição geral de preços.

 # ================= Gráfico de Regressão =======================
plt.figure(figsize=(7,5))
sns.regplot(
    data=df, x='Desconto', y='Qtd_Vendidos_Cod',
    scatter_kws={'alpha':0.35, 's':30}, line_kws={'linewidth':2}
)
plt.yscale('log')
plt.title('Desconto vs Quantidade Vendida (com regressão)', fontweight='bold', fontsize=14)
plt.xlabel('Desconto (%)', fontsize=10);
plt.ylabel('Quantidade Vendida', fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7,5))
sns.regplot(
    data=df[df['Nota']>0], x='Preço', y='Nota',
    scatter_kws={'alpha':0.35, 's':30}, line_kws={'linewidth':2}
)
plt.title('Preço vs Nota (com regressão)', fontweight='bold', fontsize=14)
plt.xlabel('Preço (R$)', fontsize=10)
plt.ylabel('Nota', fontsize=10)
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Visualizando os gráficos de Regressão, podemos observar que:

#   - A linha de tendência mostra leve correlação positiva: conforme o desconto aumenta, a quantidade vendida tende a crescer;
#   - A dispersão é alta, sugerindo que outros fatores além do desconto também influenciam as vendas;
#   - A linha de regressão para Preços vs Nota é praticamente horizontal, com leve inclinação negativa;
#   - Isso indica que o preço não tem relação significativa com a avaliação dos clientes.

print("""
Insights:
    - Distribuições: variáveis numéricas são assimétricas à direita. Há muitos produtos com valores baixos e poucos outliers (preço, desconto, avaliações). Nota concentra-se entre 4 e 5.
    - Preço x Nota: relação praticamente nula. Produtos caros e baratos recebem notas semelhantes, percepção de qualidade importa mais que preço.
    - Desconto x Vendas: tendência positiva, porém fraca e não linear. A maioria dos volumes está com 0 e 20% de desconto, ou seja, só o desconto não garante alta venda.
    - Preço x Vendas: relação inversa (mais baratos tendem a vender mais), mas existem exceções (itens caros com bom volume, provável efeito de marca).
    - Avaliações: itens com mais avaliações costumam manter notas altas, sugerindo confiança/qualidade consistente.
    - Correlações: fortes apenas entre variáveis normalizadas e seus originais. Qtd_Vendidos (ou Cod) tem correlação moderada com N_Avaliações (aproximadamente 0,8), demais relações são fracas.
    - Gênero: distribuição de preços semelhante entre grupos. Os gêneros masculino e menino são levemente mais caros. Já para feminino e masculino domina o catálogo.
    - Marcas: poucas marcas concentram a média de unidades vendidas, efeito de marketing.

""")
