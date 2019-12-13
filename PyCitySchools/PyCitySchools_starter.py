#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[ ]:


# Dependencies and Setup
import os
import csv
import pandas as pd
import statistics

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[ ]:


# District Summary


# School Total
school_total = len((school_data_complete["school_name"].unique()))
#print(school_total)

# Student Total
student_total = len((school_data_complete["Student ID"].unique()))
#print(student_total)

# Total Budget
budget_total = sum(school_data["budget"])
#print(budget_total)

# Average Reading and Math Scores
reading_avg = statistics.mean(school_data_complete["reading_score"])
#print(reading_avg)

math_avg = statistics.mean(school_data_complete["math_score"])
#print(math_avg)

# Passing Rate
passing_rate = (reading_avg + math_avg) / 2
#print(passing_rate)

# Passing Reading and Math Student Percentages
passing_reading = (sum((school_data_complete["reading_score"] >= 70)) / student_total) * 100
#print(passing_reading)

passing_math = (sum((school_data_complete["math_score"] >= 70)) / student_total) * 100
#print(passing_math)

# Data Frame of Results
district_summary_df = pd.DataFrame({
    "Total Schools": [school_total],
    "Total Students": [f"{student_total:,}"],
    "Total Budget": [f"${budget_total:,.2f}"],
    "Average Math Score": [f"{math_avg:.2f}"],
    "Average Reading Score": [f"{reading_avg:.2f}"],
    "% Passing Math": [f"{passing_math:.2f}"],
    "% Passing Reading": [f"{passing_reading:.2f}"],
    "% Overall Passing Rate": [f"{passing_rate:.2f}"]
})
district_summary_df


# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# In[ ]:


# School Summary
# print(school_data_complete)

school_summary_df = pd.DataFrame(school_data)
school_summary_df = school_summary_df[["school_name", "type", "size", "budget"]]
school_summary_df.set_index("school_name", inplace=True)
#print(school_summary_df)

#school_summary_df.iat[0,2] /school_summary_df.iat[0,1]

budget_per_student = [(school_summary_df.iat[0,2] / school_summary_df.iat[0,1]),
                      (school_summary_df.iat[1,2] / school_summary_df.iat[1,1]),
                      (school_summary_df.iat[2,2] / school_summary_df.iat[2,1]),
                      (school_summary_df.iat[3,2] / school_summary_df.iat[3,1]),
                      (school_summary_df.iat[4,2] / school_summary_df.iat[4,1]),
                      (school_summary_df.iat[5,2] / school_summary_df.iat[5,1]),
                      (school_summary_df.iat[6,2] / school_summary_df.iat[6,1]),
                      (school_summary_df.iat[7,2] / school_summary_df.iat[7,1]),
                      (school_summary_df.iat[8,2] / school_summary_df.iat[8,1]),
                      (school_summary_df.iat[9,2] / school_summary_df.iat[9,1]),
                     (school_summary_df.iat[10,2] / school_summary_df.iat[10,1]),
                     (school_summary_df.iat[11,2] / school_summary_df.iat[11,1]),
                     (school_summary_df.iat[12,2] / school_summary_df.iat[12,1]),
                     (school_summary_df.iat[13,2] / school_summary_df.iat[13,1]),
                     (school_summary_df.iat[14,2] / school_summary_df.iat[14,1])]
#print(budget_per_student)
school_summary_df['Per Student Budget'] = budget_per_student 

#school_data_complete[{"school_name"}]
school_summary_df

school_summary_df = school_summary_df.rename(columns={'type': 'School Type',
                                                      'budget' : 'School Total Budget',
                                                      'size' : 'Size'})
school_summary_df.index.names = ['Name of School']


# In[ ]:


# Individual High School Metrics


##################################
# Huang High School
Huang_data = school_data_complete[school_data_complete.school_name == "Huang High School"]

Huang_student_total = len((Huang_data["Student ID"].unique()))

# Average Reading and Math Scores
Huang_reading_avg = statistics.mean(Huang_data["reading_score"])

Huang_math_avg = statistics.mean(Huang_data["math_score"])

# Passing Rate
Huang_passing_rate = (Huang_reading_avg + Huang_math_avg) / 2

# Passing Reading and Math Student Percentages
Huang_passing_reading = (sum((Huang_data["reading_score"] >= 70)) / Huang_student_total) * 100

Huang_passing_math = (sum((Huang_data["math_score"] >= 70)) / Huang_student_total) * 100

########################################
# Figueroa High School
Figueroa_data = school_data_complete[school_data_complete.school_name == "Figueroa High School"]

Figueroa_student_total = len((Figueroa_data["Student ID"].unique()))

# Average Reading and Math Scores
Figueroa_reading_avg = statistics.mean(Figueroa_data["reading_score"])

Figueroa_math_avg = statistics.mean(Figueroa_data["math_score"])

# Passing Rate
Figueroa_passing_rate = (Figueroa_reading_avg +Figueroa_math_avg) / 2

# Passing Reading and Math Student Percentages
Figueroa_passing_reading = (sum((Figueroa_data["reading_score"] >= 70)) /Figueroa_student_total) * 100

Figueroa_passing_math = (sum((Figueroa_data["math_score"] >= 70)) /Figueroa_student_total) * 100

######################
# Shelton High School
Shelton_data = school_data_complete[school_data_complete.school_name == "Shelton High School"]

Shelton_student_total = len((Shelton_data["Student ID"].unique()))

# Average Reading and Math Scores
Shelton_reading_avg = statistics.mean(Shelton_data["reading_score"])

Shelton_math_avg = statistics.mean(Shelton_data["math_score"])

# Passing Rate
Shelton_passing_rate = (Shelton_reading_avg +Shelton_math_avg) / 2

# Passing Reading and Math Student Percentages
Shelton_passing_reading = (sum((Shelton_data["reading_score"] >= 70)) /Shelton_student_total) * 100

Shelton_passing_math = (sum((Shelton_data["math_score"] >= 70)) /Shelton_student_total) * 100

###########################
# Hernandez High School
Hernandez_data = school_data_complete[school_data_complete.school_name == "Hernandez High School"]

Hernandez_student_total = len((Hernandez_data["Student ID"].unique()))

# Average Reading and Math Scores
Hernandez_reading_avg = statistics.mean(Hernandez_data["reading_score"])

Hernandez_math_avg = statistics.mean(Hernandez_data["math_score"])

# Passing Rate
Hernandez_passing_rate = (Hernandez_reading_avg +Hernandez_math_avg) / 2

# Passing Reading and Math Student Percentages
Hernandez_passing_reading = (sum((Hernandez_data["reading_score"] >= 70)) /Hernandez_student_total) * 100

