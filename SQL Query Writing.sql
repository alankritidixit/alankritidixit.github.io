-- Employee Database Explorer Assignment

-- 1. List top 5 highest-paid employees
SELECT e.id, e.name, s.salary
FROM employees e
JOIN salaries s ON e.id = s.employee_id
ORDER BY s.salary DESC
LIMIT 5;

-- 2. Count employees in each department
SELECT d.department_name, COUNT(e.id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.department_name
ORDER BY employee_count DESC;

-- 3. Find average salary by department
SELECT d.department_name, AVG(s.salary) AS avg_salary
FROM departments d
JOIN employees e ON d.id = e.department_id
JOIN salaries s ON e.id = s.employee_id
GROUP BY d.department_name
ORDER BY avg_salary DESC;

-- Additional queries using WHERE, HAVING, BETWEEN, IN, LIKE

-- Find employees with salary BETWEEN 50,000 and 100,000
SELECT e.id, e.name, s.salary
FROM employees e
JOIN salaries s ON e.id = s.employee_id
WHERE s.salary BETWEEN 50000 AND 100000;

-- Find departments with more than 10 employees (using HAVING)
SELECT d.department_name, COUNT(e.id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.id = e.department_id
GROUP BY d.department_name
HAVING employee_count > 10;

-- Find employees whose name starts with 'J' (using LIKE)
SELECT id, name
FROM employees
WHERE name LIKE 'J%';

-- Find employees in departments 'Sales', 'Marketing', or 'IT' (using IN)
SELECT e.id, e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.id
WHERE d.department_name IN ('Sales', 'Marketing', 'IT');
