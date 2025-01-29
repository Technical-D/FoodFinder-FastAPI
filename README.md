# FatSecret API Integration with FastAPI

## Description

This project integrates the **FatSecret API** with **FastAPI** to securely fetch food-related data using **OAuth 2.0 authentication**. The application allows users to search for food items and retrieve detailed information such as nutritional values, ingredients, and more.

## Swagger UI (/docs)
![image](https://github.com/user-attachments/assets/4fb5b190-6218-4573-aecc-7a1209bf160c)

## Features
- **OAuth 2.0 Authentication**: Secure handling of credentials and access tokens.
- **IP Whitelisting**: Ensures only whitelisted IPs can access the API.
- **FastAPI**: Lightweight, high-performance web framework for serving the API requests.

## Requirements
- Python 3.10+
- FastAPI
- Requests
- Uvicorn (for development server)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure your API keys**:
   - Obtain your FatSecret API Key and Client Secret.
   - Set up your IP whitelist in the FatSecret Developer Console.
6. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```
8. **Access the API**:
   - Visit http://localhost:8000 in your browser to access the FastAPI documentation and make requests to the FatSecret API.

## IP Whitelisting
Please note that FatSecret API requires IP whitelisting. You need to add your IP address to the API Key settings in the FatSecret Developer Console to make requests. It may take up to 24 hours for changes to take effect.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
```vbnet
Feel free to modify it to suit your needs. Let me know if you need further changes!
```
