FROM node:20-alpine

# Устанавливаем рабочую директорию
WORKDIR /frontend

# Копируем файлы зависимостей для установки npm пакетов
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install
