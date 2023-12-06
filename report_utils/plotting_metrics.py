import matplotlib.pyplot as plt
import ast
import sys

file_path = sys.argv[1]
epochs = []
bleu_1_values = []
cider_values = []
with open(file_path, 'r') as file:
    for line in file:
        data = ast.literal_eval(line)
        epochs.append(data['epoch'])
        bleu_1_values.append(data['Bleu_1'])
        cider_values.append(data['CIDEr'])

# Plot Bleu_1 vs epoch
plt.figure(figsize=(10, 6))
plt.plot(epochs, bleu_1_values, marker='o', label='Bleu_1')
plt.xlabel('Epoch')
plt.ylabel('Bleu_1 Scores')
plt.title('Bleu_1 Scores vs Epoch')
plt.legend()
plt.grid(True)
plt.savefig('bleu_1_vs_epoch.png')
# plt.show()

# Plot CIDEr vs epoch
plt.figure(figsize=(10, 6))
plt.plot(epochs, cider_values, marker='x', label='CIDEr', color='orange')
plt.xlabel('Epoch')
plt.ylabel('CIDEr Scores')
plt.title('CIDEr Scores vs Epoch')
plt.legend()
plt.grid(True)
plt.savefig('cider_vs_epoch.png')
# plt.show()