Hernandez_passing_math = (sum((Hernandez_data["math_score"] >= 70)) /Hernandez_student_total) * 100

###############################
# Griffin High School
Griffin_data = school_data_complete[school_data_complete.school_name == "Griffin High School"]

Griffin_student_total = len((Griffin_data["Student ID"].unique()))

# Average Reading and Math Scores
Griffin_reading_avg = statistics.mean(Griffin_data["reading_score"])

Griffin_math_avg = statistics.mean(Griffin_data["math_score"])

# Passing Rate
Griffin_passing_rate = (Griffin_reading_avg +Griffin_math_avg) / 2

# Passing Reading and Math Student Percentages
Griffin_passing_reading = (sum((Griffin_data["reading_score"] >= 70)) /Griffin_student_total) * 100

Griffin_passing_math = (sum((Griffin_data["math_score"] >= 70)) /Griffin_student_total) * 100

##################################
# Wilson High School
Wilson_data = school_data_complete[school_data_complete.school_name == "Wilson High School"]

Wilson_student_total = len((Wilson_data["Student ID"].unique()))

# Average Reading and Math Scores
Wilson_reading_avg = statistics.mean(Wilson_data["reading_score"])

Wilson_math_avg = statistics.mean(Wilson_data["math_score"])

# Passing Rate
Wilson_passing_rate = (Wilson_reading_avg +Wilson_math_avg) / 2

# Passing Reading and Math Student Percentages
Wilson_passing_reading = (sum((Wilson_data["reading_score"] >= 70)) /Wilson_student_total) * 100

Wilson_passing_math = (sum((Wilson_data["math_score"] >= 70)) /Wilson_student_total) * 100

##############################
# Cabrera High School
Cabrera_data = school_data_complete[school_data_complete.school_name == "Cabrera High School"]

Cabrera_student_total = len((Cabrera_data["Student ID"].unique()))

# Average Reading and Math Scores
Cabrera_reading_avg = statistics.mean(Cabrera_data["reading_score"])

Cabrera_math_avg = statistics.mean(Cabrera_data["math_score"])

# Passing Rate
Cabrera_passing_rate = (Cabrera_reading_avg +Cabrera_math_avg) / 2

# Passing Reading and Math Student Percentages
Cabrera_passing_reading = (sum((Cabrera_data["reading_score"] >= 70)) /Cabrera_student_total) * 100

Cabrera_passing_math = (sum((Cabrera_data["math_score"] >= 70)) /Cabrera_student_total) * 100

###########################
# Bailey High School
Bailey_data = school_data_complete[school_data_complete.school_name == "Bailey High School"]

Bailey_student_total = len((Bailey_data["Student ID"].unique()))

# Average Reading and Math Scores
Bailey_reading_avg = statistics.mean(Bailey_data["reading_score"])

Bailey_math_avg = statistics.mean(Bailey_data["math_score"])

# Passing Rate
Bailey_passing_rate = (Bailey_reading_avg +Bailey_math_avg) / 2

# Passing Reading and Math Student Percentages
Bailey_passing_reading = (sum((Bailey_data["reading_score"] >= 70)) /Bailey_student_total) * 100

Bailey_passing_math = (sum((Bailey_data["math_score"] >= 70)) /Bailey_student_total) * 100

##############################
# Holden High School
Holden_data = school_data_complete[school_data_complete.school_name == "Holden High School"]

Holden_student_total = len((Holden_data["Student ID"].unique()))

# Average Reading and Math Scores
Holden_reading_avg = statistics.mean(Holden_data["reading_score"])

Holden_math_avg = statistics.mean(Holden_data["math_score"])

# Passing Rate
Holden_passing_rate = (Holden_reading_avg +Holden_math_avg) / 2

# Passing Reading and Math Student Percentages
Holden_passing_reading = (sum((Holden_data["reading_score"] >= 70)) /Holden_student_total) * 100

Holden_passing_math = (sum((Holden_data["math_score"] >= 70)) /Holden_student_total) * 100

#########################
# Pena High School
Pena_data = school_data_complete[school_data_complete.school_name == "Pena High School"]

Pena_student_total = len((Pena_data["Student ID"].unique()))

# Average Reading and Math Scores
Pena_reading_avg = statistics.mean(Pena_data["reading_score"])

Pena_math_avg = statistics.mean(Pena_data["math_score"])

# Passing Rate
Pena_passing_rate = (Pena_reading_avg +Pena_math_avg) / 2

# Passing Reading and Math Student Percentages
Pena_passing_reading = (sum((Pena_data["reading_score"] >= 70)) /Pena_student_total) * 100

Pena_passing_math = (sum((Pena_data["math_score"] >= 70)) /Pena_student_total) * 100

##############################
# Wright High School
Wright_data = school_data_complete[school_data_complete.school_name == "Wright High School"]

Wright_student_total = len((Wright_data["Student ID"].unique()))

# Average Reading and Math Scores
Wright_reading_avg = statistics.mean(Wright_data["reading_score"])

Wright_math_avg = statistics.mean(Wright_data["math_score"])

# Passing Rate
Wright_passing_rate = (Wright_reading_avg +Wright_math_avg) / 2

# Passing Reading and Math Student Percentages
Wright_passing_reading = (sum((Wright_data["reading_score"] >= 70)) /Wright_student_total) * 100

Wright_passing_math = (sum((Wright_data["math_score"] >= 70)) /Wright_student_total) * 100

###################################
# Rodriguez High School
Rodriguez_data = school_data_complete[school_data_complete.school_name == "Rodriguez High School"]

Rodriguez_student_total = len((Rodriguez_data["Student ID"].unique()))

# Average Reading and Math Scores
Rodriguez_reading_avg = statistics.mean(Rodriguez_data["reading_score"])

Rodriguez_math_avg = statistics.mean(Rodriguez_data["math_score"])

# Passing Rate
Rodriguez_passing_rate = (Rodriguez_reading_avg +Rodriguez_math_avg) / 2

# Passing Reading and Math Student Percentages
Rodriguez_passing_reading = (sum((Rodriguez_data["reading_score"] >= 70)) /Rodriguez_student_total) * 100

Rodriguez_passing_math = (sum((Rodriguez_data["math_score"] >= 70)) /Rodriguez_student_total) * 100

##########################
# Johnson High School
Johnson_data = school_data_complete[school_data_complete.school_name == "Johnson High School"]

Johnson_student_total = len((Johnson_data["Student ID"].unique()))

# Average Reading and Math Scores
Johnson_reading_avg = statistics.mean(Johnson_data["reading_score"])

Johnson_math_avg = statistics.mean(Johnson_data["math_score"])

