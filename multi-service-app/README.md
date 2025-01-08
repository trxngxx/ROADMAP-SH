# Multi-service Task Management Application

Project URL: https://roadmap.sh/projects/multiservice-docker

A full-stack containerized application built with React, Node.js, MongoDB, Redis, and Nginx. This project demonstrates advanced Docker and microservices concepts using Docker Compose for orchestration.

## 🏗 Architecture

```
├── frontend (React)
├── backend (Node.js/Express)
├── nginx (Reverse Proxy)
├── mongodb (Database)
└── redis (Cache)
```

### Key Features

- **Frontend**: React application with Material-UI
- **Backend**: RESTful API with Express
- **Database**: MongoDB with persistence
- **Caching**: Redis for performance optimization
- **Proxy**: Nginx for routing and load balancing
- **Docker**: Multi-container deployment
- **Logging**: Centralized logging system
- **Monitoring**: Health checks for all services

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Node.js (for local development)
- Git

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/trxngxx/ROADMAP-SH.git
cd multi-service-app
```

2. Create `.env` file in the root directory:
```env
MONGO_ROOT_USERNAME=admin
MONGO_ROOT_PASSWORD=secret123
REDIS_PASSWORD=redis123
NODE_ENV=development
API_PORT=3000
REACT_APP_API_URL=http://localhost:3000/api
```

### Development

Start all services in development mode:
```bash
docker-compose up --build
```

Access the applications:
- Frontend: http://localhost
- Backend API: http://localhost/api
- MongoDB: localhost:27017
- Redis: localhost:6379

### Production Deployment

1. Build optimized images:
```bash
docker-compose -f docker-compose.prod.yml build
```

2. Start the services:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 🛠 Project Structure

```
multi-service-app/
├── .env
├── docker-compose.yml
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
├── backend/
│   ├── Dockerfile
│   ├── package.json
│   └── src/
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── mongo/
│   └── init.js
└── redis/
    └── redis.conf
```

## 🔧 Service Configuration

### Frontend (React)
- Built with Create React App
- Material-UI components
- React Query for API state management
- Production-optimized Nginx serving

### Backend (Node.js/Express)
- RESTful API architecture
- MongoDB with Mongoose ODM
- Redis caching
- Winston logging
- Security middleware (Helmet, Rate Limiting)
- CORS enabled
- Compression

### Nginx
- Reverse proxy configuration
- SSL/TLS support (in production)
- Gzip compression
- Static file serving
- Load balancing ready

### MongoDB
- Persistent storage
- Initial data seeding
- Authentication enabled
- Optimized configuration

### Redis
- In-memory caching
- Persistence enabled
- Password protection
- Memory optimization

## 📝 API Documentation

### Endpoints

#### Tasks
- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/:id` - Get task details
- `PUT /api/tasks/:id` - Update task
- `DELETE /api/tasks/:id` - Delete task

#### Health Check
- `GET /api/health` - Service health status

## 🔍 Monitoring & Logging

### Logs Location
- Backend: `./backend/logs/`
- Nginx: `./nginx/logs/`
- MongoDB: Inside container at `/data/db/`
- Redis: Inside container at `/data/`

### Health Checks
All services have integrated health checks configured in Docker Compose.

## 🔒 Security

- Environment variables for sensitive data
- Redis password protection
- MongoDB authentication
- Nginx security headers
- Rate limiting
- CORS configuration

## 🚦 Common Commands

### Docker Compose
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f [service_name]

# Stop all services
docker-compose down

# Rebuild specific service
docker-compose build [service_name]

# Scale services
docker-compose up -d --scale backend=3
```

### Container Management
```bash
# List containers
docker ps

# Container logs
docker logs [container_id]

# Execute command in container
docker exec -it [container_id] bash
```

### Data Management
```bash
# Backup MongoDB
docker exec -it [mongo_container_id] mongodump

# Redis CLI
docker exec -it [redis_container_id] redis-cli
```

## 🔧 Troubleshooting

Common issues and solutions:

1. **Connection Refused**
   - Check if all containers are running
   - Verify network configuration
   - Ensure ports are not in use

2. **Data Persistence Issues**
   - Check volume mounts
   - Verify permissions
   - Review Docker volume status

3. **Performance Issues**
   - Monitor Redis cache hits/misses
   - Check MongoDB indexes
   - Review Nginx access logs

## 📈 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Support

For support and questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Updates and Maintenance

- Regular dependency updates
- Security patches
- Feature additions
- Bug fixes

Remember to regularly update your dependencies and check for security advisories.