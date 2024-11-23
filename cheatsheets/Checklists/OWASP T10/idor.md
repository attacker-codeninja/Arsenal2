# IDOR Checklist for Bounty Hunters

## **1. General Preparations**
- [ ] Identify all endpoints that use user-supplied identifiers such as:
  - Numeric IDs (`12345`).
  - Alphanumeric strings (`abc123`).
  - UUIDs (`550e8400-e29b-41d4-a716-446655440000`).
  - Hash-like keys (`5f4dcc3b5aa765d61d8327deb882cf99`).
- [ ] Analyze the application's roles, permissions, and access levels:
  - Super Admin, Admin, Moderator, Regular User, Guest.
- [ ] Gather valid identifiers by creating accounts, capturing tokens, and logging out each state.
- [ ] Use tools to capture requests:
  - Burp Suite, OWASP ZAP, Postman, or browser dev tools.
- [ ] Inspect JavaScript files for hidden routes or API documentation.

---

## **2. Advanced Testing Techniques**
### **2.1 Direct Object Manipulation**
- [ ] Test common object identifiers:
  - `/user/123`, `/order/ABC123`, `/invoice/INV-2023-001`.
- [ ] Check if endpoints accept partial or incomplete identifiers (e.g., `123`, `ABC`).
- [ ] Try mixed-case encoding (`abc123` → `ABC123`, URL encoding, or base64 decoding).

### **2.2 Fuzzing Identifiers**
- [ ] Use automated fuzzers (e.g., FFUF, Intruder) to test for IDOR vulnerabilities by brute-forcing:
  - Sequential or incremental IDs.
  - Known account IDs extracted from responses or front-end code.
  - Common patterns (e.g., `test`, `guest`, `admin`, `001`, `root`).

### **2.3 Testing for Token Leaks**
- [ ] Check API responses for embedded tokens (e.g., JWTs or session cookies).
- [ ] Test if tokens are tied to session ownership:
  - Replay tokens from one session in another.

### **2.4 Role and Permission Escalation**
- [ ] Test for bypassing permissions by altering `role_id` or `privilege_level` parameters.
- [ ] Check if non-admin accounts can access `/admin` endpoints or views.
- [ ] Confirm whether user roles are validated server-side or only client-side.

### **2.5 Multi-User Testing**
- [ ] Create multiple test accounts to simulate different user roles and states.
- [ ] Perform cross-account testing to ensure no data leakage between users.
- [ ] Validate if log-out or account suspension removes access to sensitive data.

### **2.6 File Access**
- [ ] Test file upload/download endpoints for IDOR:
  - `/files/<file_id>`, `/images/<image_name>.jpg`.
- [ ] Verify whether unauthorized users can view, delete, or modify files.
- [ ] Check direct access to backups or temporary files (e.g., `.bak`, `.tmp`).

---

## **3. Advanced API Testing**
### **3.1 API-Specific Scenarios**
- [ ] Enumerate API endpoints with tools like Burp Suite's **Engagement Tools** or `api_spec` files.
- [ ] Test GraphQL endpoints for query-based IDOR:
  - Modify IDs in nested GraphQL queries or variables.
  - Check introspection responses for hidden objects.

### **3.2 Batch and Bulk Operations**
- [ ] Test batch API operations (e.g., `/delete_many`, `/update_all`) for IDOR vulnerabilities.
- [ ] Inject unauthorized IDs into batch requests and observe behavior.

### **3.3 Headers and Cookies**
- [ ] Modify key headers:
  - `X-User-ID`, `X-Forwarded-For`, `X-Auth-Token`.
- [ ] Replay valid cookies from other sessions and check access.

---

## **4. Advanced Encoding and Obfuscation Checks**
- [ ] Test obfuscated identifiers:
  - Base64-encoded strings (`12345` → `MTIzNDU=`).
  - Hexadecimal representation (`12345` → `0x3039`).
- [ ] Test for parameter pollution:
  - Append duplicate parameters (e.g., `?user_id=123&user_id=456`).
- [ ] Attempt JSON parameter nesting (e.g., `{"user":{"id":12345}}`).

---

## **5. Application-Specific Scenarios**
### **5.1 E-Commerce and Payments**
- [ ] Modify cart or order IDs to view/edit other users' orders.
- [ ] Test discounts, promo codes, and payment options for misuse.
- [ ] Check refund or dispute endpoints for unauthorized actions.

### **5.2 Social Media Platforms**
- [ ] Test for unauthorized access to private messages, posts, or profiles.
- [ ] Check privacy settings endpoints for bypasses.

### **5.3 Multi-Tenant Applications**
- [ ] Test cross-tenant access by modifying tenant-specific IDs.
- [ ] Verify data segregation by attempting access across tenants.

---

## **6. Common Fix Bypass Techniques**
- [ ] Replay API requests while logged out.
- [ ] Change request methods (e.g., `PUT` → `POST` or `GET` → `DELETE`).
- [ ] Test cases with and without authentication headers.
- [ ] Add or remove optional parameters to break access control logic.

---

## **7. Tools for Advanced Bug Bounty IDOR Testing**
- **Manual Testing**:
  - Burp Suite Intruder, Repeater.
  - Postman for endpoint manipulation.
- **Automation**:
  - FFUF for fuzzing parameters and IDs.
  - ParamMiner for hidden parameter discovery.
- **API Enumeration**:
  - Tools like **Swagger-UI**, **GraphQL Voyager**, or Postman's API Explorer.
- **Workflow Mapping**:
  - Burp's session tracer and logging tools.

---

## **8. Reporting Best Practices**
- [ ] Include:
  - Full request/response pairs.
  - Screenshots of successful IDOR exploitation.
- [ ] Provide a clear reproduction path.
- [ ] Suggest clear remediation strategies:
  - Implement server-side access control checks.
  - Use unpredictable, non-sequential identifiers.

---

## **9. Reference and Resources**
- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [OWASP Top 10: Broken Access Control](https://owasp.org/www-project-top-ten/)
- Bug bounty resources like HackerOne reports, CTFs, and labs.
