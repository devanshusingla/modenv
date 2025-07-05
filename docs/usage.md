# modenv Usage Guide

## Initialization

```bash
modenv layer init
modenv layer init --parents /some/env/lib/python3.11/site-packages
```

## Linking Parents

```bash
modenv layer parent add /path/to/parent --name base-env --priority 1
modenv layer parent remove base-env
```

## Diagnostics

```bash
modenv doctor check
modenv doctor fix
```

## Exporting/Importing Specs

```bash
modenv spec export > spec.toml
modenv spec apply spec.toml
```

## Inspect Graph

```bash
modenv graph
```

## 📚 See Command Reference:
- [layer](./commands/layer.md)
- [doctor](./commands/doctor.md)
- [spec](./commands/spec.md)
- [graph](./commands/graph.md)
