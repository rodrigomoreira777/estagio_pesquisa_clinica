import json
import matplotlib.pyplot as plt

# Carregando a string "JSON" para o programa:
with open('https://github.com/rodrigomoreira777/estagio_pesquisa_clinica/blob/main/vaga_pesquisa_clinica/dados/dataset.json', 'r') as arquivo:
    conteudo = arquivo.read()
# string carregada.

# Converterndo a string carregada para uma lista de dicionarios python:
data = json.loads(conteudo)
# String convertida. Tem-se agora uma lista de dicionarios, caracterisco do formato JSON.

# Desempacotando os dados de cada paciente para variaveis auxiliares e gerando os graficos.
for i in range(0, len(data), 1):
    hyp = []
    peep = []
    coll = []
    aux = True
    melhor_peep = 0

    for j in range(0, len(data[i]['Titration Steps']), 1):
        hyp.append(float(data[i]['Titration Steps'][j].get('Hyperdistension')))
        peep.append(float(data[i]['Titration Steps'][j].get('PEEP')))
        coll.append(float(data[i]['Titration Steps'][j].get('Collapse')))

        if (coll[j] >= hyp[j]) and (aux is True):
            melhor_peep = data[i]['Titration Steps'][j - 1].get('PEEP')
            aux = False

    plt.title(data[i].get('Patient ID'), fontsize=24, weight='bold')
    plt.plot(peep, hyp, marker='s', lw=1, ls='--', ms=5, label='Hiperdistensão')
    plt.plot(peep, coll, marker='o', lw=1, ls='--', ms=5, label='Colapso')
    plt.axis([max(peep) + 2, min(peep) - 2, min(hyp) - 5, 110])
    plt.xlabel("PEEP (cm $\mathrm{H}_2\mathrm{O}$)", fontsize=16)
    plt.ylabel("(%)", fontsize=20)
    plt.legend(loc=2)
    plt.grid(True)

    plt.axvline(x=melhor_peep, color='b', ls='-.', ymax=0.9)

    plt.text(melhor_peep + 1.8, 101, 'Melhor PEEP', fontsize=14, color='b', weight='bold')
    # plt.figure(figsize=(6.4, 4.8))
    plt.savefig('https://github.com/rodrigomoreira777/estagio_pesquisa_clinica/tree/main/vaga_pesquisa_clinica/dados/graficos' + data[i].get('Patient ID') + '.png')
    plt.show()
    hyp.clear()
    peep.clear()
    coll.clear()
