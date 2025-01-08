# Multi-stage build
FROM node:18-alpine AS builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

# Runtime image
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /app /app
EXPOSE 4000
CMD ["node", "src/index.js"]
