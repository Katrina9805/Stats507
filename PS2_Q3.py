dic = {'G': '2011-2012', 'H': '2013-2014', 'I': '2015-2016', 'J': '2017-2018'}
gend = {
    1: 'Male',
    2: 'Female'
}

# Question 1
#a, b
for i in ['G', 'H', 'I', 'J']:
    temp = pd.read_sas(filepath_or_buffer="../hw2_data/DEMO_" + i + ".XPT")
    str_names = 'SEQN,RIAGENDR,RIDAGEYR,DMDEDUC2,RIDSTATR'
    var_names = str_names.split(',')
    temp = temp[var_names]
    # convert column names
    temp.rename(columns={'SEQN': 'id', 
                         'RIAGENDR': 'gender',
                         'RIDAGEYR': 'age', 
                         'DMDEDUC2': 'edu',
                         'RIDSTATR': 'exam_status'}, inplace=True)
    temp = temp.fillna(-1)
    # convert column types
    for j in temp.columns[:]:
        temp[j] = temp[j].apply(np.int64)
    temp.gender = temp.gender.map(
        gend).fillna('N/A')
    # add <20 >20 age column 
    temp['under_20'] = ["yes" if i < 20 else "no" for i in temp['age']]
    # college to two levels
    temp['college'] = ["some college/college graduate" if (i == 4 or i == 5) and j == 'no'
                       else "No college/<20" for (i,j) in zip(temp['edu'],temp['under_20'])]


    # oral data
    temp2 = pd.read_sas(filepath_or_buffer="../hw2_data/OHXDEN_" + i + ".XPT")
    temp2.rename(columns={'OHDDESTS': 'ohx_status', 
                          'SEQN': 'id'}, inplace=True)
    temp2 = temp2.fillna(-1)
    temp2 = temp2[['id','ohx_status']]
    temp2['ohx_status'] = temp2['ohx_status'].astype(int)
    
     # merge two dataset
    temp = pd.merge(temp, temp2, how="outer", on="id")
    

    temp['ohx'] = ['complete' if i == 2 and j == 1 else 'missing' 
           for (i,j) in zip(temp['exam_status'], temp['ohx_status'])]

   

    # create final df
    d = {
        'id': temp['id'],
        'gender': temp['gender'],
        'age': temp['age'],
        'under_20': temp['under_20'],
        'college': temp['college'],
        'exam_status': temp['exam_status'],
        'ohx_status': temp['ohx_status'],
        'ohx': temp['ohx']
    }
    df = pd.DataFrame(data=d)
    
    # save to pickle form
    df.to_pickle("./DEMO_" + i + ".pkl")
