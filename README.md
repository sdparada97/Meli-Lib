# Meli - Lib

Libreria para manejar el buffer con COLAS o PILAS

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Licencia](#licencia)

## Instalación

Descripción para instalar paquete:

```bash
    pip install meli-lib
```

## Uso

POLICY - FIFO:

```python
    import Buffer

    buffer = Buffer('FIFO')
    buffer.insert(1)
    item = buffer.extract()
    item == 1
```

POLICY -LIFO:

```python
    import Buffer

    buffer = Buffer('FIFO')
    buffer.insert(1)
    item = buffer.extract()
    item == 1
```

## Licencia

MIT License

Copyright (c) 2023 Tu Nombre
