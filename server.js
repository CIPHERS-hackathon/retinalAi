const express = require('express');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth'); // adjust path
const bodyParser = require('body-parser');
require('dotenv').config();

const app = express();
app.use(express.static('public')); // to serve home.html etc.
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.use('/', authRoutes);

mongoose.connect(process.env.MONGO_URI)
  .then(() => {
    app.listen(3000, () => console.log('Server running on port 3000'));
  })
  .catch(err => console.error('DB connection error:', err));
