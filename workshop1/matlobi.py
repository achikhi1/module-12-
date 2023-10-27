import matplotlib.pyplot as plt 
# ik inporteer hier en geef hem de naam plt
my_data = [11, 12, 13] 
# ik geef hem hier de data
my_labels = 'label1', 'label2', 'label3' 
# dit zijn de namen
plt.pie(my_data, labels=my_labels, autopct='%1.7f%%')
# hier doet hij alles bij elkaar
plt.title('My Title') 
# de titel
plt.axis('equal')
plt.show() 
# hier vertoont hij alles