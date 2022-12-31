import matplotlib.pyplot as plt

r =  '1.674e-24 g/mol'
r = r.replace('e-','e{-')
r = r.replace(' g/','} g/')

r = r.replace('.',',')
r = r.replace('e','.10^')
r = r.replace(' ','\\ ')
print(r)



a = f'Massa\ Molar = {r}'
print(a)
ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
plt.text(0.4,0.4,'$%s$' %a, size=20, color="black")
plt.figsize=(3,1)
plt.show()

