# My FastAPI Application

This is a FastAPI application that provides an API for managing products.

## Installation

1. Clone the repository: 

        git clone https://github.com/NickSavchyn/fastapi-product.git   
   
2. Create a virtual environment and activate it:

Windows:
    
    python -m venv venv
    .\venv\Scripts\activate
    
    
MacOS:

    python3 -m venv venv
    source venv/bin/activate

3. Install the dependencies:

        pip install -r requirements.txt
  
 
# Usage

1. Start the FastAPI server:

        uvicorn main:app --reload

2. The API endpoints available are:

GET /products/: Retrieve all products.

GET /products/{id}: Retrieve a product by ID.

POST /product/: Create a new product.

PUT /products_update/{id}: Update a product by ID.

PATCH /products_patch/{id}: Partially update a product by ID.

DELETE /products_delete/{id}: Delete a product by ID.
  
