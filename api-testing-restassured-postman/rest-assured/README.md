# API Testing – Postman & Rest Assured

This project showcases two approaches to API testing using the [JSONPlaceholder](https://jsonplaceholder.typicode.com) public REST API:

---

## Postman

| Endpoint | Method | Status |
|----------|--------|--------|
| `/posts` | GET    | 200 |
| `/posts` | POST   | 201 |

Run via Postman Runner or manually import the collection

---

## Rest Assured (Java + TestNG)

| File | Test |
|------|------|
| `GetPostsTest.java` | Validates GET /posts |
| `CreatePostTest.java` | Validates POST /posts |

### How to Run:
```bash
cd rest-assured
mvn test
