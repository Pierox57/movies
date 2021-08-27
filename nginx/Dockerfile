FROM node:16.7 as frontend-build
WORKDIR /app
COPY frontend/package*.json /app/
RUN npm install
COPY frontend /app/
RUN npm run build

FROM nginx:1.21.1
WORKDIR /app
COPY --from=frontend-build /app/dist /app/