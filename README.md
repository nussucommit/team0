# team0blog README

## ERD / DB Schema
Available on [LucidChart](https://lucid.app/lucidchart/1e724cd3-96a3-4ccb-8882-86f0eb65a756/edit?viewport_loc=-190%2C116%2C2560%2C1168%2C0_0&invitationId=inv_dbb6ec66-c1e8-4a25-a315-0d4320e5f49c)

## Responses
Responses are formatted as JSON objects.

## REST API Endpoints
### `results`
- Returns a list of ordered posts that match the query parameters
- Returns all posts by default and a blank JSON object if no posts meet the query
- Supported request methods:

| METHOD | ACTION                | PARAMETERS               |
|--------|-----------------------|--------------------------|
| GET    | Return search results | username, content, order |

- `username` is strict and requires exact data
- `content` returns all posts which contain the query string
- List is ordered chronically showing old posts first by default, pass `order=1` to reverse the order

### `post/<integer:post_id>`
- CRUD functionalities for a singular post

| METHOD | ACTION                   | PARAMETERS                      |
|--------|--------------------------|---------------------------------|
| GET    | Returns a single post    | id                              |
| POST   | Creates a new post       | id, user, title, content        |
| PUT    | Edits an existing post   | id, user, title, content, likes |
| DELETE | Deletes an existing post | id                              |

- `id` is passed via the URL

### `post/comments/<integer:post_id>`
- Returns all corresponding comments under a singular post

| METHOD | ACTION              | PARAMETERS |
|--------|---------------------|------------|
| GET    | Return all comments | post       |

- `post` is passed via the URL

### `comment/<integer:comment_id>`
- CRUD functionalities for a singular comment

| METHOD | ACTION                      | PARAMETERS                     |
|--------|-----------------------------|--------------------------------|
| GET    | Returns a single comment    | id                             |
| POST   | Creates a new comment       | id, user, post, content        |
| PUT    | Edits an existing comment   | id, user, post, content, likes |
| DELETE | Deletes an existing comment | id                             |

- `id` is passed via the URL

## Search:
### Find Post
- `GET` call from `Post` table to display title, userid, datetime via `/results?c=content&u=userid`
- Sort as a function in javascript. 

## Authentication ( By Djoser Token Based)

NOTE: If Authetication by simple jwt , use their documentation at https://django-rest-framework-simplejwt.readthedocs.io/en/latest/rest_framework_simplejwt.html


### `auth/users/`
- User Sign-up (Addition to database)

|  METHOD   |            ACTION                   |          PARAMETERS                |
| --------- | ----------------------------------- | ---------------------------------- |
|  POST     | Adds the username and password      | username , password , re_password  |

### `auth/token/login/`
- Creates a token for the user
  
| METHOD  |            ACTION                 |          PARAMETERS              |
|---------|-----------------------------------|----------------------------------|
| POST    |  Sends username for authentication| username , password.             |

### `auth/token/logout/`
- User logs out 

| METHOD  |            ACTION                 |          PARAMETERS              |
|---------|-----------------------------------|----------------------------------|
| POST    | Sends username and password       | username , password.             |
