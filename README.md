# new virtual env creation

```
python m venv <env_name>
```

# To activate virtual env
```
cd / project_name/scripts/activate
```

# django install 

```
python m install django
```

# project Install

```
django-admin startproject <project_name>
```
# app creation

```
django-admin startapp <appname>
```

# make migration to create database 

```
python manage.py makemigrations
```

# start migration to insert sample data into database 

```
python manage.py migrate
```

# to run project 
```
python manage.py runserver
```

# Django_Invoice_Application

    API to Post new Invoice / to get all invoice data from table : http:localhost:8000/api/invoices/
    API to update exisiting Invoice / to get invoice data from table based on invoice id : http:localhost:8000/api/invoices/<invoice_id>


![image](https://user-images.githubusercontent.com/50217774/159158888-070d02c2-50d5-45cd-bd8b-a368d996e68e.png)


    Database : SQLite,
    
    Table name : Invoice,
    
    Fields : ['id', 'invoice_id', 'invoice_number', 'customer_address', 'customer_city_state',  'customer_cntry', 'customer_name', 'date', 'customer_address', 'due_date',  'notes', 'salesperson_address', 'salesperson_company', 'salesperson_city_state', 'salesperson_cntry', 'customer_city_state',  'created_at', 'salesperson_name', 'status', 'subtotal', 'taxtotal',  'terms', 'total', 'line_items', 'created_at']
    
    sample json format :
    
  ![image](https://user-images.githubusercontent.com/50217774/159169320-b6da0958-7a58-4ebd-9731-9386825b63c6.png)
    

