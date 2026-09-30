# LMS 502 Bad Gateway Troubleshooting

## 1. Problem Statement

The LMS application was deployed behind Nginx. Users intermittently
received 502 Bad Gateway while accessing the application.

## 2. Architecture

User
  ↓
Nginx Port 80
  ↓
LMS Backend Port 8080
  ↓
Docker Container

## 3. Environment

OS: Ubuntu
Web Server: Nginx
Container Platform: Docker
Application Port: 8080
Proxy Port: 80

## 4. Implementation

1. Created Ubuntu EC2 instance.
2. Installed Docker.
3. Created LMS backend.
4. Built Docker image.
5. Started LMS container.
6. Installed Nginx.
7. Configured Nginx reverse proxy.
8. Tested the application.

## 5. Troubleshooting

Checked:

- Docker container status
- LMS application logs
- Port 8080
- Nginx status
- Nginx configuration
- Nginx error logs
- Backend health endpoint

## 6. Root Cause

The LMS backend Docker container was stopped and was not
listening on port 8080.

Nginx could not connect to the backend and returned
502 Bad Gateway.

## 7. Resolution

The LMS container was started again and backend health was verified.

## 8. Verification

Backend:

curl http://localhost:8080/actuator/health

Nginx:

curl http://localhost

## 9. Prevention

- Configure Docker restart policy.
- Add application health checks.
- Monitor container availability.
- Monitor CPU and memory.
- Monitor Nginx errors.
- Configure alerts for backend failure.
- Maintain proper application logs.

## 10. Conclusion

The 502 error was caused by backend unavailability.
After restoring the backend, Nginx successfully forwarded
requests and the LMS became accessible again.
