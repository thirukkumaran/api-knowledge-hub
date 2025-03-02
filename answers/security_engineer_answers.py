SECURITY_ENGINEER_ANSWERS = {
    "What are the most common security vulnerabilities in APIs?": """
Common API Security Vulnerabilities:

1. Authentication Issues
   - Weak authentication mechanisms
   - Missing authentication
   - Token exposure
   - Session management flaws

2. Authorization Flaws
   - Broken access control
   - Missing role checks
   - Privilege escalation
   - IDOR vulnerabilities

3. Data Exposure
   - Sensitive data leakage
   - Insufficient encryption
   - Missing TLS
   - Verbose error messages

4. Input Validation
   - SQL injection
   - XSS vulnerabilities
   - Command injection
   - Parameter tampering

5. Rate Limiting
   - Missing rate limits
   - DDoS vulnerability
   - Resource exhaustion
   - Brute force attacks

For comprehensive security vulnerability information, see <a href='https://docs.developer.tech.gov.sg/docs/api-governance-model' target='_blank'>GovTech's API Security Vulnerabilities</a>.
""",
    "How can I implement robust authentication and authorization for APIs?": """
Robust API Authentication & Authorization:

1. Authentication Methods
   - OAuth 2.0 implementation
   - JWT with proper signing
   - API keys management
   - MFA integration

2. Authorization Framework
   - Role-based access control
   - Attribute-based access
   - Resource-level permissions
   - Scope definitions

3. Token Management
   - Secure token storage
   - Token expiration
   - Rotation policies
   - Revocation mechanisms

4. Security Headers
   - CORS configuration
   - CSP implementation
   - HSTS enforcement
   - Cache controls

5. Best Practices
   - Regular auditing
   - Session management
   - Logging and monitoring
   - Security testing

For detailed authentication guidance, check <a href='https://docs.developer.tech.gov.sg/docs/api-governance-model' target='_blank'>GovTech's Authentication Standards</a>.
""",
    "Which best practices help secure API endpoints effectively?": """
API Endpoint Security Best Practices:

1. Input Validation
   - Schema validation
   - Type checking
   - Size limits
   - Format verification

2. Output Encoding
   - Data sanitization
   - Content-type headers
   - Character encoding
   - Error handling

3. Rate Limiting
   - Request throttling
   - Concurrent limits
   - IP-based limits
   - User-based quotas

4. Monitoring
   - Access logging
   - Error tracking
   - Usage patterns
   - Anomaly detection

5. Infrastructure
   - WAF implementation
   - DDoS protection
   - SSL/TLS setup
   - Network segmentation

For endpoint security best practices, refer to <a href='https://docs.developer.tech.gov.sg/docs/api-governance-model' target='_blank'>GovTech's Endpoint Security Guidelines</a>.
""",
    "How do I protect APIs from common cyber threats?": """
API Cyber Threat Protection:

1. Attack Prevention
   - Input sanitization
   - Parameter validation
   - Request filtering
   - Bot detection

2. Access Control
   - IP whitelisting
   - Geo-blocking
   - VPN requirements
   - Zero trust model

3. Encryption
   - TLS 1.3
   - Data encryption
   - Key management
   - Certificate handling

4. Monitoring
   - IDS/IPS systems
   - SIEM integration
   - Threat intelligence
   - Behavioral analysis

5. Response Plan
   - Incident response
   - Backup systems
   - Recovery procedures
   - Communication plan

For comprehensive threat protection, see <a href='https://docs.developer.tech.gov.sg/docs/api-governance-model' target='_blank'>GovTech's Threat Protection Guidelines</a>.
""",
    "What tools and techniques ensure comprehensive API security testing?": """
API Security Testing Tools & Techniques:

1. Testing Tools
   - OWASP ZAP
   - Burp Suite
   - Postman security
   - SoapUI security

2. Testing Types
   - Penetration testing
   - Vulnerability scanning
   - Fuzzing tests
   - Security scanning

3. Automation
   - CI/CD integration
   - Automated scans
   - Security pipelines
   - Test scheduling

4. Coverage Areas
   - Authentication tests
   - Authorization checks
   - Input validation
   - Output encoding

5. Best Practices
   - Regular testing
   - Environment isolation
   - Report generation
   - Risk assessment

For security testing guidelines, check <a href='https://docs.developer.tech.gov.sg/docs/api-governance-model' target='_blank'>GovTech's Security Testing Standards</a>.
"""
}
