import matplotlib.pyplot as plt

# 📋 Dados fictícios de raças
racas = ['Chihuahua', 'Poodle', 'Labrador', 'Pastor Alemão', 'Bulldog', 'Golden Retriever']
alturas = [15, 35, 60, 65, 40, 60]  # em centímetros
pesos = [3, 8, 30, 35, 24, 32]      # em quilogramas
cores = ['orange', 'pink', 'green', 'blue', 'brown', 'gold']

plt.figure(figsize=(10, 6))
plt.scatter(alturas, pesos, c=cores, s=150)

# 🏷️ Adiciona os nomes das raças no gráfico
for i in range(len(racas)):
    plt.text(alturas[i]+0.5, pesos[i]+0.5, racas[i], fontsize=9)

plt.title('🐕 Altura vs Peso de Diferentes Raças de Cachorro')
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.grid(True)

# 💾 Salvar imagem
plt.savefig("grafico_racas_cachorro.png")
plt.show()