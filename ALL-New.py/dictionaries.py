capitals = {'USA': 'washington DC',
            'India': 'New Dhli',
            'China': 'Beijing',
            'Russia': 'Moscow',}
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las-Vegas'})
#capitals.pop('China')
capitals.clear()


   

#print(capitals['India'])
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())  
for key,value in capitals.items():
     print(key,value)