# Passing Rate
Johnson_passing_rate = (Johnson_reading_avg +Johnson_math_avg) / 2

# Passing Reading and Math Student Percentages
Johnson_passing_reading = (sum((Johnson_data["reading_score"] >= 70)) /Johnson_student_total) * 100

Johnson_passing_math = (sum((Johnson_data["math_score"] >= 70)) /Johnson_student_total) * 100

#################################
# Ford High School
Ford_data = school_data_complete[school_data_complete.school_name == "Ford High School"]

Ford_student_total = len((Ford_data["Student ID"].unique()))

# Average Reading and Math Scores
Ford_reading_avg = statistics.mean(Ford_data["reading_score"])

Ford_math_avg = statistics.mean(Ford_data["math_score"])

# Passing Rate
Ford_passing_rate = (Ford_reading_avg +Ford_math_avg) / 2

# Passing Reading and Math Student Percentages
Ford_passing_reading = (sum((Ford_data["reading_score"] >= 70)) /Ford_student_total) * 100

Ford_passing_math = (sum((Ford_data["math_score"] >= 70)) /Ford_student_total) * 100

###############################
# Thomas High School
Thomas_data = school_data_complete[school_data_complete.school_name == "Thomas High School"]

Thomas_student_total = len((Thomas_data["Student ID"].unique()))

# Average Reading and Math Scores
Thomas_reading_avg = statistics.mean(Thomas_data["reading_score"])

Thomas_math_avg = statistics.mean(Thomas_data["math_score"])

# Passing Rate
Thomas_passing_rate = (Thomas_reading_avg +Thomas_math_avg) / 2

# Passing Reading and Math Student Percentages
Thomas_passing_reading = (sum((Thomas_data["reading_score"] >= 70)) /Thomas_student_total) * 100

Thomas_passing_math = (sum((Thomas_data["math_score"] >= 70)) /Thomas_student_total) * 100


# In[ ]:


# Constructing School Summary Data Frame
school_summary_df

# Average Math Scores
schools_math_df = [Huang_math_avg,Figueroa_math_avg,
                                         Shelton_math_avg,Hernandez_math_avg,
                                         Griffin_math_avg,Wilson_math_avg,
                                         Cabrera_math_avg,Bailey_math_avg,
                                         Holden_math_avg,Pena_math_avg,
                                         Wright_math_avg,Rodriguez_math_avg,
                                         Johnson_math_avg,Ford_math_avg,
                                         Thomas_math_avg]
schools_math_df
#school_summary_df["Average Math Score"] = schools_math_df
school_summary_df

# Average reading Scores
schools_reading_df = [Huang_reading_avg,Figueroa_reading_avg,
                                         Shelton_reading_avg,Hernandez_reading_avg,
                                         Griffin_reading_avg,Wilson_reading_avg,
                                         Cabrera_reading_avg,Bailey_reading_avg,
                                         Holden_reading_avg,Pena_reading_avg,
                                         Wright_reading_avg,Rodriguez_reading_avg,
                                         Johnson_reading_avg,Ford_reading_avg,
                                         Thomas_reading_avg]
schools_reading_df
school_summary_df["Average Math Score"] = schools_math_df
school_summary_df["Average Reading Score"] = schools_reading_df
#school_summary_df.drop(['Average reading Score'], axis=1)
school_summary_df


# In[ ]:


### School Passing Rates

### Huang High School
# Passing Rate
Huang_passing_rate = (Huang_reading_avg + Huang_math_avg) / 2
print(Huang_passing_rate)

# Passing Reading and Math Student Percentages
Huang_passing_reading = (sum((Huang_data["reading_score"] >= 70)) / len(Huang_data)) * 100

Huang_passing_math = (sum((Huang_data["math_score"] >= 70)) / len(Huang_data)) * 100


### Figueroa High School
# Passing Rate
Figueroa_passing_rate = (Figueroa_reading_avg + Figueroa_math_avg) / 2


# Passing Reading and Math Student Percentages
Figueroa_passing_reading = (sum((Figueroa_data["reading_score"] >= 70)) / len(Figueroa_data)) * 100


Figueroa_passing_math = (sum((Figueroa_data["math_score"] >= 70)) / len(Figueroa_data)) * 100


### Shelton High School
# Passing Rate
Shelton_passing_rate = (Shelton_reading_avg + Shelton_math_avg) / 2


# Passing Reading and Math Student Percentages
Shelton_passing_reading = (sum((Shelton_data["reading_score"] >= 70)) / len(Shelton_data)) * 100


Shelton_passing_math = (sum((Shelton_data["math_score"] >= 70)) / len(Shelton_data)) * 100


### Hernandez High School
# Passing Rate
Hernandez_passing_rate = (Hernandez_reading_avg + Hernandez_math_avg) / 2

# Passing Reading and Math Student Percentages
Hernandez_passing_reading = (sum((Hernandez_data["reading_score"] >= 70)) / len(Hernandez_data)) * 100

Hernandez_passing_math = (sum((Hernandez_data["math_score"] >= 70)) / len(Hernandez_data)) * 100


### Griffin High School
# Passing Rate
Griffin_passing_rate = (Griffin_reading_avg + Griffin_math_avg) / 2


# Passing Reading and Math Student Percentages
Griffin_passing_reading = (sum((Griffin_data["reading_score"] >= 70)) / len(Griffin_data)) * 100


Griffin_passing_math = (sum((Griffin_data["math_score"] >= 70)) / len(Griffin_data)) * 100


### Wilson High School
# Passing Rate
Wilson_passing_rate = (Wilson_reading_avg + Wilson_math_avg) / 2

# Passing Reading and Math Student Percentages
Wilson_passing_reading = (sum((Wilson_data["reading_score"] >= 70)) / len(Wilson_data)) * 100

Wilson_passing_math = (sum((Wilson_data["math_score"] >= 70)) / len(Wilson_data)) * 100

### Cabrera High School
# Passing Rate
Cabrera_passing_rate = (Cabrera_reading_avg + Cabrera_math_avg) / 2

# Passing Reading and Math Student Percentages
Cabrera_passing_reading = (sum((Cabrera_data["reading_score"] >= 70)) / len(Cabrera_data)) * 100

Cabrera_passing_math = (sum((Cabrera_data["math_score"] >= 70)) / len(Cabrera_data)) * 100

### Bailey High School
# Passing Rate
Bailey_passing_rate = (Bailey_reading_avg + Bailey_math_avg) / 2

# Passing Reading and Math Student Percentages
Bailey_passing_reading = (sum((Bailey_data["reading_score"] >= 70)) / len(Bailey_data)) * 100

