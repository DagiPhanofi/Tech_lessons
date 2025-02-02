#%%
# create a list of all the students 
student_list = ['Beckael','Biruk','Nahili','Keti','Abel','Sifan','Freja','Debora','Yohanna','Kaleab','Andreas','Rbika']
present = []
absent = []

for name in student_list:
    
    user_input = input(name+': (y/n)?: ')

    if user_input == 'y':
        present.append(name)
    elif user_input== 'n':
        absent.append(name)
    else:
        print('Invalid input, please try again')        
           
# print attendees and absentees
print('Attendees: '+ str(present))
print('Absentees: '+ str(absent))

# %%
