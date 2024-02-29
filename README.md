# Nombre del Proyecto

Una breve descripción de lo que hace tu proyecto y qué problemas resuelve.

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

Incluye información sobre la licencia bajo la cual se distribuye tu proyecto. Esto es importante para que los usuarios sepan cómo pueden usar y modificar tu código.
MIT License
Copyright (c) 2023 Tu Nombre
