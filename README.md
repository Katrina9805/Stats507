# Stats507

This repo is created for the purpose of Stats507 homework.

## [PS2_Q3](./PS2_Q3.py)

ref : https://jbhender.github.io/Stats507/F21/ps/ps2.html

This file uses Pandas to read, clean, and append several data files from the National Health and Nutrition Examination Survey NHANES. It uses the four cohorts spanning the years 2011-2018. 

In part a, it uses Python and Pandas to read and append the demographic datasets keeping only columns containing the unique ids (SEQN), age (RIDAGEYR), race and ethnicity (RIDRETH3), education (DMDEDUC2), and marital status (DMDMARTL), along with the following variables related to the survey weighting: (RIDSTATR, SDMVPSU, SDMVSTRA, WTMEC2YR, WTINT2YR). It adds an additional column identifying to which cohort each case belongs and renames the columns with literate variable names using all lower case and convert each column to an appropriate type. Finally, it saves the resulting data frame to pickle format.

In part b, it repeats part a for the oral health and dentition data and in part c, reports the number of cases there are in the two datasets.


[link to commit history](https://github.com/Katrina9805/Stats507/commits/main)
[link to commit history 2](https://github.com/Katrina9805/Stats507/commits/main)

link to pd_topic_ranyan: [pd_topic_ranyan.py](./pandas_notes/pd_topic_ranyan.py)


Steps:
1. Create the repository in github and clone the repository to desktop by: git clone https://github.com/Katrina9805/Stats507
Part 1
1. create python file for code from PS2, Question 3: git add PS2_Q3.py
1. git commit -a -m "add PS2 description"
1. git push
Part 2
1. git vim README.md
1. git commit -a -m "add local path"
Part 3
1. git commit -a -m "edit link"
1. git push
Part 4
1. git branch ps4
1. git checkout ps4
1. vim PS2_Q3.py
1. git commit -a -m "include variable gender"
1. git push -u origin ps4
1. git checkout main
1. git merge ps4
1. vim README.md 
1. git commit -a -m "Question 1 part 5"
1. git push