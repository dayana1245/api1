#!/bin/bash

# Usuario 1 - Desarrollador
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan Pérez", "email": "juan@dev.com", "contrasena": "dev123"}'

# Usuario 2 - Diseñadora
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "María García", "email": "maria@design.com", "contrasena": "design456"}'

# Usuario 3 - Project Manager
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Carlos Ruiz", "email": "carlos@pm.com", "contrasena": "pm789"}'

# Usuario 4 - Marketing
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Ana López", "email": "ana@mkt.com", "contrasena": "mkt321"}'

# Usuario 5 - QA Tester
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Luis Torres", "email": "luis@qa.com", "contrasena": "qa654"}'

# Usuario 6 - DevOps
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Sofia Martínez", "email": "sofia@ops.com", "contrasena": "ops987"}'

# Usuario 7 - Data Scientist
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Pedro Sánchez", "email": "pedro@data.com", "contrasena": "data123"}'

# Usuario 8 - UX Researcher
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Laura Díaz", "email": "laura@ux.com", "contrasena": "ux456"}'

# Usuario 9 - Product Owner
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Roberto Gómez", "email": "roberto@product.com", "contrasena": "prod789"}'

# Usuario 10 - Frontend Developer
curl -X POST http://localhost:5000/api/usuarios/registro \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Carmen Vega", "email": "carmen@frontend.com", "contrasena": "front123"}'
