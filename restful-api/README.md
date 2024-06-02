Basics of HTTP/HTTPS
Background
The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

Objective
At the end of this exercise, students should be able to:

Differentiate between HTTP and HTTPS.
Understand the basic working and structure of HTTP requests and responses.
Recognize and explain the common HTTP methods and status codes.
Resources
Mozilla Developer Network (MDN) - An Overview of HTTP
Difference between HTTP and HTTPS
List of HTTP status codes
Instructions
Differentiating HTTP and HTTPS
Read the provided resources to understand the basic differences between HTTP and HTTPS. Jot down the main differences, focusing on security aspects.

Main Differences between HTTP and HTTPS:

Security: HTTP does not encrypt data, making it vulnerable to eavesdropping. HTTPS uses SSL/TLS encryption to secure data.
Port: HTTP typically uses port 80, while HTTPS uses port 443.
URL Prefix: HTTP URLs start with http://, whereas HTTPS URLs start with https://.
Certificate: HTTPS requires an SSL/TLS certificate issued by a Certificate Authority (CA).
Performance: HTTPS can be slightly slower due to the encryption/decryption process, but modern optimizations have minimized this difference.
Understanding HTTP Structure
Visit a simple website, right-click, and choose “Inspect” or “Inspect Element”.
Navigate to the “Network” tab. This shows all network requests made by the page.
Reload the page and observe the first request. Click on it.
Explore the “Headers” section to understand the structure of HTTP requests and responses.
Structure of an HTTP Request:

Request Line: Contains the method, path, and HTTP version (e.g., GET /index.html HTTP/1.1).
Headers: Key-value pairs providing additional information (e.g., Host, User-Agent).
Body: Optional data sent with POST, PUT, or PATCH requests.
Structure of an HTTP Response:

Status Line: Contains the HTTP version, status code, and status message (e.g., HTTP/1.1 200 OK).
Headers: Key-value pairs providing information about the response (e.g., Content-Type, Content-Length).
Body: The data returned by the server (e.g., HTML content, JSON data).
Exploring HTTP Methods and Status Codes
Common HTTP Methods:

GET
Description: Retrieves data from the server.
Use Case: Fetching a web page or data from an API.
POST
Description: Sends data to the server.
Use Case: Submitting a form or uploading a file.
PUT
Description: Updates data on the server.
Use Case: Updating user information or modifying a resource.
DELETE
Description: Deletes data from the server.
Use Case: Removing a resource or record.
Common HTTP Status Codes:

200 OK
Description: The request was successful.
Scenario: When a web page loads successfully.

201 Created
Description: The request was successful, and a resource was created.
Scenario: After successfully creating a new user.

400 Bad Request
Description: The server could not understand the request due to invalid syntax.
Scenario: When a required parameter is missing from a request.

401 Unauthorized
Description: The client must authenticate itself to get the requested response.
Scenario: When accessing a protected resource without proper authentication.

404 Not Found
Description: The server cannot find the requested resource.
Scenario: When a requested page or resource isn’t available on the server.

500 Internal Server Error
Description: The server encountered an unexpected condition.
Scenario: When the server fails to fulfill a valid request due to an internal issue.
Expected Output
Summary of HTTP vs. HTTPS: Detailed differences focusing on security.
HTTP Request and Response Structure: Depiction of key components.
Lists of Methods and Status Codes: Descriptions and use cases for common HTTP methods and status codes.