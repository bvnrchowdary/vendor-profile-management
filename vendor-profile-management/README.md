# Vendor Profile Management

Vendor Profile Management is a Django-based web application that allows you to manage vendors, purchase orders, and historical performance metrics.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)


## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/bvnrchowdary/vendor-profile-management.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd vendor-profile-management
    ```

3. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

4. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Usage

1. **Access the admin site:**

    - URL: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
    - Use the superuser credentials created during the installation to log in.

2. **API Endpoints:**

    - The API endpoints are accessible at [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/).

    - **Vendors:**

        - **GET /api/vendors/**

            Retrieve a list of all vendors.

        - **GET /api/vendors/{vendor_id}/performance/**

            Retrieve historical performance metrics for a specific vendor.

        - **POST /api/vendors/**

            Create a new vendor.

        - **PUT /api/vendors/{vendor_id}/**

            Update details for a specific vendor.

        - **DELETE /api/vendors/{vendor_id}/**

            Delete a specific vendor.

    - **Purchase Orders:**

        - **GET /api/purchase_orders/**

            Retrieve a list of all purchase orders.

        - **GET /api/purchase_orders/{purchase_order_id}/acknowledge/**

            Retrieve acknowledgment details for a specific purchase order.

        - **POST /api/purchase_orders/**

            Create a new purchase order.

        - **PUT /api/purchase_orders/{purchase_order_id}/acknowledge/**

            Update the acknowledgment date for a specific purchase order.

        - **DELETE /api/purchase_orders/{purchase_order_id}/acknowledge/**

            Delete a specific purchase order.
