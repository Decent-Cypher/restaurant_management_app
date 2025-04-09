# Use an official Node runtime as a parent image
FROM node:23.10.0-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if exists)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all source code
COPY . .

# Expose the port (default for Create React App is 3000)
EXPOSE 3000

# Start the development server
CMD ["npm", "run", "dev"]
