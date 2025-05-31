
USE masai;
SELECT* FROM customers;


#Clean Null Values and Incorrect Data
-- Check nulls in each column (example in PostgreSQL)
SELECT 
  COUNT(*) AS total,
  COUNT(Cabin) AS cabin_not_null,
  COUNT(Age) AS age_not_null
FROM titanic;
#If Cabin is mostly NULL, you can exclude it:


-- Create a cleaned view excluding the Cabin column
CREATE VIEW titanic_cleaned AS
SELECT PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Embarked
FROM titanic;


# Grouping & Aggregation
#Survival Rate by Gender
SELECT 
  Sex,
  AVG(Survived) AS survival_rate
FROM titanic_cleaned
GROUP BY Sex;


#Survival Rate by Class

SELECT 
  Pclass,
  AVG(Survived) AS survival_rate
FROM titanic_cleaned
GROUP BY Pclass;
#Survival Rate by Class and Gender

SELECT 
  Sex,
  Pclass,
  AVG(Survived) AS survival_rate
FROM titanic_cleaned
GROUP BY Sex, Pclass
ORDER BY Sex, Pclass;
#3. Age Distribution (Histogram-like using CASE or WIDTH_BUCKET)
#For PostgreSQL:


SELECT 
  WIDTH_BUCKET(Age, 0, 80, 8) AS age_bucket,
  COUNT(*) AS count
FROM titanic_cleaned
GROUP BY age_bucket
ORDER BY age_bucket;

#In MySQL (manually bucketed):

SELECT
  CASE
    WHEN Age < 10 THEN '0-9'
    WHEN Age BETWEEN 10 AND 19 THEN '10-19'
    WHEN Age BETWEEN 20 AND 29 THEN '20-29'
    WHEN Age BETWEEN 30 AND 39 THEN '30-39'
    WHEN Age BETWEEN 40 AND 49 THEN '40-49'
    WHEN Age BETWEEN 50 AND 59 THEN '50-59'
    WHEN Age >= 60 THEN '60+'
    ELSE 'Unknown'
  END AS age_group,
  COUNT(*) AS count
FROM titanic_cleaned
GROUP BY age_group
ORDER BY age_group;

#4. Correlation Matrix in SQL
#SQL doesn’t compute correlations directly, but in PostgreSQL or with an extension like corr() in PostgreSQL:

SELECT
  CORR(Survived, Age) AS corr_survived_age,
  CORR(Survived, Fare) AS corr_survived_fare,
  CORR(Survived, Pclass) AS corr_survived_pclass
FROM titanic_cleaned;


#For MySQL, you need to compute it manually with the correlation formula.

#5. Summary Insights Example

#Male survival rate is X%, female is Y%.

#First-class passengers have the highest survival rate.

#Most passengers were aged between 20–40.

#Strongest correlation with survival: Pclass (inverse).