Bailey_passing_math = (sum((Bailey_data["math_score"] >= 70)) / len(Bailey_data)) * 100

### Holden High School
# Passing Rate
Holden_passing_rate = (Holden_reading_avg + Holden_math_avg) / 2

# Passing Reading and Math Student Percentages
Holden_passing_reading = (sum((Holden_data["reading_score"] >= 70)) / len(Holden_data)) * 100

Holden_passing_math = (sum((Holden_data["math_score"] >= 70)) / len(Holden_data)) * 100

### Pena High School
# Passing Rate
Pena_passing_rate = (Pena_reading_avg + Pena_math_avg) / 2

# Passing Reading and Math Student Percentages
Pena_passing_reading = (sum((Pena_data["reading_score"] >= 70)) / len(Pena_data)) * 100

Pena_passing_math = (sum((Pena_data["math_score"] >= 70)) / len(Pena_data)) * 100

### Wright High School
# Passing Rate
Wright_passing_rate = (Wright_reading_avg + Wright_math_avg) / 2

# Passing Reading and Math Student Percentages
Wright_passing_reading = (sum((Wright_data["reading_score"] >= 70)) / len(Wright_data)) * 100

Wright_passing_math = (sum((Wright_data["math_score"] >= 70)) / len(Wright_data)) * 100

### Rodriguez High School
# Passing Rate
Rodriguez_passing_rate = (Rodriguez_reading_avg + Rodriguez_math_avg) / 2

# Passing Reading and Math Student Percentages
Rodriguez_passing_reading = (sum((Rodriguez_data["reading_score"] >= 70)) / len(Rodriguez_data)) * 100

Rodriguez_passing_math = (sum((Rodriguez_data["math_score"] >= 70)) / len(Rodriguez_data)) * 100

### Johnson High School
# Passing Rate
Johnson_passing_rate = (Johnson_reading_avg + Johnson_math_avg) / 2

# Passing Reading and Math Student Percentages
Johnson_passing_reading = (sum((Johnson_data["reading_score"] >= 70)) / len(Johnson_data)) * 100

Johnson_passing_math = (sum((Johnson_data["math_score"] >= 70)) / len(Johnson_data)) * 100

### Ford High School
# Passing Rate
Ford_passing_rate = (Ford_reading_avg + Ford_math_avg) / 2

# Passing Reading and Math Student Percentages
Ford_passing_reading = (sum((Ford_data["reading_score"] >= 70)) / len(Ford_data)) * 100

Ford_passing_math = (sum((Ford_data["math_score"] >= 70)) / len(Ford_data)) * 100

### Thomas High School
# Passing Rate
Thomas_passing_rate = (Thomas_reading_avg + Thomas_math_avg) / 2

# Passing Reading and Math Student Percentages
Thomas_passing_reading = (sum((Thomas_data["reading_score"] >= 70)) / len(Thomas_data)) * 100

Thomas_passing_math = (sum((Thomas_data["math_score"] >= 70)) / len(Thomas_data)) * 100


# In[ ]:


# % Passing Math
schools_passing_math_df = [Huang_passing_math,Figueroa_passing_math,
                                         Shelton_passing_math,Hernandez_passing_math,
                                         Griffin_passing_math,Wilson_passing_math,
                                         Cabrera_passing_math,Bailey_passing_math,
                                         Holden_passing_math,Pena_passing_math,
                                         Wright_passing_math,Rodriguez_passing_math,
                                         Johnson_passing_math,Ford_passing_math,
                                         Thomas_passing_math]

# % Passing Reading
schools_passing_reading_df = [Huang_passing_reading,Figueroa_passing_reading,
                                         Shelton_passing_reading,Hernandez_passing_reading,
                                         Griffin_passing_reading,Wilson_passing_reading,
                                         Cabrera_passing_reading,Bailey_passing_reading,
                                         Holden_passing_reading,Pena_passing_reading,
                                         Wright_passing_reading,Rodriguez_passing_reading,
                                         Johnson_passing_reading,Ford_passing_reading,
                                         Thomas_passing_reading]

# % Overall Passing Rate
schools_passing_rate_df = [Huang_passing_rate,Figueroa_passing_rate,
                                         Shelton_passing_rate,Hernandez_passing_rate,
                                         Griffin_passing_rate,Wilson_passing_rate,
                                         Cabrera_passing_rate,Bailey_passing_rate,
                                         Holden_passing_rate,Pena_passing_rate,
                                         Wright_passing_rate,Rodriguez_passing_rate,
                                         Johnson_passing_rate,Ford_passing_rate,
                                         Thomas_passing_rate]
#print(schools_passing_math_df)
#schools_passing_reading_df
school_summary_df["% Passing Math"] = schools_passing_math_df
school_summary_df["% Passing Reading"] = schools_passing_reading_df
school_summary_df["% Overall Passing Rate"] = schools_passing_rate_df
school_summary_df


# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[ ]:


top_passing = school_summary_df.sort_values("% Overall Passing Rate", ascending=False)
top_passing.head(5)


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[ ]:


bottom_passing = school_summary_df.sort_values("% Overall Passing Rate", ascending=True)
bottom_passing.head(5)


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[ ]:


######### Huang High School math Average By Grade

Huang_9 = Huang_data.loc[Huang_data['grade'] == '9th'] 
Huang_9_mavg = statistics.mean(Huang_9["math_score"])

Huang_10 = Huang_data.loc[Huang_data['grade'] == '10th'] 
Huang_10_mavg = statistics.mean(Huang_10["math_score"])

Huang_11 = Huang_data.loc[Huang_data['grade'] == '11th'] 
Huang_11_mavg = statistics.mean(Huang_11["math_score"])

Huang_12 = Huang_data.loc[Huang_data['grade'] == '12th'] 
Huang_12_mavg = statistics.mean(Huang_12["math_score"])

######### Figueroa High School math Average By Grade

Figueroa_9 = Figueroa_data.loc[Figueroa_data['grade'] == '9th'] 
Figueroa_9_mavg = statistics.mean(Figueroa_9["math_score"])

Figueroa_10 = Figueroa_data.loc[Figueroa_data['grade'] == '10th'] 
Figueroa_10_mavg = statistics.mean(Figueroa_10["math_score"])

Figueroa_11 = Figueroa_data.loc[Figueroa_data['grade'] == '11th'] 
Figueroa_11_mavg = statistics.mean(Figueroa_11["math_score"])

Figueroa_12 = Figueroa_data.loc[Figueroa_data['grade'] == '12th'] 
Figueroa_12_mavg = statistics.mean(Figueroa_12["math_score"])

######### Shelton High School math Average By Grade

