# Benford Analysis

A análise matemática realizada neste código se baseia na Lei de Benford, que descreve a distribuição natural dos dígitos iniciais em muitos conjuntos de dados do mundo real.

Explicação mais detalhada da análise matemática:
A função benford_distribution() calcula a distribuição esperada de acordo com a Lei de Benford.
A fórmula utilizada é: P(d) = log10(1 + 1/d), onde d é o dígito inicial (de 1 a 9).
Essa fórmula descreve a probabilidade esperada de cada dígito inicial aparecer no conjunto de dados.

Extração dos Dígitos Iniciais:
A função first_digit(n) extrai o primeiro dígito de um número n.
Isso é feito dividindo repetidamente o número por 10 até que o primeiro dígito seja obtido.

Contagem da Distribuição Observada:
O código conta a frequência de cada dígito inicial (de 1 a 9) no conjunto de dados combinado (dados fictícios + dados fornecidos pelo usuário).
Essa contagem é normalizada para obter a distribuição observada.

Comparação com a Distribuição de Benford:
A distribuição observada é comparada visualmente com a distribuição esperada de acordo com a Lei de Benford.
Isso é feito utilizando um gráfico de barras, onde as barras representam a distribuição observada e a linha vermelha representa a distribuição esperada de Benford.
A comparação entre a distribuição observada e a distribuição esperada de Benford pode revelar se os dados seguem o padrão esperado pela Lei de Benford ou se há indícios de possíveis irregularidades ou manipulação dos números

The mathematical analysis performed in this code is based on Benford's Law, which describes the natural distribution of leading digits in many real-world datasets.

Detailed Explanation of the Mathematical Analysis:
The function benford_distribution() calculates the expected distribution according to Benford's Law. The formula used is: P(d) = log10(1 + 1/d),
where d is the leading digit (from 1 to 9). This formula describes the expected probability of each leading digit appearing in the dataset.

Extraction of Leading Digits:
The function first_digit(n) extracts the first digit of a number n. This is accomplished by repeatedly dividing the number by 10 until the first digit is obtained.

Counting the Observed Distribution:
The code counts the frequency of each leading digit (from 1 to 9) in the combined dataset (fictional data + user-provided data). This count is normalized to obtain the observed distribution.

Comparison with Benford's Distribution:
The observed distribution is visually compared with the expected distribution according to Benford's Law. This is done using a bar chart, where the bars represent the observed distribution and a red line represents the expected Benford distribution. The comparison between the observed distribution and the expected Benford distribution can reveal whether the data follows the pattern expected by Benford's Law or if there are indications of potential irregularities or manipulation of the numbers.

Link App:
https://projetoappapp-ekokniffmdxkcgye8wiasy.streamlit.app/
