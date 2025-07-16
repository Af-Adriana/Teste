import matplotlib.pyplot as plt
 

categorias=["Python", "JavaScript", "Java", "HTML5", "CSS"]
quantidade=[80,65,40,69,71]

plt.bar(categorias, quantidade)
plt.title("Linguagens mais usadas")
plt.xlabel("Linguagens")
plt.ylabel("Quantidade")

plt.show()