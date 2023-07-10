# My FastAPI Application

This is a FastAPI application that provides an API for managing products.

## Installation

1. Clone the repository: 

        git clone https://github.com/NickSavchyn/fastapi-product.git   
   
2. Create a virtual environment and activate it:

   - **Windows:**
    
     ```
     python -m venv venv
     .\venv\Scripts\activate
     ```
    
   - **MacOS/Linux:**
    
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the dependencies:

        pip install -r requirements.txt

4. Apply database migrations:

   - Make sure your database connection settings are correctly configured in the `config.py` file.
   
   - Run the following command to apply the migrations:
   
     ```
     alembic upgrade head
     ```

## Usage

1. Start the FastAPI server:

        uvicorn main:app --reload

2. The API endpoints available are:

   - **GET /products/:** Retrieve all products.
  
   - **GET /products/{id}:** Retrieve a product by ID.
  
   - **POST /products/:** Create a new product.
  
   - **PUT /products/{id}:** Update a product by ID.
  
   - **PATCH /products/{id}:** Partially update a product by ID.
  
   - **DELETE /products/{id}:** Delete a product by ID.

3. Example Request/Response:

   - **GET /products/:**
   
     Request:
     
     ```http
     GET /products/
     ```
     
     Response:
     
     ```json
     [
       {
         "id": 1,
         "name": "Product 1",
         "price": 10.99
       },
       {
         "id": 2,
         "name": "Product 2",
         "price": 15.99
       }
     ]
     ```

   - **GET /products/{id}:**
   
     Request:
     
     ```http
     GET /products/1
     ```
     
     Response:
     
     ```json
     {
       "id": 1,
       "name": "Product 1",
       "price": 10.99
     }
     ```


