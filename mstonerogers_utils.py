''' This module provides a reusable byline for the author's services. '''
import statistics

def main():
  #define variables 
  company_name: str = 'All Analytics, LLC'
  company_description: str = 'Top rated company!'
  current_employees: int = 50
  has_all_analytics: bool = True
  employee_satisfaction: float = 9.9
  breakroom_snacks: list = ['Coffee', 'Granola Bars',  
  'Water', 'Oreos']
  company_ratings: list = [9.7, 9.6, 9.99, 
  9.8, 9.5]
  work_options: list = ['Remote', 'Hybrid', 'Onsite']

# Multiline string with byline using f-string formatting
  general_overview_string: str = f"""
  Company: {company_name}
  Description: {company_description}
  Has All Analytics: {has_all_analytics}
  Employee Satisfaction: {employee_satisfaction} out of 10!
  Work Options: {work_options}
  Breakroom Snacks: {breakroom_snacks}
  """

  stats_string: str = f"""
  More Details: 
  Number of Happy Employees: {current_employees}
  Lowest Outside Rating: {min(company_ratings)}
  Highest Outside Rating: {max(company_ratings)}
  Number of Ratings: {len(company_ratings)}
  Average Outside Rating: 
  {statistics.mean(company_ratings)}
  Total: {sum(company_ratings)}
  Mode: {statistics.mode(company_ratings)}
  Median: {statistics.median(company_ratings)}
  Standard Deviation: {statistics.stdev(company_ratings)}
  """

  byline: str = f"""
  {general_overview_string}
  {stats_string}
  """
  print(byline)

if __name__ == '__main__':
  main()