Shelton_9 = Shelton_data.loc[Shelton_data['grade'] == '9th'] 
Shelton_9_mavg = statistics.mean(Shelton_9["math_score"])

Shelton_10 = Shelton_data.loc[Shelton_data['grade'] == '10th'] 
Shelton_10_mavg = statistics.mean(Shelton_10["math_score"])

Shelton_11 = Shelton_data.loc[Shelton_data['grade'] == '11th'] 
Shelton_11_mavg = statistics.mean(Shelton_11["math_score"])

Shelton_12 = Shelton_data.loc[Shelton_data['grade'] == '12th'] 
Shelton_12_mavg = statistics.mean(Shelton_12["math_score"])

######### Hernandez High School math Average By Grade

Hernandez_9 = Hernandez_data.loc[Hernandez_data['grade'] == '9th'] 
Hernandez_9_mavg = statistics.mean(Hernandez_9["math_score"])

Hernandez_10 = Hernandez_data.loc[Hernandez_data['grade'] == '10th'] 
Hernandez_10_mavg = statistics.mean(Hernandez_10["math_score"])

Hernandez_11 = Hernandez_data.loc[Hernandez_data['grade'] == '11th'] 
Hernandez_11_mavg = statistics.mean(Hernandez_11["math_score"])

Hernandez_12 = Hernandez_data.loc[Hernandez_data['grade'] == '12th'] 
Hernandez_12_mavg = statistics.mean(Hernandez_12["math_score"])

######### Griffin High School math Average By Grade

Griffin_9 = Griffin_data.loc[Griffin_data['grade'] == '9th'] 
Griffin_9_mavg = statistics.mean(Griffin_9["math_score"])

Griffin_10 = Griffin_data.loc[Griffin_data['grade'] == '10th'] 
Griffin_10_mavg = statistics.mean(Griffin_10["math_score"])

Griffin_11 = Griffin_data.loc[Griffin_data['grade'] == '11th'] 
Griffin_11_mavg = statistics.mean(Griffin_11["math_score"])

Griffin_12 = Griffin_data.loc[Griffin_data['grade'] == '12th'] 
Griffin_12_mavg = statistics.mean(Griffin_12["math_score"])

######### Wilson High School math Average By Grade

Wilson_9 = Wilson_data.loc[Wilson_data['grade'] == '9th'] 
Wilson_9_mavg = statistics.mean(Wilson_9["math_score"])

Wilson_10 = Wilson_data.loc[Wilson_data['grade'] == '10th'] 
Wilson_10_mavg = statistics.mean(Wilson_10["math_score"])

Wilson_11 = Wilson_data.loc[Wilson_data['grade'] == '11th'] 
Wilson_11_mavg = statistics.mean(Wilson_11["math_score"])

Wilson_12 = Wilson_data.loc[Wilson_data['grade'] == '12th'] 
Wilson_12_mavg = statistics.mean(Wilson_12["math_score"])


######### Cabrera High School math Average By Grade

Cabrera_9 = Cabrera_data.loc[Cabrera_data['grade'] == '9th'] 
Cabrera_9_mavg = statistics.mean(Cabrera_9["math_score"])

Cabrera_10 = Cabrera_data.loc[Cabrera_data['grade'] == '10th'] 
Cabrera_10_mavg = statistics.mean(Cabrera_10["math_score"])

Cabrera_11 = Cabrera_data.loc[Cabrera_data['grade'] == '11th'] 
Cabrera_11_mavg = statistics.mean(Cabrera_11["math_score"])

Cabrera_12 = Cabrera_data.loc[Cabrera_data['grade'] == '12th'] 
Cabrera_12_mavg = statistics.mean(Cabrera_12["math_score"])


######### Bailey High School math Average By Grade

Bailey_9 = Bailey_data.loc[Bailey_data['grade'] == '9th'] 
Bailey_9_mavg = statistics.mean(Bailey_9["math_score"])

Bailey_10 = Bailey_data.loc[Bailey_data['grade'] == '10th'] 
Bailey_10_mavg = statistics.mean(Bailey_10["math_score"])

Bailey_11 = Bailey_data.loc[Bailey_data['grade'] == '11th'] 
Bailey_11_mavg = statistics.mean(Bailey_11["math_score"])

Bailey_12 = Bailey_data.loc[Bailey_data['grade'] == '12th'] 
Bailey_12_mavg = statistics.mean(Bailey_12["math_score"])


######### Holden High School math Average By Grade

Holden_9 = Holden_data.loc[Holden_data['grade'] == '9th'] 
Holden_9_mavg = statistics.mean(Holden_9["math_score"])

Holden_10 = Holden_data.loc[Holden_data['grade'] == '10th'] 
Holden_10_mavg = statistics.mean(Holden_10["math_score"])

Holden_11 = Holden_data.loc[Holden_data['grade'] == '11th'] 
Holden_11_mavg = statistics.mean(Holden_11["math_score"])

Holden_12 = Holden_data.loc[Holden_data['grade'] == '12th'] 
Holden_12_mavg = statistics.mean(Holden_12["math_score"])


######### Pena High School math Average By Grade

Pena_9 = Pena_data.loc[Pena_data['grade'] == '9th'] 
Pena_9_mavg = statistics.mean(Pena_9["math_score"])

Pena_10 = Pena_data.loc[Pena_data['grade'] == '10th'] 
Pena_10_mavg = statistics.mean(Pena_10["math_score"])

Pena_11 = Pena_data.loc[Pena_data['grade'] == '11th'] 
Pena_11_mavg = statistics.mean(Pena_11["math_score"])

Pena_12 = Pena_data.loc[Pena_data['grade'] == '12th'] 
Pena_12_mavg = statistics.mean(Pena_12["math_score"])


######### Wright High School math Average By Grade

Wright_9 = Wright_data.loc[Wright_data['grade'] == '9th'] 
Wright_9_mavg = statistics.mean(Wright_9["math_score"])

Wright_10 = Wright_data.loc[Wright_data['grade'] == '10th'] 
Wright_10_mavg = statistics.mean(Wright_10["math_score"])

Wright_11 = Wright_data.loc[Wright_data['grade'] == '11th'] 
Wright_11_mavg = statistics.mean(Wright_11["math_score"])

Wright_12 = Wright_data.loc[Wright_data['grade'] == '12th'] 
Wright_12_mavg = statistics.mean(Wright_12["math_score"])

######### Rodriguez High School math Average By Grade

Rodriguez_9 = Rodriguez_data.loc[Rodriguez_data['grade'] == '9th'] 
Rodriguez_9_mavg = statistics.mean(Rodriguez_9["math_score"])

