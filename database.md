# Restaurant Management System
# User(Roles)
   - user_id
   - name
   - role
   - contact
   - password

# Category
   - category_id (id)
   - name         (str)

# Food/MenuItems
   - MenuItems_id (int)
   - Items_name (str)
   - Items_price   (float)
   - Category  (Foreign Key) 


# Tables
   - table_id (int)
   - table_number (int/str)
   - table_size (int)
   - available(boolean)

# Order 
   - order_id (int)
   - User_id (FK)
   - payment_status (bool)
   - table_id(FK)

# OrderItem
   -orderitem(PK)
   - Order(FK)
   - MenuItems(FK)
   - quantity (int)
   - price_at_order (float)

# Ingredients
   - ingredient_id (int)
   - name

# Storage
   - storage_id (int)
   - Ingredients(FK)
   - quantity(int)

# Recipe
   - recipe_id (int)
   - Food(FK)
   - recipe

User: 1, 2

Food: pizza, buger

Order: 1: pizza, buger -- 2: pizza