import matplotlib.pyplot as plt
import ast
import sys

file_path = sys.argv[1]

epochs = []
train_loss_values = []

with open(file_path, 'r') as file:
    for line in file:
        data = ast.literal_eval(line)
        epochs.append(data['epoch'])
        train_loss_values.append(float(data['train_loss']))  

plt.figure(figsize=(10, 6))
plt.plot(epochs, train_loss_values, marker='o', label='Train Loss', color='red')
plt.xlabel('Epoch')
plt.ylabel('Train Loss')
plt.title('Train Loss vs Epoch')
plt.legend()
plt.grid(True)
plt.savefig('train_loss_vs_epoch.png')  
# plt.show()