Rodriguez_10 = Rodriguez_data.loc[Rodriguez_data['grade'] == '10th'] 
Rodriguez_10_mavg = statistics.mean(Rodriguez_10["math_score"])

Rodriguez_11 = Rodriguez_data.loc[Rodriguez_data['grade'] == '11th'] 
Rodriguez_11_mavg = statistics.mean(Rodriguez_11["math_score"])

Rodriguez_12 = Rodriguez_data.loc[Rodriguez_data['grade'] == '12th'] 
Rodriguez_12_mavg = statistics.mean(Rodriguez_12["math_score"])


######### Johnson High School math Average By Grade

Johnson_9 = Johnson_data.loc[Johnson_data['grade'] == '9th'] 
Johnson_9_mavg = statistics.mean(Johnson_9["math_score"])

Johnson_10 = Johnson_data.loc[Johnson_data['grade'] == '10th'] 
Johnson_10_mavg = statistics.mean(Johnson_10["math_score"])

Johnson_11 = Johnson_data.loc[Johnson_data['grade'] == '11th'] 
Johnson_11_mavg = statistics.mean(Johnson_11["math_score"])

Johnson_12 = Johnson_data.loc[Johnson_data['grade'] == '12th'] 
Johnson_12_mavg = statistics.mean(Johnson_12["math_score"])


######### Ford High School math Average By Grade

Ford_9 = Ford_data.loc[Ford_data['grade'] == '9th'] 
Ford_9_mavg = statistics.mean(Ford_9["math_score"])

Ford_10 = Ford_data.loc[Ford_data['grade'] == '10th'] 
Ford_10_mavg = statistics.mean(Ford_10["math_score"])

Ford_11 = Ford_data.loc[Ford_data['grade'] == '11th'] 
Ford_11_mavg = statistics.mean(Ford_11["math_score"])

Ford_12 = Ford_data.loc[Ford_data['grade'] == '12th'] 
Ford_12_mavg = statistics.mean(Ford_12["math_score"])


######### Thomas High School math Average By Grade

Thomas_9 = Thomas_data.loc[Thomas_data['grade'] == '9th'] 
Thomas_9_mavg = statistics.mean(Thomas_9["math_score"])

Thomas_10 = Thomas_data.loc[Thomas_data['grade'] == '10th'] 
Thomas_10_mavg = statistics.mean(Thomas_10["math_score"])

Thomas_11 = Thomas_data.loc[Thomas_data['grade'] == '11th'] 
Thomas_11_mavg = statistics.mean(Thomas_11["math_score"])

Thomas_12 = Thomas_data.loc[Thomas_data['grade'] == '12th'] 
Thomas_12_mavg = statistics.mean(Thomas_12["math_score"])







# In[ ]:


math_avg_by_grade = {'School Name': ['Huang High School','Figueroa High School',
                    'Shelton High School','Hernandez High School','Griffin High School','Wilson High School',
                    'Cabrera High School','Bailey High School','Holden High School',     
                    'Pena High School','Wright High School','Rodriguez High School',
                    'Johnson High School','Ford High School','Thomas High School'],
                    '9th': [Huang_9_mavg,Figueroa_9_mavg,Shelton_9_mavg,Hernandez_9_mavg,
                    Griffin_9_mavg,Wilson_9_mavg,Cabrera_9_mavg,Bailey_9_mavg,Holden_9_mavg,
                    Pena_9_mavg,Wright_9_mavg,Rodriguez_9_mavg,Johnson_9_mavg,Ford_9_mavg,Thomas_9_mavg], 
                    '10th': [Huang_10_mavg,Figueroa_10_mavg,Shelton_10_mavg,Hernandez_10_mavg,
                    Griffin_10_mavg,Wilson_10_mavg,Cabrera_10_mavg,Bailey_10_mavg,Holden_10_mavg,
                    Pena_10_mavg,Wright_10_mavg,Rodriguez_10_mavg,Johnson_10_mavg,Ford_10_mavg,Thomas_10_mavg], 
                    '11th': [Huang_11_mavg,Figueroa_11_mavg,Shelton_11_mavg,Hernandez_11_mavg,
                    Griffin_11_mavg,Wilson_11_mavg,Cabrera_11_mavg,Bailey_11_mavg,Holden_11_mavg,
                    Pena_11_mavg,Wright_11_mavg,Rodriguez_11_mavg,Johnson_11_mavg,Ford_11_mavg,Thomas_11_mavg],
                    '12th': [Huang_12_mavg,Figueroa_12_mavg,Shelton_12_mavg,Hernandez_12_mavg,
                    Griffin_12_mavg,Wilson_12_mavg,Cabrera_12_mavg,Bailey_12_mavg,Holden_12_mavg,
                    Pena_12_mavg,Wright_12_mavg,Rodriguez_12_mavg,Johnson_12_mavg,Ford_12_mavg,Thomas_12_mavg]}

math_avg_by_grade_df = pd.DataFrame(math_avg_by_grade)                   
                                        
math_avg_by_grade_df


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[ ]:


######### Huang High School Reading Average By Grade

Huang_9 = Huang_data.loc[Huang_data['grade'] == '9th'] 
Huang_9_ravg = statistics.mean(Huang_9["reading_score"])

Huang_10 = Huang_data.loc[Huang_data['grade'] == '10th'] 
Huang_10_ravg = statistics.mean(Huang_10["reading_score"])

Huang_11 = Huang_data.loc[Huang_data['grade'] == '11th'] 
Huang_11_ravg = statistics.mean(Huang_11["reading_score"])

Huang_12 = Huang_data.loc[Huang_data['grade'] == '12th'] 
Huang_12_ravg = statistics.mean(Huang_12["reading_score"])

######### Figueroa High School Reading Average By Grade

Figueroa_9 = Figueroa_data.loc[Figueroa_data['grade'] == '9th'] 
Figueroa_9_ravg = statistics.mean(Figueroa_9["reading_score"])

Figueroa_10 = Figueroa_data.loc[Figueroa_data['grade'] == '10th'] 
Figueroa_10_ravg = statistics.mean(Figueroa_10["reading_score"])

Figueroa_11 = Figueroa_data.loc[Figueroa_data['grade'] == '11th'] 
Figueroa_11_ravg = statistics.mean(Figueroa_11["reading_score"])

Figueroa_12 = Figueroa_data.loc[Figueroa_data['grade'] == '12th'] 
Figueroa_12_ravg = statistics.mean(Figueroa_12["reading_score"])

######### Shelton High School Reading Average By Grade

Shelton_9 = Shelton_data.loc[Shelton_data['grade'] == '9th'] 
Shelton_9_ravg = statistics.mean(Shelton_9["reading_score"])

