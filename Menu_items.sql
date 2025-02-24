USE restaurant_db;
-- 1. View the menu_items table.
SELECT * FROM menu_items;

-- 2. Find the number of items on the menu.
SELECT COUNT(*) FROM menu_items;

-- 3. Wht are the least and most expensive item on the menu?
-- ascending
SELECT * FROM menu_items
ORDER BY price;

-- descending
SELECT * FROM menu_items
ORDER BY price desc;

-- 4. How many are the Italian dishes on the menu?
SELECT COUNT(*) FROM menu_items
WHERE category = 'Italian';

-- 5. What are the least and most expensive Itlian dishes?
-- ascending
SELECT * FROM menu_items
WHERE category= 'Italian'
ORDER BY price;

-- descending
SELECT * FROM menu_items
WHERE category = 'Italian'
ORDER BY price desc;


-- 6. How many dishes are in each category ?
SELECT category, COUNT(category) FROM menu_items
GROUP BY category;


-- 7. What is average dish price in each category ?
SELECT category, AVG(price) as avg_price FROM menu_items
GROUP BY category;
