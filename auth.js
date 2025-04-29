const express = require('express');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const User = require('./models/User'); // Adjust the path if needed
const router = express.Router();

// Sign Up Route
router.post('/signup', async (req, res) => {
  const { email, password } = req.body;

  try {
    // Check if user already exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      return res.status(400).send('User already exists');
    }

    // Hash password and create user
    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = new User({ email, password: hashedPassword });
    await newUser.save();

    // Redirect to dashboard
    res.redirect('/home.html');
  } catch (err) {
    console.error('Signup error:', err);
    res.status(500).send('Internal Server Error');
  }
});

// Sign In Route
router.post('/signin', async (req, res) => {
  const { email, password } = req.body;

  try {
    // Check user existence
    const user = await User.findOne({ email });
    if (!user) return res.status(400).send('Invalid credentials');

    // Compare password
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) return res.status(400).send('Invalid credentials');

    // Optional JWT token (for future use)
    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, {
      expiresIn: '1h',
    });

    // Set cookie (optional): res.cookie('token', token, { httpOnly: true });

    // Redirect to dashboard
    res.redirect('/home.html');
  } catch (err) {
    console.error('Signin error:', err);
    res.status(500).send('Internal Server Error');
  }
});

module.exports = router;
