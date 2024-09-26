# OTP-Based User Authentication System

A Django Rest Framework-based system that enables users to register, log in, and authenticate using a One-Time Password (OTP) sent to their email. This project demonstrates how to securely manage user authentication using OTP verification.

## Features

- **User Registration**
  - Users can sign up with details like `username`, `email`, `password`, `confirm_password`, `age`, and `gender`.
  - Password confirmation is enforced before registration.
  
- **Password Hashing**
  - Passwords are securely hashed and stored using Django's built-in hashing mechanism.

- **OTP Generation**
  - An OTP is generated and sent to the user's email when they request OTP login or identity verification.

- **Email Validation**
  - Only registered users can request OTPs. The system validates the existence of the user's email before sending an OTP.

- **OTP Sending**
  - The generated OTP is automatically sent to the user's email for login or verification purposes.

- **OTP Verification**
  - Users input their email and OTP to verify their identity. If the OTP is valid, they are granted access.

- **Error Handling**
  - Clear error messages, such as "Passwords do not match" or "Invalid OTP or email," are provided to users during registration and login.

- **User Authentication**
  - Upon successful OTP verification, the user is authenticated and can proceed to access secure sections of the system.

- **Optional OTP Expiration**
  - You can optionally implement OTP expiration (e.g., 5 minutes) to enhance security.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/surajmendhe5573/otpLogin.git
   cd otp-authentication-system
