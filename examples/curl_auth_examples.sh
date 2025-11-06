#!/bin/bash

# Login Usuario 1 - Desarrollador
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "juan@dev.com", "contrasena": "dev123"}'

# Login Usuario 2 - Diseñadora
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "maria@design.com", "contrasena": "design456"}'

# Login Usuario 3 - Project Manager
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "carlos@pm.com", "contrasena": "pm789"}'

# Login Usuario 4 - Marketing
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "ana@mkt.com", "contrasena": "mkt321"}'

# Login Usuario 5 - QA Tester
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "luis@qa.com", "contrasena": "qa654"}'

# Login Usuario 6 - DevOps
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "sofia@ops.com", "contrasena": "ops987"}'

# Login Usuario 7 - Data Scientist
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "pedro@data.com", "contrasena": "data123"}'

# Login Usuario 8 - UX Researcher
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "laura@ux.com", "contrasena": "ux456"}'

# Login Usuario 9 - Product Owner
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "roberto@product.com", "contrasena": "prod789"}'

# Login Usuario 10 - Frontend Developer
curl -X POST http://localhost:5000/api/usuarios/login \
  -H "Content-Type: application/json" \
  -d '{"email": "carmen@frontend.com", "contrasena": "front123"}'

# Ejemplo de cómo usar el token devuelto:
# TOKEN=$(curl -s -X POST http://localhost:5000/api/usuarios/login -H "Content-Type: application/json" -d '{"email": "juan@dev.com", "contrasena": "dev123"}' | jq -r '.token')
# curl -H "Authorization: Bearer $TOKEN" http://localhost:5000/api/registros
