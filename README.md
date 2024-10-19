# Django-Assesment

# **Django REST API with Custom User Roles and Social Authentication**

This project is a **Django REST API** built with **Django Rest Framework (DRF)**. It supports custom user roles, including **admin, coach, agent, and football player**, along with **social authentication (Google and Facebook)**. Additionally, the API includes a secure **password reset** flow via email.

---

## **Features**

- **Custom User Roles**:
  - Admin, Coach, Agent, Football Player.
- **Authentication and Authorization**:
  - **Sign up** with email/password and social accounts (Google, Facebook).
  - **Login** with email/password and social accounts.
  - **Password Reset** through email.
- **Role Management**: Custom logic to handle permissions and user types.
- **Django Allauth Integration** for social logins.

---

## **Tech Stack**

- **Backend**: Django, Django Rest Framework (DRF)
- **Authentication**: Django Allauth
- **Database**: SQLite (for development)
- **Email Service**: Gmail SMTP

---

## **Installation Guide**

### **1. Clone the Repository**

```bash
git clone https://github.com/TigistW/Mereb-django-assesment
cd Mereb-django-assesment
```

### **2. Set Up a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Configure Environment Variables**

Create a `.env` file in the project root to store sensitive data:

```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
SOCIAL_GOOGLE_CLIENT_ID=your-google-client-id
SOCIAL_GOOGLE_SECRET=your-google-client-secret
SOCIAL_FACEBOOK_APP_ID=your-facebook-app-id
SOCIAL_FACEBOOK_SECRET=your-facebook-app-secret
```

### **5. Apply Migrations and Create Superuser**

```bash
python manage.py migrate
python manage.py createsuperuser
```

### **6. Run the Development Server**

```bash
python manage.py runserver
```

The API will be available at:

```
http://127.0.0.1:8000/
```

---

## **API Endpoints**

### **Authentication**

- **Sign up**: `/api/users/signup/`
- **Login**: `/api/users/login/`
- **Social Login (Google)**: `/accounts/google/login/`
- **Social Login (Facebook)**: `/accounts/facebook/login/`
- **Password Reset Request**: `/password_reset/`
- **Password Reset Confirm**: `/reset/<uidb64>/<token>/`

### **Users Management**

- **Get User by ID**: `/api/users/<id>/`

---

## **Usage Instructions**

1. **Google and Facebook OAuth Setup**:

   - Register your app on **Google Cloud Console** and **Facebook Developer Portal**.
   - Add the respective **redirect URIs**:
     - Google: `http://127.0.0.1:8000/accounts/google/login/callback/`
     - Facebook: `http://127.0.0.1:8000/accounts/facebook/login/callback/`
2. **Testing Password Reset**:

   - Use `/password_reset/` to request a reset link.
   - Use `/reset/<uidb64>/<token>/` to reset the password.
3. **Assigning Roles**:

   - Use the Django admin panel to assign roles to users:
     ```
     http://127.0.0.1:8000/admin/
     ```

---

## **Project Structure**

```
your-project/
│
├── Auth/                  # Custom user app
│   ├── models.py           # User models with custom roles
│   ├── serializers.py      # DRF serializers for API responses
│   ├── views.py            # User-related views and endpoints
│
├── templates/registration/ # Templates for password reset and social login
├── manage.py               # Django management commands
├── requirements.txt        # Dependencies list
├── settings.py             # Django project settings
└── urls.py                 # URL configuration
```

---

## **Troubleshooting**

### **Email Issues**

1. Ensure that **Gmail SMTP** or your email provider’s SMTP is correctly configured.
2. Check your **spam folder** if the email is not arriving.
3. For Gmail, use an **App Password** if 2FA is enabled.

### **OAuth Errors**

1. Ensure the redirect URIs match exactly as registered in Google/Facebook portals.
2. Verify that you have enabled **OAuth APIs** in the respective platforms.

## **Contributing**

Pull requests are welcome. For significant changes, please open an issue to discuss what you would like to change.
