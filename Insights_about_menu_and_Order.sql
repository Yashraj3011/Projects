-- 1. Combine the menu_items and order_details into a single table. 
SELECT * FROM menu_items ;
SELECT * FROM order_details;

SELECT * 
FROM order_details od LEFT JOIN menu_items mi
	ON od.item_id = mi.menu_item_id;
    
-- 2. What were the least and most ordered items ? What catgories were they in ?
SELECT item_name,category, COUNT(order_details_id) as num_purchases
FROM order_details od LEFT JOIN menu_items mi
	ON od.item_id = mi.menu_item_id
GROUP BY item_name, category
ORDER BY num_purchases DESC;


-- 3. What were the top 5 orders that spent most money ? 
SELECT order_id, SUM(price) as total_spend
FROM order_details od LEFT JOIN menu_items mi
	ON od.item_id = mi.menu_item_id
GROUP BY order_id
ORDER BY total_spend desc
Limit 5;

-- 4. View the details of the highest spend order. Waht insights you can gather from it ?
SELECT category, count(item_id) as num_items
FROM order_details od LEFT JOIN menu_items mi
	ON od.item_id = mi.menu_item_id
WHERE order_id = 440 
GROUP BY category;

-- 5. View the details of top 5 highest spend order. Waht insights you can gather from it ?
SELECT order_id,category, count(item_id) as num_items
FROM order_details od LEFT JOIN menu_items mi
	ON od.item_id = mi.menu_item_id
WHERE order_id IN (440, 2075, 1957, 330, 2675) 
GROUP BY order_id,category;