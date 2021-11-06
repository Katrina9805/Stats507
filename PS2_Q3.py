# Question 3
#a
num_demo = 0 
dic = {'G': '2011-2012', 'H': '2013-2014', 'I': '2015-2016', 'J': '2017-2018'}
for i in ['G', 'H', 'I', 'J']:
    cohort = dic[i]
    temp = pd.read_sas(filepath_or_buffer = "./hw2_data/DEMO_" + i + ".XPT")
    str_names = 'SEQN,RIDAGEYR,RIDRETH3,DMDEDUC2,DMDMARTL,RIDSTATR,SDMVPSU,SDMVSTRA,WTMEC2YR,WTINT2YR'
    var_names = str_names.split(',')
    temp = temp[var_names]
    # convert column names
    temp.rename(columns={'SEQN': 'respondent sequence number', 'RIDAGEYR': 'age', 
                        'RIDRETH3': 'race', 'DMDEDUC2': 'highest_degree',
                        'DMDMARTL': 'marital_status', 
                        'RIDSTATR': 'interview_and_examination_status',
                        'SDMVPSU': 'masked variance unit pseudo-PSU',
                        'SDMVSTRA': 'masked variance unit pseudo-stratum',
                        'WTMEC2YR': 'MEC exam weight', 
                        'WTINT2YR': 'interview weight'}, inplace=True)
    temp['cohort'] = cohort
    temp = temp.fillna(-1)
    
    # convert column types
    for i in temp.columns[:-3]:
        temp[i] = temp[i].apply(np.int64)
    
    # convert categorical names
    race = {1: 'Mexican American',
            2: 'Other Hispanic',
            3: 'Non-Hispanic White',
            4: 'Non-Hispanic Black',
            6: 'Non-Hispanic Asian',
            7: 'Other Race - Including Multi-Racial'}
    
    temp.race = temp.race.map(race).fillna('N/A')
    
    education = {1: 'Less than 9th grade',
                 2: '9-11th grade (Includes 12th grade with no diploma)',
                 3: 'High school graduate/GED or equivalent',
                 4: 'Some college or AA degree',
                 5: 'College graduate or above',
                 7: 'Refused',
                 9: 'Dont Know'}
    
    temp.highest_degree = temp.highest_degree.map(education).fillna('N/A')
    
    marital = { 1: 'Married',
                2: 'Widowed',
                3: 'Divorced',
                4: 'Separated',
                5: 'Never married',
                6: 'Living with partner',
                77: 'Refused',
                99: 'Dont Know'}
    
    temp.marital_status = temp.marital_status.map(marital).fillna('N/A')
    
    interview = {1: 'Interviewed only',
                 2: 'Both interviewed and MEC examined'}
    
    temp.interview_and_examination_status = temp.interview_and_examination_status.map(
        interview).fillna('N/A')
    
    num_demo += temp.shape[0]
    temp.to_pickle("./DEMO_" + i + ".pkl")

#b
num_oral = 0
for i in ['G', 'H', 'I', 'J']:
    temp = pd.read_sas(filepath_or_buffer = "./hw2_data/OHXDEN_" + i + ".XPT")
    temp = temp.filter(regex=("SEQN|OHDDESTS|OHX\d\dTC|OHX\d\dCTC"))
    temp.rename(columns={'SEQN': 'respondent sequence number', 
                         'OHDDESTS': 'dentition_status_code'}, inplace=True)
    temp['cohort'] = cohort
    
    # numeric code to categorical values
    temp = temp.fillna(-1)
    for i in temp.filter(regex=("SEQN|OHDDESTS|OHX\d\dTC")):
        temp[i] = temp[i].apply(np.int64)
        
    for i in temp.filter(regex=("OHX\d\dCTC")):
        temp[i] = temp[i].astype('str') 
    
    dsc = {
        1: 'Complete',
        2: 'Partial',
        3: 'Not done'
    }
    
    temp.dentition_status_code = temp.dentition_status_code.map(
        dsc).fillna('N/A')
    
    tooth_count = {1: 'Primary tooth (deciduous) present',
                    2: 'Permanent tooth present',
                    3: 'Dental Implant',
                    4: 'Tooth not present',
                    5: 'Permanent dental root fragment present',
                    9: 'Could not assess'}
    
    # fill in values and rename
    for column in temp.filter(regex=("OHX\d\dTC")):
        temp[column] = temp[column].map(
        tooth_count).fillna('N/A')
        temp.rename(columns = {column: "tooth count #" + column[3:5]}, inplace = True)
    
    tooth_count_c = {
        "b'D'": "Sound primary tooth",
        "b'E'": "Missing due to dental disease",
        "b'J'": "Permanent root tip is present but no restorative replacement is present",
        "b'K'": "Primary tooth with surface condition",
        "b'M'": "Missing due to other causes",
        "b'P'": "Missing due to dental disease but replaced by a removable restoration",
        "b'Q'": "Missing due to other causes but replaced by a removable restoration",
        "b'R'": "Missing due to dental disease but replaced by a fixed restoration",
        "b'S'": "Sound permanent tooth",
        "b'T'": "Permanent root tip is present but a restorative replacement is present",
        "b'U'": "Unerupted",
        "b'X'": "Missing due to other causes, but replaced by a fixed restoration",
        "b'Y'": "Tooth present, condition cannot be assessed",
        "b'Z'": "Permanent tooth with surface condition"
    }
    
    for column in temp.filter(regex=("OHX\d\dCTC")):
        temp[column] = temp[column].map(
        tooth_count_c).fillna('N/A')
        temp.rename(columns = {column: "coronal caries: tooth count #" + column[3:5]}, inplace = True)
    
    num_oral += temp.shape[0]
    temp.to_pickle("./OHXDEN_" + i + ".pkl")


#c
print("number of cases in the first dataset is: " + str(num_demo))
print("number of cases in the second dataset is: " + str(num_oral))
