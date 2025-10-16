FROM node:14

WORKDIR /app

COPY package.json ./
# Remove package-lock.json if not present
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]