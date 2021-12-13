# team0

## Notes for reference

## Authentication Feature :
### Sign up
- `POST` to `User` table via `/sign-up?u=userid&p=password`
- It should add an entry to the database, with the primary key as user id and another column with passwords. 
### Sign in
- `GET` call from the database, to authenticate the user via `/authenticate?u=userid&p=password`
- Username and password are parameters for the get call.
- It should check the database for username and password, if there exists a user matching then return success, if not then error. 

## Posts:
### Write post
- `POST` to `Post` table via `/pwrite?p=postid`
### Like post
- `PUT` likes +1 via `/plike?p=postid`
### Edit post
- `PUT` content via `/pedit?p=postid`
### Delete post
- `DELETE` all information about the post via `/pdelete?p=postid`
### Read post
- `GET` call from `Post` table to display via`/pread?p=postid`

## Comments:
### Write comments
- `POST` content, datetime to `Comment` table via `/cwrite?c=commentid`
### Like comment
- `PUT` likes +1 via `/clike?c=commentid`
### Update comments
- `PUT` content via `/cedit?c=commentid`
### Delete comments
- `DELETE` all information of the comment via `/cdelete?c=commentid`
### Read comments
- `GET` call from `Comment` table to display via `/cread?c=commentid`

## Search:
### Find Post
- `GET` call from `Post` table to display title, userid, datetime via `/results?c=content&u=userid`
- Sort as a function in javascript. 
