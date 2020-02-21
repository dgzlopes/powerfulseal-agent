
> This project is under development.

`curl -X POST "http://0.0.0.0:8000/attacks/new" -H "accept: application/json" -H "Content-Type: application/json" -d "{ json snippet }"`
```json
{
  "command": {
    "type": "cpu",
    "args": [
      "--cores","1","--duration","40"
    ]
  },
  "target": []
}
```
```json
{
  "command": {
    "type": "memory",
    "args": []
  },
  "target": []
}
```