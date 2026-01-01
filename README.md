Workflow

The user signs up and logs in to the application.

After successful login, a JWT token is issued to authenticate the user.

While authenticated, the user submits a comment.

The comment is analyzed using TextBlob to determine whether it is positive or negative.

The comment, sentiment result, and user information are stored in the sentiment analysis table.

The sentiment analysis result returned by TextBlob is sent back in the API response.
