const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// define the Schema (the structure of the article)
const userSchema = new Schema({
  fireName: String,
  lastName: String,
  email: String,
  phoneNumber: String,
  age: Number,
  country: String,
  gender: String,
}, { timestamps: true });

const loginSchema = new Schema({
  name: {
    type: String,
    required: true
  },
  password: {
    type: String,
    required: true
  }
})

// Create a model based on that schema
const User = mongoose.model("customer", userSchema);
const login = mongoose.model("login", loginSchema);

// export the model
module.exports = {User, login};
