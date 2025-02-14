# Use official Node.js image
FROM node:20

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy all files
COPY . .

# Build the Vue app
RUN npm run build

# Install 'serve' for static hosting
RUN npm install -g serve

# Serve the built app on port 5173
CMD ["serve", "-s", "/app/dist", "-l", "5173"]

# Expose the port
EXPOSE 5173
