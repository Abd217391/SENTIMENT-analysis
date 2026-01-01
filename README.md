<h2>Workflow</h2>

<ol>
  <li>The user signs up and logs in to the application.</li>
  <li>After successful login, a <strong>JWT token</strong> is issued to authenticate the user.</li>
  <li>While authenticated, the user submits a comment.</li>
  <li>The comment is analyzed using <strong>TextBlob</strong> to determine whether it is positive or negative.</li>
  <li>The comment, sentiment result, and user information are stored in the <strong>sentiment analysis table</strong>.</li>
  
</ol>