Shelton_10 = Shelton_data.loc[Shelton_data['grade'] == '10th'] 
Shelton_10_ravg = statistics.mean(Shelton_10["reading_score"])

Shelton_11 = Shelton_data.loc[Shelton_data['grade'] == '11th'] 
Shelton_11_ravg = statistics.mean(Shelton_11["reading_score"])

Shelton_12 = Shelton_data.loc[Shelton_data['grade'] == '12th'] 
Shelton_12_ravg = statistics.mean(Shelton_12["reading_score"])

######### Hernandez High School Reading Average By Grade

Hernandez_9 = Hernandez_data.loc[Hernandez_data['grade'] == '9th'] 
Hernandez_9_ravg = statistics.mean(Hernandez_9["reading_score"])

Hernandez_10 = Hernandez_data.loc[Hernandez_data['grade'] == '10th'] 
Hernandez_10_ravg = statistics.mean(Hernandez_10["reading_score"])

Hernandez_11 = Hernandez_data.loc[Hernandez_data['grade'] == '11th'] 
Hernandez_11_ravg = statistics.mean(Hernandez_11["reading_score"])

Hernandez_12 = Hernandez_data.loc[Hernandez_data['grade'] == '12th'] 
Hernandez_12_ravg = statistics.mean(Hernandez_12["reading_score"])

######### Griffin High School Reading Average By Grade

Griffin_9 = Griffin_data.loc[Griffin_data['grade'] == '9th'] 
Griffin_9_ravg = statistics.mean(Griffin_9["reading_score"])

Griffin_10 = Griffin_data.loc[Griffin_data['grade'] == '10th'] 
Griffin_10_ravg = statistics.mean(Griffin_10["reading_score"])

Griffin_11 = Griffin_data.loc[Griffin_data['grade'] == '11th'] 
Griffin_11_ravg = statistics.mean(Griffin_11["reading_score"])

Griffin_12 = Griffin_data.loc[Griffin_data['grade'] == '12th'] 
Griffin_12_ravg = statistics.mean(Griffin_12["reading_score"])

######### Wilson High School Reading Average By Grade

Wilson_9 = Wilson_data.loc[Wilson_data['grade'] == '9th'] 
Wilson_9_ravg = statistics.mean(Wilson_9["reading_score"])

Wilson_10 = Wilson_data.loc[Wilson_data['grade'] == '10th'] 
Wilson_10_ravg = statistics.mean(Wilson_10["reading_score"])

Wilson_11 = Wilson_data.loc[Wilson_data['grade'] == '11th'] 
Wilson_11_ravg = statistics.mean(Wilson_11["reading_score"])

Wilson_12 = Wilson_data.loc[Wilson_data['grade'] == '12th'] 
Wilson_12_ravg = statistics.mean(Wilson_12["reading_score"])


######### Cabrera High School Reading Average By Grade

Cabrera_9 = Cabrera_data.loc[Cabrera_data['grade'] == '9th'] 
Cabrera_9_ravg = statistics.mean(Cabrera_9["reading_score"])

Cabrera_10 = Cabrera_data.loc[Cabrera_data['grade'] == '10th'] 
Cabrera_10_ravg = statistics.mean(Cabrera_10["reading_score"])

Cabrera_11 = Cabrera_data.loc[Cabrera_data['grade'] == '11th'] 
Cabrera_11_ravg = statistics.mean(Cabrera_11["reading_score"])

Cabrera_12 = Cabrera_data.loc[Cabrera_data['grade'] == '12th'] 
Cabrera_12_ravg = statistics.mean(Cabrera_12["reading_score"])


######### Bailey High School Reading Average By Grade

Bailey_9 = Bailey_data.loc[Bailey_data['grade'] == '9th'] 
Bailey_9_ravg = statistics.mean(Bailey_9["reading_score"])

Bailey_10 = Bailey_data.loc[Bailey_data['grade'] == '10th'] 
Bailey_10_ravg = statistics.mean(Bailey_10["reading_score"])

Bailey_11 = Bailey_data.loc[Bailey_data['grade'] == '11th'] 
Bailey_11_ravg = statistics.mean(Bailey_11["reading_score"])

Bailey_12 = Bailey_data.loc[Bailey_data['grade'] == '12th'] 
Bailey_12_ravg = statistics.mean(Bailey_12["reading_score"])


######### Holden High School Reading Average By Grade

Holden_9 = Holden_data.loc[Holden_data['grade'] == '9th'] 
Holden_9_ravg = statistics.mean(Holden_9["reading_score"])

Holden_10 = Holden_data.loc[Holden_data['grade'] == '10th'] 
Holden_10_ravg = statistics.mean(Holden_10["reading_score"])

Holden_11 = Holden_data.loc[Holden_data['grade'] == '11th'] 
Holden_11_ravg = statistics.mean(Holden_11["reading_score"])

Holden_12 = Holden_data.loc[Holden_data['grade'] == '12th'] 
Holden_12_ravg = statistics.mean(Holden_12["reading_score"])


######### Pena High School Reading Average By Grade

Pena_9 = Pena_data.loc[Pena_data['grade'] == '9th'] 
Pena_9_ravg = statistics.mean(Pena_9["reading_score"])

Pena_10 = Pena_data.loc[Pena_data['grade'] == '10th'] 
Pena_10_ravg = statistics.mean(Pena_10["reading_score"])

Pena_11 = Pena_data.loc[Pena_data['grade'] == '11th'] 
Pena_11_ravg = statistics.mean(Pena_11["reading_score"])

Pena_12 = Pena_data.loc[Pena_data['grade'] == '12th'] 
Pena_12_ravg = statistics.mean(Pena_12["reading_score"])


######### Wright High School Reading Average By Grade

Wright_9 = Wright_data.loc[Wright_data['grade'] == '9th'] 
Wright_9_ravg = statistics.mean(Wright_9["reading_score"])

Wright_10 = Wright_data.loc[Wright_data['grade'] == '10th'] 
Wright_10_ravg = statistics.mean(Wright_10["reading_score"])

Wright_11 = Wright_data.loc[Wright_data['grade'] == '11th'] 
Wright_11_ravg = statistics.mean(Wright_11["reading_score"])

Wright_12 = Wright_data.loc[Wright_data['grade'] == '12th'] 
Wright_12_ravg = statistics.mean(Wright_12["reading_score"])

######### Rodriguez High School Reading Average By Grade

Rodriguez_9 = Rodriguez_data.loc[Rodriguez_data['grade'] == '9th'] 
Rodriguez_9_ravg = statistics.mean(Rodriguez_9["reading_score"])

Rodriguez_10 = Rodriguez_data.loc[Rodriguez_data['grade'] == '10th'] 
Rodriguez_10_ravg = statistics.mean(Rodriguez_10["reading_score"])

