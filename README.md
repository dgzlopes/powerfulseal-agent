# powerfulseal-agent

> :warning: This repo is a proof of concept for an experimental Powerfulseal feature. 

## Usage
> Requirements: Docker

Build and run the container:
```
$ make build
$ make run
```
Go to -> http://127.0.0.1:8000/docs (Interactive OpenAPI based docs).

## Actions

Right now you can List attacks, Delete attacks and Create new attacks. For a quick and interactive overview go to -> [/docs](http://127.0.0.1:8000/docs)

Example [API View](https://github.com/dgzlopes/powerfulseal-agent/blob/master/media/api-docs.png).

## Attacks

Right now three areas of attack are available in `powerfulseal-agent`. Each one with its own types of attacks.

> The API design and docs are inspired by [Gremlin](https://www.gremlin.com/docs/infrastructure-layer/attacks/).

### Resource
> Types: CPU and memory

This type of attack makes use of `stress` to exhaust resources.

#### Examples

```json
# Default memory attack
{
  "command": {
    "type": "memory",
    "args": []
  }
}
```

```json
# CPU attack with custom args
{
  "command": {
    "type": "cpu",
    "args": [
      "--cores","1","--duration","40"
    ]
  }
}
```

#### Todo/Ideas

- Add IO and Disk types.
- Add docs about each type and its args.

### Network

TBD (Latency [placeholder](https://github.com/dgzlopes/powerfulseal-agent/blob/master/powerfulseal_agent/network.py) in code)

### State

> Types: Shutdown and restart

Perform chaos actions on the host operating system.

#### Examples

```json
{
  "command": {
    "type": "shutdown",
    "args": []
  }
}
```

#### Todo/Ideas

- Add Process killer type.
- Add docs about each type and its args.
