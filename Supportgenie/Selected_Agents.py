import random
from Agent_data import Agent

n=int(input("Enter Number Of Agents :"))   #Enter No of Agents 
selection_mode=int(input("Enter Number Of Selection mode :")) #Selectionmode 1.All available 2.Leastbusy 3.Random
j=0
agents=[]    #Enter Agent Data here
while j<n:
 agent=Agent(eval(input()),input(),[item for item in input("Enter the list items : ").split()])
 agents.append(agent)
 j=j+1     

def Agent_selection(agents,selection_mode):  # Agent Selection function
 selected_agents=[]
 issue="sales"                               #issues
 i=0
 sm=selection_mode
 max=agents[0].available_since
 if sm==1:                  # All available
  while i<n:
   if agents[i].is_available=="True":
    print(agents[i].is_available)
    selected_agents.append("agent"+str(i+1))
   i=i+1
  return selected_agents
 elif sm==2:             #Least busy mode
  i=0
  least_busy_agent=''
  while i<n:
   if agents[i].is_available==True and issue in agents[i].roles:
    selected_agents.append("agent"+str(i+1))
    if agents[i].available_since<=max:
     max=agents[i].available_since
     least_busy_agent="agent"+str(i+1)
   i=i+1
  return least_busy_agent
 elif sm==3:                   #Random mode
  print("sm==3")
  while i<n:
   if agents[i].is_available=="True" and issue in agents[i].roles:
    selected_agents.append("agent"+str(i+1))
   i=i+1
  return random.choice(selected_agents)
 else:
  print("Please enter a valid Selection Mode ")

sa=Agent_selection(agents,selection_mode)  #calling Agent selection function
print(sa)