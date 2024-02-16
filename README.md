# Safety First

Website displaying:
```
  +---+
  | N |
  +---+
   Days
Since Last
 Bricking
 Incident

Last incident: YYYY-MM-DD
```

## Endpoints

GET / -- page
GET /days -- GET /?units=days
GET /hours -- GET /?units=hours
GET /minutes -- GET /?units=minutes
GET /seconds -- GET /?units=seconds
POST /oopsie -- updates last incident date.

