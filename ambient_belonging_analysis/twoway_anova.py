import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

datafile="AmBe_FB_0801.csv"
data = pd.read_csv(datafile)

# prints out a 2x2 anova table
def double_anova(data, dep_col, ind_col1, ind_col2):
  N = len(data[dep_col]) # sample size
  df_a = len(data[ind_col1].unique()) - 1 # degrees of freedom for ind_col1
  df_b = len(data[ind_col2].unique()) - 1 # degrees of freedom for ind_col2
  df_axb = df_a*df_b 
  df_w = N - (len(data[ind_col1].unique())*len(data[ind_col2].unique()))

  grand_mean = data[dep_col].mean() # mean of all values of len

  ssq_a = sum([(data[data[ind_col1] ==l][dep_col].mean()-grand_mean)**2 for l in data[ind_col1]]) # sum of squares for ind_col1
  ssq_b = sum([(data[data[ind_col2] ==l][dep_col].mean()-grand_mean)**2 for l in data[ind_col2]]) # sum of squares for ind_col2
  ssq_t = sum((data[dep_col] - grand_mean)**2) # total sum of squares

  Female = data[data['Gender'] == 'Female'] # the data where ind_col1 = Female
  Male = data[data[ind_col1] == 'Male'] # the data where ind_col1 = Male
  Female_ind_col2_means = [Female[Female[ind_col2] == d][dep_col].mean() for d in Female[ind_col2]]
  Male_ind_col2_means = [Male[Male[ind_col2] == d][dep_col].mean() for d in Male[ind_col2]]
  ssq_w = sum((Male[dep_col] - Male_ind_col2_means)**2) +sum((Female[dep_col] - Female_ind_col2_means)**2)

  ssq_axb = ssq_t-ssq_a-ssq_b-ssq_w # sum of squares for the interaction of ind_col1 and ind_col2

  ms_a = ssq_a/df_a
  ms_b = ssq_b/df_b
  ms_axb = ssq_axb/df_axb
  ms_w = ssq_w/df_w

  f_a = ms_a/ms_w
  f_b = ms_b/ms_w
  f_axb = ms_axb/ms_w


  p_a = stats.f.sf(f_a, df_a, df_w)
  p_b = stats.f.sf(f_b, df_b, df_w)
  p_axb = stats.f.sf(f_axb, df_axb, df_w)

  results = {'sum_sq':[ssq_a, ssq_b, ssq_axb, ssq_w],
             'df':[df_a, df_b, df_axb, df_w],
             'F':[f_a, f_b, f_axb, 'NaN'],
              'PR(>F)':[p_a, p_b, p_axb, 'NaN']}
  columns=['sum_sq', 'df', 'F', 'PR(>F)']
   
  aov_table1 = pd.DataFrame(results, columns=columns,
                            index=[ind_col1, ind_col2, 
                            ind_col1 + ":" + ind_col2, 'Residual'])

  print(aov_table1)

print 'Enrollment Intention'
double_anova(data, 'EnrollmentIntention', 'Gender', 'Condition_DO')
print '\n Ambient Belonging'
double_anova(data, 'AmbientBelonging', 'Gender', 'Condition_DO')
print '\n Anticipated Success'
double_anova(data, 'AnticipatedSuccess', 'Gender', 'Condition_DO')
print '\n Fun'
double_anova(data, 'Fun', 'Gender', 'Condition_DO')
print '\n Natural Skill'
double_anova(data, 'NaturalSkill', 'Gender', 'Condition_DO')
print '\n Confidence'
double_anova(data, 'Confidence', 'Gender', 'Condition_DO')
print '\n Longterm Behavior'
double_anova(data, 'LongtermBehavior', 'Gender', 'Condition_DO')
print '\n Stereotypes'
double_anova(data, 'Stereotypes', 'Gender', 'Condition_DO')
print '\n Masculinity'
double_anova(data, 'Masculinity', 'Gender', 'Condition_DO')
print '\n Gender Stereotypes'
double_anova(data, 'GenderStereotypes', 'Gender', 'Condition_DO')

