# 🤖 Revisão da Segunda Aula: Fundamentos de dados

# 💾 Armazenamento de Informações com Arquivos de Dados

## 📚 Para que servem os arquivos de dados?

Arquivos de dados servem como **repositórios permanentes de informações**. Diferente de variáveis em memória (que somem ao fechar o programa), os dados nos arquivos **persistem**.

**🧠 Exemplo prático:**  
Um sistema de cadastro salva nome, idade e curso dos usuários em um arquivo. Mesmo depois de desligar o PC, os dados continuam lá.

---

## 📁 Tipos de Arquivos de Dados

### 1. 📄 CSV (Comma-Separated Values)

- 🔹 **Formato simples** baseado em texto.
- 🔹 Cada linha = 1 registro.
- 🔹 Campos separados por vírgula (ou ponto e vírgula).
- 🔹 Funciona bem com Excel e programas de planilha.
- ❌ Não suporta estruturas complexas.

**📌 Exemplo:**
```csv
nome,idade,curso
João,20,Engenharia
Maria,22,Medicina
```

### 2. 🧩 JSON (JavaScript Object Notation)

🔹 Formato de texto estruturado, com objetos e arrays.

🔹 Muito usado em APIs e aplicações web.

🔹 Flexível: aceita dados aninhados.

❌ Não é fácil de visualizar em planilhas.

📌 Exemplo:

[
  { "nome": "João", "idade": 20, "curso": "Engenharia" },
  { "nome": "Maria", "idade": 22, "curso": "Medicina" }
]

### 3. ☁️ Google Sheets (Planilhas do Google)
🔹 Planilha online, colaborativa.

🔹 Acessível de qualquer lugar com internet.

🔹 Ideal para equipes e automações com scripts.

❌ Depende da nuvem e de conta Google.

📌 Exemplo prático:
Time de vendas atualiza metas diárias em uma planilha que o gerente vê em tempo real.

### 🛠️ Aplicações Práticas

| Tipo de Arquivo      | Onde Usar                 | Por Quê?                      |
| -------------------- | ------------------------- | ----------------------------- |
| 📄 **CSV**           | Exportar dados para Excel | Simples, compatível com tudo  |
| 🧩 **JSON**          | APIs, configs, apps web   | Estrutura rica e leve         |
| ☁️ **Google Sheets** | Dashboards e relatórios   | Compartilhável e colaborativo |


# Vantagens e Limitações de Formatos de Dados

## 📊 **Vantagens do Google Sheets**
- 🌐 **Acessibilidade em tempo real**: Como é baseado na nuvem, você pode acessar e editar a planilha de qualquer lugar, de qualquer dispositivo.
- 🤝 **Colaboração**: Vários usuários podem editar o mesmo arquivo simultaneamente, com comentários e sugestões, o que é ótimo para trabalhos em equipe.
- 🔗 **Integração com outros serviços Google**: O Google Sheets se integra bem com outras ferramentas da Google, como Docs, Drive, e Gmail.
- 📈 **Fórmulas e ferramentas avançadas**: Oferece uma vasta gama de fórmulas, gráficos e funções que facilitam a análise e visualização de dados.
- 🖥️ **Facilidade de uso**: Interface intuitiva e fácil de aprender, ideal para quem não é especialista em Excel ou outras planilhas.

## 📜 **Vantagens do CSV**
- 📝 **Simplicidade**: O formato CSV é basicamente uma lista de valores separados por vírgulas. É fácil de entender e manipular, tanto para máquinas quanto para humanos.
- 🔄 **Compatibilidade**: Praticamente qualquer programa ou linguagem de programação pode ler ou gerar arquivos CSV, tornando-o muito versátil.
- ⚡ **Leveza**: Como os arquivos CSV não têm formatação, eles são muito mais leves comparados a outros formatos, como o Excel.
- 🔄 **Facilidade de importação e exportação**: Ideal para exportar ou importar dados entre diferentes sistemas, especialmente em grandes volumes de dados.

## ⚠️ **Limitações do JSON**
- 🧩 **Maior complexidade**: O JSON pode ser mais difícil de ler ou editar manualmente, especialmente se for muito complexo e aninhado.
- 🚫 **Sem suporte nativo para formatação**: Ao contrário de CSV ou planilhas, o JSON não tem suporte para formatação de células, estilos ou tipos de gráficos.
- 🏋️ **Tamanho dos arquivos**: Quando os dados são muito grandes, o arquivo JSON pode crescer significativamente, se tornando difícil de gerenciar e de transmitir.
- 📉 **Pouco adequado para grandes conjuntos de dados tabulares**: Embora seja ótimo para representar dados estruturados, o JSON não é a melhor opção quando se trata de grandes volumes de dados.