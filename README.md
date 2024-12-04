# Bikeflex: Your Electric Bike Marketplace
#### Video Demo: [Watch the Demo Here](<URL HERE>)
#### Description:

Bikeflex is an e-commerce platform dedicated to electric bikes. It enables users to browse, search, and purchase electric bikes from a wide range of options. The platform is designed with user experience in mind, offering a seamless interface for both customers and administrators. Built using Django, HTML, CSS, and SQLite3, Bikeflex demonstrates the power of web technologies in creating a functional and responsive online store.

---

## Features:
1. **Homepage**: A welcoming interface showcasing featured electric bikes and the latest arrivals.
2. **Product Listings**: A catalog of bikes with detailed information, pricing, and filtering options.
3. **Shopping Cart**: Users can add items to their cart and adjust quantities before proceeding to checkout.
4. **Checkout System**: A secure and straightforward process for completing purchases.
5. **User Authentication**: Customers can create accounts, log in, and manage their orders and profiles.
6. **Admin Panel**: Administrators can manage inventory, update product details, and monitor orders.
7. **Responsive Design**: The platform is accessible on various devices, ensuring a consistent experience.

---

## File Descriptions:

- **`bikestore/`**: Contains the primary Django project files.
  - **`settings.py`**: Configures the project, including database setup and app registration.
  - **`urls.py`**: Defines the routing for all URLs in the application.
  - **`wsgi.py`**: Entry point for WSGI-compatible web servers to serve the project.

- **`store/`**: The core app responsible for the e-commerce functionality.
  - **`models.py`**: Defines the database schema for products, orders, and users.
  - **`views.py`**: Handles business logic and renders the appropriate templates.
  - **`forms.py`**: Contains forms for user input, such as login and product management.
  - **`templates/`**: Houses the HTML files for the website's frontend.
    - **`base.html`**: The main template structure for the site.
    - **`home.html`**: The homepage view.
    - **`product_detail.html`**: Displays a list of products with filtering options.
    - **`cart.html`**: Shows items in the shopping cart.
    - **`checkout.html`**: The checkout page.

- **`static/`**: Contains static assets like CSS, images, and JavaScript.
  - **`style.css`**: Stylesheet for the website, ensuring a clean and modern look.

- **`db.sqlite3`**: The SQLite3 database storing all application data, including user accounts, products, and orders.

- **`manage.py`**: Django’s command-line utility for administrative tasks.

---

## Design Choices:
### **Database Design:**
I chose SQLite3 for its simplicity and compatibility during development. For a production environment, I would consider upgrading to a more robust database like PostgreSQL.

### **Template Structure:**
The use of Django templates with a base file (`base.html`) ensures consistency across pages, making it easier to maintain and update the site.

### **User Experience:**
A responsive design was prioritized to ensure usability across devices. Bootstrap was considered for styling but ultimately I opted for custom CSS to have more control over the look and feel.

### **Checkout and Payment:**
Currently, the checkout process stops short of integrating a live payment gateway due to time constraints. However, the design allows for easy integration with services like Stripe or PayPal in the future.

---

## Challenges and Considerations:
### **Design Challenges:**
- Balancing functionality with simplicity was a key challenge. I aimed to provide enough features for users without overwhelming them.
- Security was a major consideration. I implemented Django's authentication system and plan to add HTTPS and secure session management in the future.

### **Future Improvements:**
- **Payment Integration**: Implementing live payment options for a complete e-commerce experience.
- **Search Optimization**: Improving the search and filtering system for better performance.
- **Performance**: Optimizing database queries and reducing load times with caching.
- **Deployment**: Moving to a cloud platform for wider accessibility and scalability.

---

## How to Run the Project:

1. Clone the repository:
   ```bash
   git clone https://github.com/Samuel-Nnadi/bikestore.git
   cd bikestore

2. Create and activate python environment:
    python -m venv venv
    venv\Scripts\activate

3. Install dependencies:
    pip install -r requirements.txt

4. Run database migrations:
    python manage.py makemigrations
    python manage.py migrate

5. Start the server:
    python manage.py runserver

6. Open your browser and navigate to http://127.0.0.1:8000

---

## Acknowledgments:
- CS50: For providing a comprehensive course that enabled me to build this project.
- Django Documentation: For its excellent resources that guided the development process.
- Friends and Family: For their support and feedback.
    
### ***Thank you for exploring Bikeflex!***