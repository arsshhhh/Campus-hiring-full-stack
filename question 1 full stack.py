const express = require("express");
const app = express();
const PORT = 3001;

// Sample data
const users = [
  { id: 1, name: "User A", postCount: 50 },
  { id: 2, name: "User B", postCount: 40 },
  { id: 3, name: "User C", postCount: 35 },
  { id: 4, name: "User D", postCount: 30 },
  { id: 5, name: "User E", postCount: 25 },
  { id: 6, name: "User F", postCount: 20 },
];

const posts = [
  { id: 1, content: "Post 1", commentCount: 100, timestamp: 1700000000 },
  { id: 2, content: "Post 2", commentCount: 150, timestamp: 1700001000 },
  { id: 3, content: "Post 3", commentCount: 200, timestamp: 1700002000 },
  { id: 4, content: "Post 4", commentCount: 180, timestamp: 1700003000 },
  { id: 5, content: "Post 5", commentCount: 90, timestamp: 1700004000 },
];

// API to fetch top 5 users by post count
app.get("/users", (req, res) => {
  const topUsers = users.sort((a, b) => b.postCount - a.postCount).slice(0, 5);
  res.json(topUsers);
});

// API to fetch top or latest posts
app.get("/posts", (req, res) => {
  const type = req.query.type;
  let sortedPosts;

  if (type === "popular") {
    sortedPosts = posts.sort((a, b) => b.commentCount - a.commentCount);
  } else if (type === "latest") {
    sortedPosts = posts.sort((a, b) => b.timestamp - a.timestamp);
  } else {
    return res.status(400).json({ error: "Invalid type parameter. Use 'latest' or 'popular'." });
  }

  res.json(sortedPosts);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

