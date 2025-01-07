import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Função para calcular a distribuição de Benford
def benford_distribution():
    return [np.log10(1 + 1/d) for d in range(1, 10)]

# Função para extrair dígitos iniciais
def first_digit(n):
    while n >= 10:
        n //= 10
    return n

# Dados fictícios para simulação
instagram_links = [f"https://instagram.com/perfil{i}" for i in range(10)]
linkedin_links = [f"https://linkedin.com/in/perfil{i}" for i in range(10)]

instagram_followers = [random.randint(100, 50000) for _ in range(10)]
linkedin_followers = [random.randint(100, 10000) for _ in range(10)]

instagram_df = pd.DataFrame({
    'Perfil': instagram_links,
    'Seguidores': instagram_followers
})

linkedin_df = pd.DataFrame({
    'Perfil': linkedin_links,
    'Seguidores': linkedin_followers
})

# Combinar os dados fictícios
all_profiles_df = pd.concat([instagram_df, linkedin_df], ignore_index=True)

# Interface do Streamlit
st.title("Análise de Perfis Usando a Lei de Benford")

# Entrada de URLs e seguidores
urls = st.text_area("Cole os links dos perfis (um por linha):")
user_followers_input = st.text_area("Cole a quantidade de seguidores correspondente a cada link (um número por linha, na mesma ordem):")

if st.button("Analisar"):
    urls_list = urls.splitlines()
    followers_list = user_followers_input.splitlines()

    if len(urls_list) != len(followers_list):
        st.error("O número de URLs e de quantidades de seguidores fornecidos não coincide. Certifique-se de que ambos têm o mesmo número de linhas.")
    else:
        # Converter seguidores fornecidos pelo usuário para números
        try:
            user_followers = [int(f) for f in followers_list]
        except ValueError:
            st.error("Certifique-se de que todas as quantidades de seguidores fornecidas são números válidos.")
            st.stop()

        # Criar DataFrame com os dados fornecidos pelo usuário
        user_profiles = pd.DataFrame({
            'Perfil': urls_list,
            'Seguidores': user_followers
        })

        # Combinar os dados fictícios e os dados fornecidos pelo usuário
        combined_df = pd.concat([all_profiles_df, user_profiles], ignore_index=True)

        # Extraindo dígitos iniciais
        combined_df['Primeiro Dígito'] = combined_df['Seguidores'].apply(first_digit)

        # Contagem da distribuição
        observed_distribution = combined_df['Primeiro Dígito'].value_counts(normalize=True).sort_index()
        benford_dist = benford_distribution()

        # Visualização
        fig, ax = plt.subplots()
        ax.bar(observed_distribution.index, observed_distribution.values, alpha=0.5, label='Observado')
        ax.plot(range(1, 10), benford_dist, marker='o', color='red', label='Esperado (Benford)')
        ax.set_xlabel('Primeiro Dígito')
        ax.set_ylabel('Frequência')
        ax.set_title('Distribuição dos Dígitos Iniciais')
        ax.legend()

        st.pyplot(fig)

        # Mostrar tabela dos perfis analisados
        st.subheader("Perfis Analisados (Fictícios + Fornecidos)")
        st.dataframe(combined_df)

        # Análise detalhada da confiabilidade dos dados
        st.subheader("Análise da Confiabilidade dos Dados")
        st.write("### Indícios de Manipulação dos Dados:")
        st.markdown("- Quando a distribuição observada se desvia significativamente da distribuição esperada pela Lei de Benford, observe o gráfico.")
        st.markdown("- Quanto maior a diferença entre as duas distribuições, maior a suspeita de possível manipulação dos dados.")
        st.markdown("- Por exemplo, no gráfico apresentado, se a distribuição observada for muito maior que a esperada, e muito menor para outros dígitos, isso é um forte indício de manipulação.")

        st.write("### Dados Confiáveis:")
        st.markdown("- Quando a distribuição observada se aproxima muito da distribuição esperada pela Lei de Benford.")
        st.markdown("- Quanto menor a diferença entre as duas distribuições, maior a confiabilidade dos dados.")
        st.markdown("- Se a distribuição observada acompanha de perto a curva da distribuição de Benford, é um sinal de que os dados seguem o padrão natural esperado e, portanto, podem ser considerados confiáveis.")

        st.write("### Resumo:")
        st.markdown("- Quanto maior o desvio da distribuição observada em relação à distribuição de Benford, mais suspeita de manipulação dos dados.")
        st.markdown("- Quanto mais próximas as duas distribuições, maior a confiabilidade dos dados analisados.")

        st.info("Este tipo de análise comparativa entre a distribuição observada e a distribuição de Benford é uma ferramenta útil para identificar possíveis irregularidades nos dados.")



