import matplotlib.pyplot as plt

bar1 = [1,2,3,4,5]
bar2 = [6,7,8]
x_labels = ['A','B','C',]
plt.bar(x_labels, bar1, label='Group1')
plt.bar(x_labels, bar, bottle=bar1, label='Group2')
plt.legent()
plt.show()