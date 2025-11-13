# Use Node para build
FROM node:20-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --prod

# Use Nginx para servir a aplicação
FROM nginx:alpine
COPY --from=build /app/dist/meu-projeto-angular /usr/share/nginx/html

# Copie configuração customizada se quiser (opcional)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
