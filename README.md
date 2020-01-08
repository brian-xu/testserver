#testserver

Experimenting with handling SQL requests with PyMySQL in Flask

The purpose of this project was to create a thread-safe SQL handler in Python.

SELECT operations are read-only and should be able to be handled synchronously. However, they still require separate connections to the MySQL database because PyMySQL is not thread safe.

From reading the PyMySQL documentation, I thought the following code would be sufficient:

```python
def threaded_select(self):
    with self.connection().cursor() as cursor:
        cursor.execute("SELECT * FROM `test_table` ORDER BY id DESC LIMIT 6")
        messages = cursor.fetchall()
        cursor.close()
    return json.dumps(messages)
```

However, I was met with packet size errors when using this code. Perhaps there is a gap in my understanding/implementation or a better way to do it than my current implementation.

INSERT operations modify the database and need to be handled asynchronously. I used a semaphore to make sure that only one connection is modifying the database at once. Funnily enough, this asynchronous nature lets me use one connection to handle all insertions.

# Why?

Educational purposes, mostly. I will most likely use this handler for any web applications I build in the future, unless I decide to learn other technologies. It's not amazing, but it handles somewhere between 150-200 requests per second which is far greater than any load I'm expecting.