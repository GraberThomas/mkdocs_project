FROM python:3.13-alpine AS builder

WORKDIR /docs

COPY requirements.txt /docs/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /docs

RUN mkdocs build --strict --site-dir /output

FROM nginx:alpine-slim

COPY --from=builder /output /usr/share/nginx/html

EXPOSE 80

# Démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