Rodriguez_11 = Rodriguez_data.loc[Rodriguez_data['grade'] == '11th'] 
Rodriguez_11_ravg = statistics.mean(Rodriguez_11["reading_score"])

Rodriguez_12 = Rodriguez_data.loc[Rodriguez_data['grade'] == '12th'] 
Rodriguez_12_ravg = statistics.mean(Rodriguez_12["reading_score"])


######### Johnson High School Reading Average By Grade

Johnson_9 = Johnson_data.loc[Johnson_data['grade'] == '9th'] 
Johnson_9_ravg = statistics.mean(Johnson_9["reading_score"])

Johnson_10 = Johnson_data.loc[Johnson_data['grade'] == '10th'] 
Johnson_10_ravg = statistics.mean(Johnson_10["reading_score"])

Johnson_11 = Johnson_data.loc[Johnson_data['grade'] == '11th'] 
Johnson_11_ravg = statistics.mean(Johnson_11["reading_score"])

Johnson_12 = Johnson_data.loc[Johnson_data['grade'] == '12th'] 
Johnson_12_ravg = statistics.mean(Johnson_12["reading_score"])


######### Ford High School Reading Average By Grade

Ford_9 = Ford_data.loc[Ford_data['grade'] == '9th'] 
Ford_9_ravg = statistics.mean(Ford_9["reading_score"])

Ford_10 = Ford_data.loc[Ford_data['grade'] == '10th'] 
Ford_10_ravg = statistics.mean(Ford_10["reading_score"])

Ford_11 = Ford_data.loc[Ford_data['grade'] == '11th'] 
Ford_11_ravg = statistics.mean(Ford_11["reading_score"])

Ford_12 = Ford_data.loc[Ford_data['grade'] == '12th'] 
Ford_12_ravg = statistics.mean(Ford_12["reading_score"])


######### Thomas High School Reading Average By Grade

Thomas_9 = Thomas_data.loc[Thomas_data['grade'] == '9th'] 
Thomas_9_ravg = statistics.mean(Thomas_9["reading_score"])

Thomas_10 = Thomas_data.loc[Thomas_data['grade'] == '10th'] 
Thomas_10_ravg = statistics.mean(Thomas_10["reading_score"])

Thomas_11 = Thomas_data.loc[Thomas_data['grade'] == '11th'] 
Thomas_11_ravg = statistics.mean(Thomas_11["reading_score"])

Thomas_12 = Thomas_data.loc[Thomas_data['grade'] == '12th'] 
Thomas_12_ravg = statistics.mean(Thomas_12["reading_score"])


# In[ ]:


reading_avg_by_grade = {'School Name': ['Huang High School','Figueroa High School',
                    'Shelton High School','Hernandez High School','Griffin High School','Wilson High School',
                    'Cabrera High School','Bailey High School','Holden High School',     
                    'Pena High School','Wright High School','Rodriguez High School',
                    'Johnson High School','Ford High School','Thomas High School'],
                    '9th': [Huang_9_ravg,Figueroa_9_ravg,Shelton_9_ravg,Hernandez_9_ravg,
                    Griffin_9_ravg,Wilson_9_ravg,Cabrera_9_ravg,Bailey_9_ravg,Holden_9_ravg,
                    Pena_9_ravg,Wright_9_ravg,Rodriguez_9_ravg,Johnson_9_ravg,Ford_9_ravg,Thomas_9_ravg], 
                    '10th': [Huang_10_ravg,Figueroa_10_ravg,Shelton_10_ravg,Hernandez_10_ravg,
                    Griffin_10_ravg,Wilson_10_ravg,Cabrera_10_ravg,Bailey_10_ravg,Holden_10_ravg,
                    Pena_10_ravg,Wright_10_ravg,Rodriguez_10_ravg,Johnson_10_ravg,Ford_10_ravg,Thomas_10_ravg], 
                    '11th': [Huang_11_ravg,Figueroa_11_ravg,Shelton_11_ravg,Hernandez_11_ravg,
                    Griffin_11_ravg,Wilson_11_ravg,Cabrera_11_ravg,Bailey_11_ravg,Holden_11_ravg,
                    Pena_11_ravg,Wright_11_ravg,Rodriguez_11_ravg,Johnson_11_ravg,Ford_11_ravg,Thomas_11_ravg],
                    '12th': [Huang_12_ravg,Figueroa_12_ravg,Shelton_12_ravg,Hernandez_12_ravg,
                    Griffin_12_ravg,Wilson_12_ravg,Cabrera_12_ravg,Bailey_12_ravg,Holden_12_ravg,
                    Pena_12_ravg,Wright_12_ravg,Rodriguez_12_ravg,Johnson_12_ravg,Ford_12_ravg,Thomas_12_ravg]}

reading_avg_by_grade_df = pd.DataFrame(reading_avg_by_grade)                   
                                        
reading_avg_by_grade_df


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[ ]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# In[ ]:


pd.cut(school_summary_df["Per Student Budget"], spending_bins, labels=group_names)
school_summary_df["Spending Ranges (Per Student)"] = pd.cut(school_summary_df["Per Student Budget"], spending_bins, labels=group_names)

school_summary_df

spending_group = school_summary_df.groupby("Spending Ranges (Per Student)")

spending_group[["Average Math Score", "Average Reading Score",
                "% Passing Math","% Passing Reading",
               "% Overall Passing Rate"]].mean()


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[ ]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# In[ ]:


pd.cut(school_summary_df["Size"], size_bins, labels=group_names)
school_summary_df["School Size"] = pd.cut(school_summary_df["Size"], size_bins, labels=group_names)

school_summary_df

size_group = school_summary_df.groupby("School Size")

size_group[["Average Math Score", "Average Reading Score",
                "% Passing Math","% Passing Reading",
               "% Overall Passing Rate"]].mean()


# ## Scores by School Type

# * Perform the same operations as above, based on school type.

# In[ ]:


schools_type_df = school_summary_df.groupby('School Type')
schools_type_df.head()


schools_type_df[["Average Math Score", "Average Reading Score",
                "% Passing Math","% Passing Reading",
               "% Overall Passing Rate"]].mean()


# In[ ]:


# You must include a written description of three observable trends based on the data.

# In the included dataset we can observe that:
#     - Smaller schools tended to be the top performers in Math and Reading scores, perhaps due to smaller class sizes.
#     - Spending per student did not necessarily translate into higher test scores, the highest performers were actually schools
#         that were in the lowest spending per student category (<$585).
#     - Charter schools tended to have higher overall passing rates when it came to Math and Reading.

