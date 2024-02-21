#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Part 2


# In[2]:


#DONE
#Q1
def protein_list(proteins):
    return len(set(proteins))


# In[3]:


proteins = ["PF13411.1", "PF12728.1", "PF01381.2", "PF00205.2", "PF10875.1", "PF05766.1",
"PF00860.2", "PF10766.1", "PF11812.1"]


# In[4]:


protein_list(proteins)


# In[5]:


#DONE
#Q2
def protein_dict(proteins):
    dict1 = {}
    for protein in proteins:
        dict1[protein] = dict1.get(protein,0)+1
    return dict1


# In[6]:


protein_dict(proteins)


# In[7]:


#DONE
#Q3
def combo_dict(dict1, dict2):
    
    single_dict = {}
    
    combo_keys = set(dict1.keys()) | set(dict2.keys())
    
    single_dict = {key:(dict1.get(key, 0), dict2.get(key, 0)) for key in combo_keys}
    
    return single_dict


# In[8]:


proteins1 = {'PF13411.1': 1,
 'PF12728.1': 1, 'PF01381.2': 1, 'PF00205.2': 1, 'PF10875.1': 1,
 'PF05766.1': 1,
 'PF00860.2': 1,
 'PF10766.1': 1,
 'PF11812.1': 1}

proteins2 = {'PF13411.1': 2,
 'PF12728.1': 1, 'PF01381.2': 1,'PF00205.2': 1, 'PF10875.1': 1,
 'PF05766.1': 1,
 'PF00860.2': 1,
 'PF10766.1': 1,
 'PF11812.1': 0}


# In[9]:


combo_dict(proteins1, proteins2)


# In[10]:


#Part 3


# In[21]:


#DONE
#Q1
def iso_format(dates):
    
    iso_dates = []
    
    for date in dates:
        months = {"January":"01", "February":"02", "March":"03", "April":"04","May":"05","June":"06",
                 "July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
        
        month, day, year = date.split()[0],date.split()[1].strip(','),date.split()[2]
        
        if len(day) == 1:
            day = '0'+ day
        
        proper_dates = f"{year}-{months[month]}-{day}"
        
        iso_dates.append(proper_dates)
        
    return iso_dates


# In[22]:


dates = ["February 6, 1992", "February 18, 1992", "February 27, 1992"]
iso_format(dates)


# In[32]:


#DONE
#Q2

def sorted_dates(iso_dates):
    
    separate = iso_dates.split('-')
    
    return separate[0], separate[1], separate[2]


# In[33]:


to_order = ['1992-02-6', '1992-02-18', '1992-02-27']
ordered = sorted(to_order, key = sorted_dates)
ordered 

